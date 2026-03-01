from src.simulator import generate_merchants, generate_orders
from src.reconstruction import compute_merchant_sts, correct_for, compute_kli, compute_lm, predict_kpt
from src.metrics import evaluate

import numpy as np

print("Generating data...")
merchants = generate_merchants()
orders = generate_orders(merchants)

from src.reconstruction import compute_merchant_sts

print("Computing Merchant STS...")
merchant_sts = compute_merchant_sts(orders)

print("Applying corrections...")

orders["for_corrected"] = orders.apply(
    lambda x: correct_for(x, merchant_sts),
    axis=1
)

orders["kli"] = orders["hour"].apply(compute_kli)
orders["lm"] = orders["kli"].apply(compute_lm)

# Contextual baseline (F6 simplified)
cb = np.percentile(orders["true_prep"], 75)

orders["predicted_kpt"] = orders.apply(
    lambda x: predict_kpt(cb, x["lm"], merchant_sts[x["merchant_id"]]),
    axis=1
)

orders = evaluate(orders)

orders = evaluate(orders)

print("\n=== LABEL QUALITY (reference) ===")
print("Baseline Label Error:", orders["baseline_error"].mean())
print("KSRL Label Error:", orders["ksrl_label_error"].mean())

print("\n=== OPERATIONAL IMPACT (key metric) ===")
print("Avg Rider Wait (Baseline):", orders["baseline_wait"].mean())
print("Avg Rider Wait (KSRL):", orders["ksrl_wait"].mean())

import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1️⃣ Rider Wait Comparison
# -----------------------------
plt.figure()
plt.bar(
    ["Baseline", "KSRL"],
    [orders["baseline_wait"].mean(), orders["ksrl_wait"].mean()]
)
plt.title("Average Rider Wait Time Reduction")
plt.ylabel("Minutes")
plt.savefig("outputs/rider_wait_reduction.png")
plt.close()

# -----------------------------
# 2️⃣ Rush Hour Comparison
# -----------------------------
orders["period"] = orders["hour"].apply(
    lambda x: "Rush" if (12 <= x <= 14 or 19 <= x <= 22) else "Normal"
)

rush_stats = orders.groupby("period")[["baseline_wait", "ksrl_wait"]].mean()

rush_stats.plot(kind="bar")
plt.title("Rider Wait During Rush vs Normal Hours")
plt.ylabel("Average Wait (Minutes)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/rush_hour_comparison.png")
plt.close()

# -----------------------------
# 3️⃣ Error Distribution
# -----------------------------
plt.figure()
sns.kdeplot(orders["baseline_error"], label="Baseline")
sns.kdeplot(orders["ksrl_label_error"], label="KSRL")
plt.title("Label Error Distribution Comparison")
plt.xlabel("Absolute Error")
plt.legend()
plt.savefig("outputs/error_distribution.png")
plt.close()

print("\nCharts saved inside 'outputs' folder.")