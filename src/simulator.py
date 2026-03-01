import numpy as np
import pandas as pd

np.random.seed(42)


def generate_merchants(n=50):
    cuisines = ["Biryani", "Pizza", "NorthIndian", "Chinese", "Cafe"]

    merchants = pd.DataFrame({
        "merchant_id": range(n),
        "cuisine": np.random.choice(cuisines, n),
        "base_prep": np.random.uniform(8, 18, n),
        "bias_type": np.random.choice(
            ["honest", "delayed_for", "batch_marking"],
            n,
            p=[0.5, 0.3, 0.2]
        )
    })

    return merchants


def rush_multiplier(hour):
    if 12 <= hour <= 14:
        return 1.6
    elif 19 <= hour <= 22:
        return 1.8
    else:
        return 1.0


def generate_orders(merchants, n_orders=3000):
    rows = []

    for i in range(n_orders):

        m = merchants.sample(1).iloc[0]
        hour = np.random.randint(9, 23)

        rush = rush_multiplier(hour)

        # True kitchen completion time
        true_prep = np.random.normal(m.base_prep * rush, 2)

        # Rider dispatched slightly early (system prediction error)
        rider_arrival = true_prep - np.random.uniform(1, 4)

        # Merchant behavior simulation
        if m.bias_type == "honest":
            # Marks ready near actual completion
            for_mark = true_prep + np.random.uniform(-0.5, 0.5)

        elif m.bias_type == "delayed_for":
            # Marks ready when rider arrives
            for_mark = rider_arrival

        elif m.bias_type == "batch_marking":
            # Bulk marking around rider arrival
            for_mark = rider_arrival + np.random.uniform(-1, 1)

        # Pickup happens only when food is actually ready
        pickup_time = max(true_prep, rider_arrival)

        rows.append([
            i,
            m.merchant_id,
            m.cuisine,
            hour,
            true_prep,
            for_mark,
            rider_arrival,
            pickup_time
        ])

    return pd.DataFrame(rows, columns=[
        "order_id",
        "merchant_id",
        "cuisine",
        "hour",
        "true_prep",
        "for_mark",
        "rider_arrival",
        "pickup_time"
    ])