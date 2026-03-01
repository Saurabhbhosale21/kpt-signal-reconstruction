import numpy as np

def evaluate(df):
    # Label error (for reference only)
    df["baseline_error"] = abs(df["for_mark"] - df["true_prep"])
    df["ksrl_label_error"] = abs(df["for_corrected"] - df["true_prep"])

    # Operational metric: rider waiting time
    df["baseline_wait"] = np.maximum(0, df["true_prep"] - df["rider_arrival"])

    # If system had used corrected readiness, dispatch would align closer:
    df["ksrl_wait"] = np.maximum(0, df["true_prep"] - df["for_corrected"])

    return df