"""
generate_data.py
Generates synthetic competitor benchmarking data for power tools market.
"""
import pandas as pd
import numpy as np
import random
import os

np.random.seed(77)
random.seed(77)

COMPETITORS = ["Ingersoll Rand", "Bosch Professional", "Makita", "DeWalt", "Milwaukee", "Metabo"]
CATEGORIES  = ["Impact Wrenches", "Drills", "Grinders", "Compressors", "Ratchets"]
MONTHS      = list(range(1, 13))

records = []
for comp in COMPETITORS:
    is_ir = comp == "Ingersoll Rand"
    for cat in CATEGORIES:
        base_price    = round(random.uniform(80, 450), 2)
        records.append({
            "brand": comp,
            "category": cat,
            "avg_price_eur": base_price,
            "product_count": random.randint(8, 45),
            "avg_rating": round(random.uniform(3.8, 4.9), 1),
            "review_count": random.randint(200, 8000),
            "in_stock_pct": round(random.uniform(0.72, 0.99) * 100, 1),
            "discount_pct": round(random.uniform(0, 0.25) * 100, 1),
            "seo_visibility_score": round(random.uniform(30, 95), 1),
            "paid_search_presence": random.choice([True, True, True, False]),
            "social_followers_k": round(random.uniform(5, 850), 1),
        })

product_df = pd.DataFrame(records)

# Monthly web traffic simulation
traffic_records = []
for comp in COMPETITORS:
    for month in MONTHS:
        traffic_records.append({
            "brand": comp,
            "month": month,
            "organic_sessions_k": round(random.uniform(10, 500), 1),
            "paid_sessions_k": round(random.uniform(5, 200), 1),
            "bounce_rate_pct": round(random.uniform(28, 65), 1),
            "avg_session_duration_sec": random.randint(90, 320),
            "share_of_voice_pct": round(random.uniform(5, 35), 1),
        })
traffic_df = pd.DataFrame(traffic_records)

os.makedirs("data", exist_ok=True)
product_df.to_csv("data/product_benchmarks.csv", index=False)
traffic_df.to_csv("data/traffic_benchmarks.csv", index=False)
print(f"Generated {len(product_df)} product records and {len(traffic_df)} traffic records.")
