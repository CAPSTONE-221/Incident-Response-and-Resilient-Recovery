"""
Module: encoder_scaler.py
Description: Feature scaling and categorical encoding with strict data-leakage prevention
             and artifact persistence.
"""

import os
import joblib
import pandas as pd
import numpy as np
from typing import List, Optional, Dict, Any
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler, LabelEncoder

class FeatureTransformer:
    def __init__(
        self,
        scaler_type: str = "RobustScaler",
        categorical_columns: Optional[List[str]] = None,
        target_columns: Optional[List[str]] = None,
        artifacts_dir: Optional[str] = None
    ):
        self.scaler_type = scaler_type
        self.categorical_columns = categorical_columns or []
        self.target_columns = target_columns or []
        self.artifacts_dir = artifacts_dir
        
        # Initialize scaler
        if scaler_type == "RobustScaler":
            self.scaler = RobustScaler()
        elif scaler_type == "MinMaxScaler":
            self.scaler = MinMaxScaler()
        else:
            self.scaler = StandardScaler()
            
        self.label_encoders: Dict[str, LabelEncoder] = {}
        self.target_encoders: Dict[str, LabelEncoder] = {}
        self.num_features_: List[str] = []
        self.fitted_ = False

    def fit(self, df: pd.DataFrame) -> "FeatureTransformer":
        """Fits scalers and encoders ONLY on training features (prevents data leakage)."""
        df_work = df.copy()
        
        # 1. Identify numerical feature columns (excluding target columns)
        self.num_features_ = [
            c for c in df_work.select_dtypes(include=[np.number]).columns
            if c not in self.target_columns and c not in self.categorical_columns
        ]
        
        # 2. Fit numerical scaler
        if self.num_features_:
            self.scaler.fit(df_work[self.num_features_])

        # 3. Fit categorical encoders
        for col in self.categorical_columns:
            if col in df_work.columns:
                le = LabelEncoder()
                # Include an 'UNKNOWN' category for handling unseen test categories
                unique_vals = list(df_work[col].astype(str).unique())
                if "UNKNOWN" not in unique_vals:
                    unique_vals.append("UNKNOWN")
                le.fit(unique_vals)
                self.label_encoders[col] = le

        # 4. Fit target encoders for any categorical target labels
        for col in self.target_columns:
            if col in df_work.columns and df_work[col].dtype == "object":
                te = LabelEncoder()
                te.fit(df_work[col].astype(str))
                self.target_encoders[col] = te

        self.fitted_ = True
        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transforms input dataframe using pre-fitted transformers."""
        if not self.fitted_:
            raise ValueError("FeatureTransformer must be fitted before calling transform().")

        df_out = df.copy()

        # 1. Transform numerical features
        if self.num_features_:
            scaled_vals = self.scaler.transform(df_out[self.num_features_])
            df_out[self.num_features_] = scaled_vals

        # 2. Transform categorical features (map unseen values to 'UNKNOWN')
        for col, le in self.label_encoders.items():
            if col in df_out.columns:
                known_classes = set(le.classes_)
                df_out[col] = df_out[col].astype(str).apply(
                    lambda x: x if x in known_classes else "UNKNOWN"
                )
                df_out[col] = le.transform(df_out[col])

        # 3. Transform categorical targets if present
        for col, te in self.target_encoders.items():
            if col in df_out.columns:
                known = set(te.classes_)
                # Keep original if binary integer, else transform
                if not pd.api.types.is_numeric_dtype(df_out[col]):
                    df_out[col] = df_out[col].astype(str).apply(lambda x: x if x in known else list(known)[0])
                    df_out[f"{col}_encoded"] = te.transform(df_out[col])

        return df_out

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return self.fit(df).transform(df)

    def save_artifacts(self, name_prefix: str) -> Dict[str, str]:
        """Saves fitted scalers and encoders to artifacts directory."""
        if not self.artifacts_dir:
            return {}
        os.makedirs(self.artifacts_dir, exist_ok=True)
        
        saved_paths = {}
        scaler_path = os.path.join(self.artifacts_dir, f"{name_prefix}_{self.scaler_type}.joblib")
        joblib.dump(self.scaler, scaler_path)
        saved_paths["scaler"] = scaler_path

        encoders_path = os.path.join(self.artifacts_dir, f"{name_prefix}_encoders.joblib")
        joblib.dump({
            "label_encoders": self.label_encoders,
            "target_encoders": self.target_encoders,
            "num_features": self.num_features_
        }, encoders_path)
        saved_paths["encoders"] = encoders_path

        return saved_paths
