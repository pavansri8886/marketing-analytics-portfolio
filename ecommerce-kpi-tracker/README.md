# E-Commerce KPI Tracker

Most e-commerce dashboards show you traffic and revenue. This one shows you where you are losing customers — and at which stage of the funnel.

I built this to answer a specific question: if conversion rate drops this week, is it because fewer people are adding to cart, or because people are abandoning at checkout? The answer changes what you do about it.

---

## The Problem It Solves

A drop in revenue could mean dozens of different things. Traffic fell. Bounce rate spiked. Add-to-cart rate is fine but checkout completion dropped. Average order value declined. Each of these has a different fix, and without a proper funnel breakdown you are guessing.

This tracker breaks the funnel into stages and attributes performance by acquisition channel so you know exactly where the leak is.

---

## What I Built

A Python pipeline that tracks the full e-commerce conversion funnel across 5 acquisition channels — from sessions to add-to-cart to checkout to purchase — and surfaces channel-level performance with status classification.

**Channels:** Organic Search · Paid Search · Email · Social Media · Direct

**Funnel stages tracked:**
- Sessions and bounce rate
- Add-to-cart rate
- Checkout rate
- Conversion rate
- Cart abandonment rate
- Average order value

---

## Sample Output

```
Overall Performance (FY 2024)
─────────────────────────────
Total Revenue:       €93,863,172
Total Orders:        427,783
Avg Conversion Rate: 5.8%
Avg Bounce Rate:     47.6%
Avg Order Value:     €216.50
Cart Abandonment:    60.6%

Conversion Funnel Averages:
Add to Cart Rate:    14.8%
Checkout Rate:        8.9%
Conversion Rate:      5.8%
Cart Abandonment:    60.6%

Channel Status:
All 5 channels classified as HIGH PERFORMER (conv rate > 3%)
Best channel by revenue: Social Media
```

---

## Project Structure

```
ecommerce-kpi-tracker/
├── data/
│   └── ecommerce_data.csv       # 1,825 daily channel records
├── src/
│   ├── generate_data.py         # Data generation
│   ├── analysis.py              # Funnel analysis and channel scoring
│   └── dashboard.py             # HTML dashboard builder
├── reports/
│   ├── dashboard.html           # Interactive dashboard
│   ├── channel_scorecard.csv
│   ├── monthly_trend.csv
│   └── summary.json
└── README.md
```

---

## How to Run

```bash
pip install pandas numpy
cd src
python generate_data.py
python analysis.py
python dashboard.py
open ../reports/dashboard.html
```

---

## Channel Classification Logic

| Status | Conversion Rate Threshold |
|---|---|
| HIGH PERFORMER | Above 3% |
| AVERAGE | 1.5% to 3% |
| NEEDS ATTENTION | Below 1.5% |

---

## What I Would Add Next

- Cohort analysis — track repeat purchase rate by acquisition channel
- A/B test result tracker for checkout flow experiments
- Product category breakdown — which SKUs drive the most abandoned carts
- Integration with Shopify or WooCommerce API for live data

---

## Tech Stack

`Python 3.11` · `pandas` · `Chart.js 4.4` · `JSON`

---

*Pavan Kumar Naganaboina — MSc Data Management & AI, ECE Paris 2025–2026*
