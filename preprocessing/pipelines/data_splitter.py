"""
Module: data_splitter.py
Description: Stratified splitting of datasets into Train, Validation, and Test sets
             with strict data leakage prevention.
"""

import pandas as pd
import numpy as np
from typing import Tuple, Optional, Dict, Any
from sklearn.model_selection import train_test_split

class DataSplitter:
    def __init__(
        self,
        train_ratio: float = 0.70,
        val_ratio: float = 0.15,
        test_ratio: float = 0.15,
        random_seed: int = 42
    ):
        if not np.isclose(train_ratio + val_ratio + test_ratio, 1.0):
            raise ValueError("train_ratio + val_ratio + test_ratio must sum to 1.0")
            
        self.train_ratio = float(train_ratio)
        self.val_ratio = float(val_ratio)
        self.test_ratio = float(test_ratio)
        self.random_seed = int(random_seed)

    def split(
        self,
        df: pd.DataFrame,
        stratify_col: Optional[str] = None
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """Performs two-stage stratified splitting: (1) Train vs (Val+Test), (2) Val vs Test."""
        val_test_ratio = self.val_ratio + self.test_ratio
        relative_test_ratio = self.test_ratio / val_test_ratio

        stratify_series = None
        if stratify_col and stratify_col in df.columns:
            counts = df[stratify_col].value_counts()
            valid_classes = counts[counts >= 2].index
            df_filtered = df[df[stratify_col].isin(valid_classes)].copy()
            stratify_series = df_filtered[stratify_col]
        else:
            df_filtered = df.copy()

        # Step 1: Split into Train and (Val + Test)
        train_df, val_test_df = train_test_split(
            df_filtered,
            test_size=val_test_ratio,
            random_state=self.random_seed,
            stratify=stratify_series
        )

        # Step 2: Split (Val + Test) into Val and Test
        stratify_val_test = None
        if stratify_col and stratify_col in val_test_df.columns:
            stratify_val_test = val_test_df[stratify_col]

        val_df, test_df = train_test_split(
            val_test_df,
            test_size=relative_test_ratio,
            random_state=self.random_seed,
            stratify=stratify_val_test
        )

        # Verify no index leakage
        train_idx = set(train_df.index)
        val_idx = set(val_df.index)
        test_idx = set(test_df.index)
        assert len(train_idx.intersection(val_idx)) == 0, "Data leakage detected: train and val share indices!"
        assert len(train_idx.intersection(test_idx)) == 0, "Data leakage detected: train and test share indices!"
        assert len(val_idx.intersection(test_idx)) == 0, "Data leakage detected: val and test share indices!"

        return train_df.reset_index(drop=True), val_df.reset_index(drop=True), test_df.reset_index(drop=True)

    def get_split_stats(
        self,
        train_df: pd.DataFrame,
        val_df: pd.DataFrame,
        test_df: pd.DataFrame
    ) -> Dict[str, Any]:
        total = int(len(train_df) + len(val_df) + len(test_df))
        n_train = int(len(train_df))
        n_val = int(len(val_df))
        n_test = int(len(test_df))
        return {
            "total_samples": total,
            "train_samples": n_train,
            "train_percent": round(float(n_train / total) * 100, 2),
            "val_samples": n_val,
            "val_percent": round(float(n_val / total) * 100, 2),
            "test_samples": n_test,
            "test_percent": round(float(n_test / total) * 100, 2)
        }
