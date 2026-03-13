"""
analysis.py
Competitor Benchmarking Analysis — pricing, digital presence, market share signals.
"""
import pandas as pd
import numpy as np
import json
import os

products = pd.read_csv("data/product_benchmarks.csv")
traffic  = pd.read_csv("data/traffic_benchmarks.csv")
os.makedirs("reports", exist_ok=True)

print("=" * 60)
print("COMPETITOR BENCHMARKING ANALYSIS")
print("=" * 60)

# 1. Pricing position
pricing = products.groupby("brand").agg(
    avg_price=("avg_price_eur","mean"),
    avg_rating=("avg_rating","mean"),
    total_products=("product_count","sum"),
    avg_discount=("discount_pct","mean"),
    avg_stock=("in_stock_pct","mean"),
).round(2).reset_index().sort_values("avg_price", ascending=False)

print(f"\n[1] Pricing & Product Position:")
print(pricing.to_string(index=False))

# 2. Digital presence
digital = products.groupby("brand").agg(
    seo_score=("seo_visibility_score","mean"),
    social_followers_k=("social_followers_k","mean"),
    paid_search_presence=("paid_search_presence","mean"),
).round(2).reset_index()

traffic_summary = traffic.groupby("brand").agg(
    avg_organic_k=("organic_sessions_k","mean"),
    avg_paid_k=("paid_sessions_k","mean"),
    avg_sov=("share_of_voice_pct","mean"),
    avg_bounce=("bounce_rate_pct","mean"),
).round(2).reset_index()

digital_full = digital.merge(traffic_summary, on="brand").sort_values("avg_sov", ascending=False)

print(f"\n[2] Digital Presence & Share of Voice:")
print(digital_full.to_string(index=False))

# 3. Category level pricing vs IR
ir_prices = products[products["brand"]=="Ingersoll Rand"][["category","avg_price_eur"]].rename(columns={"avg_price_eur":"ir_price"})
cat_comparison = products[products["brand"]!="Ingersoll Rand"].groupby(["brand","category"])["avg_price_eur"].mean().reset_index()
cat_comparison = cat_comparison.merge(ir_prices, on="category")
cat_comparison["price_diff_pct"] = ((cat_comparison["avg_price_eur"] - cat_comparison["ir_price"]) / cat_comparison["ir_price"] * 100).round(1)
cat_comparison["position"] = cat_comparison["price_diff_pct"].apply(lambda x: "IR CHEAPER" if x > 2 else ("IR PRICIER" if x < -2 else "SIMILAR"))

print(f"\n[3] Category Price Comparison vs Ingersoll Rand:")
print(cat_comparison[["brand","category","avg_price_eur","ir_price","price_diff_pct","position"]].to_string(index=False))

# 4. Rating comparison
ratings = products.groupby("brand").agg(
    avg_rating=("avg_rating","mean"),
    total_reviews=("review_count","sum"),
).round(2).reset_index().sort_values("avg_rating", ascending=False)

print(f"\n[4] Customer Rating Comparison:")
print(ratings.to_string(index=False))

# Save
pricing.to_csv("reports/pricing_benchmark.csv", index=False)
digital_full.to_csv("reports/digital_presence.csv", index=False)
cat_comparison.to_csv("reports/category_price_comparison.csv", index=False)
ratings.to_csv("reports/rating_comparison.csv", index=False)

ir_sov = digital_full[digital_full["brand"]=="Ingersoll Rand"]["avg_sov"].values[0]
top_competitor = digital_full[digital_full["brand"]!="Ingersoll Rand"].sort_values("avg_sov",ascending=False).iloc[0]["brand"]

summary = {
    "brands_analysed": len(products["brand"].unique()),
    "categories_covered": len(products["category"].unique()),
    "ir_avg_price": float(pricing[pricing["brand"]=="Ingersoll Rand"]["avg_price"].values[0]),
    "ir_avg_rating": float(ratings[ratings["brand"]=="Ingersoll Rand"]["avg_rating"].values[0]),
    "ir_share_of_voice_pct": float(ir_sov),
    "top_competitor_by_sov": top_competitor,
}
with open("reports/summary.json","w") as f:
    json.dump(summary, f, indent=2)
print(f"\n[OUTPUT] Reports saved.")
print(json.dumps(summary, indent=2))
