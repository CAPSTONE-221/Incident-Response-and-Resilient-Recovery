"""
Module: feature_selector.py
Description: Feature selection via VarianceThreshold and pairwise collinearity filtering.
"""

import pandas as pd
import numpy as np
from typing import List, Optional, Dict, Any
from sklearn.feature_selection import VarianceThreshold

class FeatureSelector:
    def __init__(
        self,
        variance_threshold: float = 0.0001,
        correlation_threshold: float = 0.98,
        exclude_columns: Optional[List[str]] = None
    ):
        self.variance_threshold = variance_threshold
        self.correlation_threshold = correlation_threshold
        self.exclude_columns = exclude_columns or []
        self.selected_features_: List[str] = []
        self.dropped_variance_cols_: List[str] = []
        self.dropped_correlation_cols_: List[str] = []

    def fit(self, df: pd.DataFrame) -> "FeatureSelector":
        """Identifies low-variance and collinear features on the training set only."""
        num_cols = [
            c for c in df.select_dtypes(include=[np.number]).columns
            if c not in self.exclude_columns
        ]

        if not num_cols:
            self.selected_features_ = list(df.columns)
            return self

        # 1. Variance Threshold
        vt = VarianceThreshold(threshold=self.variance_threshold)
        vt.fit(df[num_cols])
        var_mask = vt.get_support()
        survived_var_cols = [num_cols[i] for i, m in enumerate(var_mask) if m]
        self.dropped_variance_cols_ = [num_cols[i] for i, m in enumerate(var_mask) if not m]

        # 2. Pairwise Correlation Threshold
        if len(survived_var_cols) > 1:
            corr_matrix = df[survived_var_cols].corr().abs()
            upper_triangle = corr_matrix.where(
                np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
            )
            self.dropped_correlation_cols_ = [
                col for col in upper_triangle.columns
                if any(upper_triangle[col] > self.correlation_threshold)
            ]
            final_num_cols = [c for c in survived_var_cols if c not in self.dropped_correlation_cols_]
        else:
            final_num_cols = survived_var_cols

        # Non-numeric columns + excluded targets are kept
        other_cols = [c for c in df.columns if c not in num_cols]
        self.selected_features_ = final_num_cols + other_cols

        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Keeps only selected features."""
        cols_to_keep = [c for c in self.selected_features_ if c in df.columns]
        return df[cols_to_keep]

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return self.fit(df).transform(df)
