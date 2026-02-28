# Improving Kitchen Prep Time Prediction via Signal Reconstruction

## Team
RockStar - Saurabh Bhosale & Krunal Kadam.

---

## Problem Understanding

KPT predictions today rely heavily on merchant-marked Food Order Ready (FOR) signals.
These signals are operationally biased and introduce systematic noise into model labels.

This results in:
- Early rider arrivals
- Idle fleet time
- ETA volatility
- Reduced platform efficiency

We identified this as a **data-truth problem rather than a modelling problem**.

---

## Proposed Solution: Kitchen Signal Reconstruction Layer (KSRL)

We introduce a passive intelligence layer that reconstructs true food readiness
using operational telemetry already available within Zomato’s ecosystem.

No additional hardware or POS integrations are required.

---

## Signals Used

1. Rider arrival and dwell behaviour  
2. Merchant historical throughput patterns  
3. Time-of-day rush modelling  
4. Cuisine-level preparation variability  
5. Merchant signal reliability scoring  

---

## Key Innovation: Signal Trust Scoring

We dynamically estimate how reliable each merchant’s FOR signal is
and adjust its contribution to KPT estimation.

---

## System Architecture

Event-driven microservice that:
- Consumes order lifecycle events
- Estimates Kitchen Load Index (KLI)
- Computes Merchant Trust Score (STS)
- Produces cleaned KPT signal

This feeds directly into the existing KPT model.

---

## Scalability

- Works for 300K+ merchants
- No integration dependency
- O(1) computation per order
- Stream-processing compatible

---

## Simulation Results

Using synthetic but behaviourally realistic data:

| Metric | Improvement |
|--------|-------------|
Rider Wait Time | ↓ ~20% |
ETA Prediction Error | ↓ ~12% |
Operational Stability | Improved |

---

## A/B Testing Strategy

We simulate a 50/50 rollout and observe statistically significant
reduction in rider idle time and ETA variance.

---

## Why This Works

Instead of building a better model,
we provide the model with **better ground-truth signals**.

---

## Deployment Plan

Phase 1: Silent evaluation alongside current system  
Phase 2: Partial rollout in high-density cities  
Phase 3: Nationwide activation  

---

## Conclusion

Improving signal quality is the highest-leverage way to enhance
KPT prediction at Zomato’s scale.

Our approach is:
- Scalable
- Non-invasive
- Immediately deployable
