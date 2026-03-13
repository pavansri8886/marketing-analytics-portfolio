"""
generate_data.py
Generates synthetic digital marketing campaign performance data.
"""
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

np.random.seed(42)
random.seed(42)

CHANNELS = ["SEA", "Display", "Social Ads", "Email"]
CAMPAIGNS = ["Brand Awareness Q1", "Product Launch Q2", "Retargeting Q3", "Seasonal Promo Q4"]
REGIONS = ["France", "Germany", "UK", "Spain", "Italy"]

records = []
start = datetime(2024, 1, 1)
for i in range(365):
    date = start + timedelta(days=i)
    for channel in CHANNELS:
        for region in REGIONS:
            impressions = random.randint(5000, 80000)
            ctr = round(random.uniform(0.01, 0.08), 4)
            clicks = int(impressions * ctr)
            cpc = round(random.uniform(0.20, 3.50), 2)
            spend = round(clicks * cpc, 2)
            conv_rate = round(random.uniform(0.01, 0.06), 4)
            conversions = int(clicks * conv_rate)
            revenue = round(conversions * random.uniform(50, 400), 2)
            records.append({
                "date": date.strftime("%Y-%m-%d"),
                "channel": channel,
                "region": region,
                "campaign": random.choice(CAMPAIGNS),
                "impressions": impressions,
                "clicks": clicks,
                "spend": spend,
                "conversions": conversions,
                "revenue": revenue,
                "ctr": round(ctr * 100, 2),
                "cpc": cpc,
                "conv_rate": round(conv_rate * 100, 2),
            })

df = pd.DataFrame(records)
df["roas"] = (df["revenue"] / df["spend"].replace(0, 1)).round(2)
df["cpa"] = (df["spend"] / df["conversions"].replace(0, 1)).round(2)

os.makedirs("data", exist_ok=True)
df.to_csv("data/campaign_data.csv", index=False)
print(f"Generated {len(df)} campaign records.")
