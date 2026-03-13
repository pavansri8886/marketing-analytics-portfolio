"""
generate_data.py
Generates synthetic e-commerce performance data.
"""
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

np.random.seed(99)
random.seed(99)

CHANNELS = ["Organic Search", "Paid Search", "Email", "Social Media", "Direct"]
CATEGORIES = ["Power Tools", "Accessories", "Consumables", "Parts", "Safety Equipment"]

records = []
start = datetime(2024, 1, 1)
for i in range(365):
    date = start + timedelta(days=i)
    for channel in CHANNELS:
        sessions     = random.randint(200, 8000)
        bounce_rate  = round(random.uniform(0.25, 0.70), 3)
        pages_sess   = round(random.uniform(1.5, 6.5), 1)
        add_to_cart  = round(random.uniform(0.05, 0.25), 3)
        checkout     = round(add_to_cart * random.uniform(0.4, 0.8), 3)
        conv_rate    = round(checkout * random.uniform(0.4, 0.9), 4)
        orders       = int(sessions * conv_rate)
        aov          = round(random.uniform(45, 380), 2)
        revenue      = round(orders * aov, 2)
        records.append({
            "date": date.strftime("%Y-%m-%d"),
            "channel": channel,
            "sessions": sessions,
            "bounce_rate_pct": round(bounce_rate * 100, 1),
            "pages_per_session": pages_sess,
            "add_to_cart_rate_pct": round(add_to_cart * 100, 1),
            "checkout_rate_pct": round(checkout * 100, 1),
            "conv_rate_pct": round(conv_rate * 100, 2),
            "orders": orders,
            "avg_order_value": aov,
            "revenue": revenue,
        })

df = pd.DataFrame(records)
df["cart_abandonment_pct"] = (100 - (df["conv_rate_pct"] / df["add_to_cart_rate_pct"] * 100)).clip(0, 100).round(1)
os.makedirs("data", exist_ok=True)
df.to_csv("data/ecommerce_data.csv", index=False)
print(f"Generated {len(df)} e-commerce records.")
