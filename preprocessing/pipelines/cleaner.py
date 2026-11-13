"""
Module: cleaner.py
Description: Robust cleaning for cybersecurity datasets (handles missing, infinite, duplicates, whitespace).
"""

import pandas as pd
import numpy as np
from typing import List, Optional, Tuple, Dict, Any

class DataCleaner:
    def __init__(self, drop_columns: Optional[List[str]] = None):
        self.drop_columns = drop_columns or []
        self.numeric_impute_values: Dict[str, float] = {}
        self.categorical_impute_values: Dict[str, str] = {}
        self.stats_: Dict[str, Any] = {}

    def fit(self, df: pd.DataFrame) -> "DataCleaner":
        """Calculates imputation statistics from the training set only (preventing data leakage)."""
        df_work = df.copy()
        for col in self.drop_columns:
            if col in df_work.columns:
                df_work = df_work.drop(columns=[col])

        # Replace infinite values with NaN for calculation
        df_work = df_work.replace([np.inf, -np.inf], np.nan)

        # Numerical columns: use median
        num_cols = df_work.select_dtypes(include=[np.number]).columns
        for col in num_cols:
            self.numeric_impute_values[col] = float(df_work[col].median()) if not df_work[col].isna().all() else 0.0

        # Categorical columns: use mode
        cat_cols = df_work.select_dtypes(include=["object", "string", "category"]).columns
        for col in cat_cols:
            mode_val = df_work[col].mode()
            self.categorical_impute_values[col] = str(mode_val[0]) if len(mode_val) > 0 else "UNKNOWN"

        return self

    def transform(self, df: pd.DataFrame, is_train: bool = False) -> pd.DataFrame:
        """Applies cleaning transformations."""
        initial_rows = len(df)
        df_clean = df.copy()

        # 1. Drop identifier / non-predictive columns
        for col in self.drop_columns:
            if col in df_clean.columns:
                df_clean = df_clean.drop(columns=[col])

        # 2. Clean string column whitespace and casing
        for col in df_clean.select_dtypes(include=["object", "string"]).columns:
            df_clean[col] = df_clean[col].astype(str).str.strip()

        # 3. Replace infinite values with NaN
        df_clean = df_clean.replace([np.inf, -np.inf], np.nan)

        # 4. Impute missing values using fitted statistics
        for col, val in self.numeric_impute_values.items():
            if col in df_clean.columns and df_clean[col].isna().any():
                df_clean[col] = df_clean[col].fillna(val)

        for col, val in self.categorical_impute_values.items():
            if col in df_clean.columns and df_clean[col].isna().any():
                df_clean[col] = df_clean[col].fillna(val)

        # 5. Drop duplicate rows on training set if requested
        duplicates_removed = 0
        if is_train:
            before_dup = len(df_clean)
            df_clean = df_clean.drop_duplicates()
            duplicates_removed = before_dup - len(df_clean)

        self.stats_ = {
            "initial_rows": initial_rows,
            "final_rows": len(df_clean),
            "duplicates_removed": duplicates_removed,
            "remaining_nulls": int(df_clean.isna().sum().sum())
        }

        return df_clean

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return self.fit(df).transform(df, is_train=True)

