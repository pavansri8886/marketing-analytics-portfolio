"""
analysis.py
E-commerce KPI Tracker — channel performance, conversion funnel, revenue trends.
"""
import pandas as pd
import numpy as np
import json
import os

df = pd.read_csv("data/ecommerce_data.csv", parse_dates=["date"])
os.makedirs("reports", exist_ok=True)

print("=" * 60)
print("E-COMMERCE KPI TRACKER")
print("=" * 60)

# Overall
total_rev    = df["revenue"].sum()
total_orders = df["orders"].sum()
avg_conv     = df["conv_rate_pct"].mean().round(2)
avg_bounce   = df["bounce_rate_pct"].mean().round(1)
avg_aov      = df["avg_order_value"].mean().round(2)

print(f"\n[KPI 1] Overall Summary")
print(f"  Total Revenue:    €{total_rev:,.0f}")
print(f"  Total Orders:     {total_orders:,}")
print(f"  Avg Conv Rate:    {avg_conv}%")
print(f"  Avg Bounce Rate:  {avg_bounce}%")
print(f"  Avg Order Value:  €{avg_aov}")

# Channel scorecard
channel = df.groupby("channel").agg(
    total_sessions=("sessions","sum"),
    total_orders=("orders","sum"),
    total_revenue=("revenue","sum"),
    avg_conv_rate=("conv_rate_pct","mean"),
    avg_bounce=("bounce_rate_pct","mean"),
    avg_aov=("avg_order_value","mean"),
    avg_cart_abandon=("cart_abandonment_pct","mean"),
).round(2).reset_index()
channel["revenue_per_session"] = (channel["total_revenue"] / channel["total_sessions"]).round(2)
channel["status"] = channel["avg_conv_rate"].apply(
    lambda x: "HIGH PERFORMER" if x >= 3 else ("AVERAGE" if x >= 1.5 else "NEEDS ATTENTION"))
channel = channel.sort_values("total_revenue", ascending=False)

print(f"\n[KPI 2] Channel Scorecard:")
print(channel[["channel","total_sessions","total_revenue","avg_conv_rate","avg_bounce","status"]].to_string(index=False))

# Monthly trend
df["month"] = df["date"].dt.month
monthly = df.groupby("month").agg(
    sessions=("sessions","sum"),
    orders=("orders","sum"),
    revenue=("revenue","sum"),
    avg_conv=("conv_rate_pct","mean"),
    avg_aov=("avg_order_value","mean"),
).round(2).reset_index()

print(f"\n[KPI 3] Monthly Trend:")
print(monthly.to_string(index=False))

# Funnel analysis
funnel = df[["add_to_cart_rate_pct","checkout_rate_pct","conv_rate_pct","cart_abandonment_pct"]].mean().round(2)
print(f"\n[KPI 4] Conversion Funnel Averages:")
print(funnel)

# Save
channel.to_csv("reports/channel_scorecard.csv", index=False)
monthly.to_csv("reports/monthly_trend.csv", index=False)

summary = {
    "total_revenue": f"€{total_rev:,.0f}",
    "total_orders": int(total_orders),
    "avg_conv_rate_pct": float(avg_conv),
    "avg_bounce_rate_pct": float(avg_bounce),
    "avg_order_value": float(avg_aov),
    "best_channel": channel.iloc[0]["channel"],
    "avg_cart_abandonment_pct": float(df["cart_abandonment_pct"].mean().round(1)),
}
with open("reports/summary.json","w") as f:
    json.dump(summary, f, indent=2)
print(f"\n[OUTPUT] Reports saved.")
print(json.dumps(summary, indent=2))
