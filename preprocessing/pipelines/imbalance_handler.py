"""
Module: imbalance_handler.py
Description: Analyzes class distributions and computes balanced class weights to address
             cyberattack vs. normal traffic class imbalance.
"""

import numpy as np
import pandas as pd
from typing import Dict, Any, Union
from sklearn.utils.class_weight import compute_class_weight

class ClassImbalanceHandler:
    def __init__(self, target_column: str):
        self.target_column = target_column
        self.class_counts_: Dict[str, int] = {}
        self.class_proportions_: Dict[str, float] = {}
        self.class_weights_: Dict[str, float] = {}

    def fit(self, y: pd.Series) -> "ClassImbalanceHandler":
        """Calculates class frequencies and inverse-frequency class weights."""
        y_clean = y.dropna()
        counts_dict = y_clean.value_counts().to_dict()
        self.class_counts_ = {str(k): int(v) for k, v in counts_dict.items()}
        total = int(len(y_clean))
        self.class_proportions_ = {str(k): round(float(v) / total, 4) for k, v in self.class_counts_.items()}

        classes = np.unique(y_clean)
        weights = compute_class_weight(class_weight="balanced", classes=classes, y=y_clean)
        self.class_weights_ = {str(cls): round(float(w), 4) for cls, w in zip(classes, weights)}

        return self

    def get_summary(self) -> Dict[str, Any]:
        """Returns distribution metrics and calculated class weights in native JSON-serializable types."""
        imbalance_ratio = 1.0
        if len(self.class_counts_) >= 2:
            counts = list(self.class_counts_.values())
            imbalance_ratio = round(float(max(counts)) / float(min(counts)), 2)

        return {
            "target_column": str(self.target_column),
            "num_classes": int(len(self.class_counts_)),
            "class_counts": self.class_counts_,
            "class_proportions": self.class_proportions_,
            "class_weights": self.class_weights_,
            "imbalance_ratio": float(imbalance_ratio)
        }
