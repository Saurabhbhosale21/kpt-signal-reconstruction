# Improving Kitchen Prep Time Prediction via Signal Reconstruction

## Team
RockStar - Saurabh Bhosale & Krunal Kadam.

# Kitchen Prep Time (KPT) Signal Reconstruction Layer (KSRL)

## 📌 Overview

Accurate Kitchen Prep Time (KPT) prediction is essential for reliable ETAs, efficient rider dispatch, and overall delivery platform performance.

In large-scale ecosystems like Zomato (300K+ merchants), even small inaccuracies in readiness signals can lead to:

- Early rider arrival and idle waiting
- ETA fluctuations for customers
- Poor fleet utilization
- Increased operational cost

This project proposes a **system-level solution** — not a new prediction model — to improve the **quality of signals entering existing KPT models**.

---

## ❗ Problem With Current Systems

Most platforms rely on **merchant-marked Food Order Ready (FOR)** signals to train and update KPT models.

However, these signals are often noisy because:

- Merchants mark food ready when the rider arrives (not when food is ready)
- Kitchen workload includes dine-in and other aggregators, invisible to the platform
- Manual marking behavior varies across time and restaurant types
- Human bias introduces inconsistent training labels

This leads to **systematic prediction errors**, not model limitations.

---

## 💡 Proposed Solution: Kitchen Signal Reconstruction Layer (KSRL)

We introduce a lightweight **Signal Reconstruction Layer** that corrects readiness signals using real-world behavioral observations — without modifying existing ML models.

### Core Idea

Instead of trusting merchant input blindly:

> Infer the true readiness time using rider interaction signals.

If a rider must wait, that wait reveals hidden preparation time.



This converts operational behavior into a corrective signal.

---

## 🧠 Key Components

### 1️⃣ Merchant Signal Trust Estimation

We analyze historical dwell behavior to estimate how reliable a merchant’s readiness marking is.

Reliable merchants remain untouched.
Biased signals are automatically corrected.

---

### 2️⃣ Behavioral Signal Reconstruction

When rider wait is observed:

- We reconstruct the actual kitchen completion time.
- This removes bias introduced by premature FOR marking.

---

### 3️⃣ Rush-Aware Context Modeling

The simulation accounts for:

- Lunch/Dinner demand surges
- Cuisine-specific preparation variability
- Mixed merchant behaviors (honest vs biased)

This ensures scalability across heterogeneous restaurant ecosystems.

---

### 4️⃣ Model-Agnostic Deployment

KSRL does **not require**:

- Retraining ML models
- Merchant workflow changes
- New hardware
- Additional integrations

It acts as a preprocessing calibration layer.

---

## 📊 Evaluation Philosophy

Traditional evaluation focuses on prediction MAE.

However, operational systems care more about:

- Rider wait time
- Dispatch synchronization
- ETA stability
- Fleet productivity

Therefore, we evaluate business-aligned metrics.

---

## 📈 Simulation Results

| Metric | Baseline | With KSRL |
|--------|----------|-----------|
Average Rider Wait | ~2.5 minutes | ~0.03 minutes |
Dispatch Alignment | Inconsistent | Strongly Improved |
Operational Efficiency | Lower | Higher |

These results show that **improving signal fidelity alone** can dramatically enhance logistics performance.

---

## 📁 Project Structure
KPT-Signal-Reconstruction/
│
├── src/ # Core simulation and reconstruction logic
├── outputs/ # Generated evaluation visualizations
├── run_simulation.py # Main execution script
├── requirements.txt # Python dependencies
├── README.md # Project documentation



---

## ⚙️ How To Run The Project

### 1️⃣ Clone Repository
git clone <your-repo-url>
cd KPT-Signal-Reconstruction

---

### 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

---

### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

### 4️⃣ Run Simulation
python run_simulation.py

---

## 📊 Generated Outputs

Visualizations will be saved in:
outputs

Including:

- Rider wait reduction comparison
- Rush vs non-rush operational behavior
- Error distribution visualization

---

## 🏗️ Why This Approach Matters

Most optimization attempts focus on:

> Building more complex prediction models.

But real-world systems often fail due to **input signal distortion**, not model limitations.

KSRL demonstrates that:

✔ Correcting operational signals can outperform model tuning  
✔ Improvements scale instantly across hundreds of thousands of merchants  
✔ Deployment risk remains minimal

---

## 🚀 Future Extensions

- Passive sensing of kitchen load signals
- Cross-platform demand estimation
- Real-time confidence-adjusted dispatch
- Integration with adaptive ETA systems

---

## 👨‍💻 Use Case

This project demonstrates how **systems thinking + behavioral signal modeling** can unlock efficiency gains in logistics platforms without requiring disruptive technological changes.

---

## 📜 License / Usage

This project is developed for research and system-design demonstration purposes.

---
