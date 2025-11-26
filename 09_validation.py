import pandas as pd
import numpy as np

# ---------------------------------------------------------
# Basic binary classification metrics
# ---------------------------------------------------------

def compute_confusion_matrix(y_true, y_pred):
    TP = np.sum((y_true == 1) & (y_pred == 1))
    TN = np.sum((y_true == 0) & (y_pred == 0))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    FN = np.sum((y_true == 1) & (y_pred == 0))
    return TP, FP, TN, FN


def compute_scores(TP, FP, TN, FN):
    accuracy  = (TP + TN) / (TP + TN + FP + FN)
    precision = TP / (TP + FP) if TP + FP > 0 else 0
    recall    = TP / (TP + FN) if TP + FN > 0 else 0
    if (precision + recall) == 0:
        f1 = 0
    else:
        f1 = 2 * (precision * recall) / (precision + recall)
    return accuracy, precision, recall, f1


# ---------------------------------------------------------
# validate_thresholds()
# This is what the notebooks expect.
# ---------------------------------------------------------

def validate_thresholds(df, value_col, thresholds, obs_col="obs"):
    """
    df: DataFrame containing predictions + observed values
    value_col: column containing numeric DHI values
    thresholds: list of thresholds to evaluate (e.g. [25, 30, 40])
    obs_col: observed drought binary (0/1)

    Returns: DataFrame with metrics for each threshold
    """
    results = []

    for T in thresholds:
        df["pred"] = (df[value_col] >= T).astype(int)

        TP, FP, TN, FN = compute_confusion_matrix(df[obs_col], df["pred"])
        accuracy, precision, recall, f1 = compute_scores(TP, FP, TN, FN)

        results.append({
            "T": T,
            "TP": TP,
            "FP": FP,
            "TN": TN,
            "FN": FN,
            "Accuracy": accuracy,
            "Precision": precision,
            "Recall": recall,
            "F1": f1
        })

    return pd.DataFrame(results)
def compute_binary_metrics(y_true, y_pred):
    """
    Compatibility wrapper expected by older notebooks.
    Returns TP, FP, TN, FN, Accuracy, Precision, Recall, F1.
    """
    TP, FP, TN, FN = compute_confusion_matrix(y_true, y_pred)
    accuracy, precision, recall, f1 = compute_scores(TP, FP, TN, FN)

    return {
        "TP": TP,
        "FP": FP,
        "TN": TN,
        "FN": FN,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1": f1
    }
