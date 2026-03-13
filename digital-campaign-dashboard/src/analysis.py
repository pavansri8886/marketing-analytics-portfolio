"""
analysis.py
Digital Campaign Performance Analytics Pipeline.
Computes KPIs across channels, regions, and time periods.
"""
import pandas as pd
import numpy as np
import json
import os

df = pd.read_csv("data/campaign_data.csv", parse_dates=["date"])
os.makedirs("reports", exist_ok=True)

print("=" * 60)
print("DIGITAL CAMPAIGN PERFORMANCE ANALYTICS")
print("=" * 60)

# KPI 1: Overall summary
total_spend   = df["spend"].sum()
total_revenue = df["revenue"].sum()
total_conv    = df["conversions"].sum()
total_clicks  = df["clicks"].sum()
overall_roas  = round(total_revenue / total_spend, 2)
overall_ctr   = round((total_clicks / df["impressions"].sum()) * 100, 2)

print(f"\n[KPI 1] Overall Performance")
print(f"  Total Spend:       €{total_spend:,.0f}")
print(f"  Total Revenue:     €{total_revenue:,.0f}")
print(f"  Overall ROAS:      {overall_roas}x")
print(f"  Overall CTR:       {overall_ctr}%")
print(f"  Total Conversions: {total_conv:,}")

# KPI 2: Channel performance
channel_kpis = df.groupby("channel").agg(
    total_spend=("spend", "sum"),
    total_revenue=("revenue", "sum"),
    total_clicks=("clicks", "sum"),
    total_impressions=("impressions", "sum"),
    total_conversions=("conversions", "sum"),
).round(2).reset_index()
channel_kpis["roas"]       = (channel_kpis["total_revenue"] / channel_kpis["total_spend"]).round(2)
channel_kpis["ctr_pct"]    = (channel_kpis["total_clicks"] / channel_kpis["total_impressions"] * 100).round(2)
channel_kpis["cpa"]        = (channel_kpis["total_spend"] / channel_kpis["total_conversions"]).round(2)
channel_kpis["status"]     = channel_kpis["roas"].apply(lambda x: "STRONG" if x >= 3 else ("AVERAGE" if x >= 1.5 else "WEAK"))
channel_kpis = channel_kpis.sort_values("roas", ascending=False)

print(f"\n[KPI 2] Channel Performance:")
print(channel_kpis[["channel","total_spend","total_revenue","roas","ctr_pct","cpa","status"]].to_string(index=False))

# KPI 3: Monthly trend
df["month"] = df["date"].dt.month
monthly = df.groupby("month").agg(
    spend=("spend","sum"),
    revenue=("revenue","sum"),
    conversions=("conversions","sum"),
    clicks=("clicks","sum"),
    impressions=("impressions","sum")
).reset_index()
monthly["roas"]    = (monthly["revenue"] / monthly["spend"]).round(2)
monthly["ctr_pct"] = (monthly["clicks"] / monthly["impressions"] * 100).round(2)

print(f"\n[KPI 3] Monthly Trend:")
print(monthly.to_string(index=False))

# KPI 4: Region performance
region_kpis = df.groupby("region").agg(
    total_spend=("spend","sum"),
    total_revenue=("revenue","sum"),
    total_conversions=("conversions","sum"),
).reset_index()
region_kpis["roas"] = (region_kpis["total_revenue"] / region_kpis["total_spend"]).round(2)
region_kpis["cpa"]  = (region_kpis["total_spend"] / region_kpis["total_conversions"]).round(2)
region_kpis = region_kpis.sort_values("roas", ascending=False)

print(f"\n[KPI 4] Region Performance:")
print(region_kpis.to_string(index=False))

# KPI 5: Campaign performance
campaign_kpis = df.groupby("campaign").agg(
    spend=("spend","sum"),
    revenue=("revenue","sum"),
    conversions=("conversions","sum"),
).reset_index()
campaign_kpis["roas"] = (campaign_kpis["revenue"] / campaign_kpis["spend"]).round(2)
campaign_kpis = campaign_kpis.sort_values("roas", ascending=False)

print(f"\n[KPI 5] Campaign Performance:")
print(campaign_kpis.to_string(index=False))

# Save reports
channel_kpis.to_csv("reports/channel_performance.csv", index=False)
monthly.to_csv("reports/monthly_trend.csv", index=False)
region_kpis.to_csv("reports/region_performance.csv", index=False)
campaign_kpis.to_csv("reports/campaign_performance.csv", index=False)

summary = {
    "total_spend": f"€{total_spend:,.0f}",
    "total_revenue": f"€{total_revenue:,.0f}",
    "overall_roas": overall_roas,
    "overall_ctr_pct": overall_ctr,
    "total_conversions": int(total_conv),
    "best_channel": channel_kpis.iloc[0]["channel"],
    "best_region": region_kpis.iloc[0]["region"],
}
with open("reports/summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print(f"\n[OUTPUT] Reports saved.")
print(json.dumps(summary, indent=2))
