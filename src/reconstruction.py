import numpy as np

# F3 - STS
import numpy as np

def compute_merchant_sts(df):
    """
    Compute STS per merchant using their own dwell behaviour.
    """
    merchant_sts = {}

    for merchant_id, group in df.groupby("merchant_id"):
        dwell = (group["pickup_time"] - group["rider_arrival"]).clip(lower=0)
        mean_dwell = dwell.mean()

        max_dwell = 2.0  # tolerance threshold
        sts = 1 - min(mean_dwell / max_dwell, 1)

        merchant_sts[merchant_id] = max(sts, 0)

    return merchant_sts

# F2 - Corrected FOR
def correct_for(row, merchant_sts):

    # Real waiting time (only positive wait counts)
    dwell = max(0, row["pickup_time"] - row["rider_arrival"])

    # If there is NO waiting → merchant signal already correct
    if dwell == 0:
        return row["for_mark"]

    # If waiting happened → reconstruct true readiness
    return row["for_mark"] + dwell

# F4 - KLI
def compute_kli(hour):
    if 12 <= hour <= 14 or 19 <= hour <= 22:
        return 0.8
    else:
        return 0.3

# F5 - Load Multiplier
def compute_lm(kli):
    return 1.0 + 0.65 * kli

# F7 - Final KPT Prediction
def predict_kpt(cb, lm, sts):
    volatility = 0.1
    sb = 1.0 + volatility * (1 - sts)
    return cb * lm * sb