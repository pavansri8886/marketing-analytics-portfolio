# Digital Campaign Performance Dashboard

Tracking €25M+ in annual ad spend across SEA, Display, Social Ads, and Email to identify which channels actually deliver returns — and which ones are burning budget.

I built this after realising that most marketing teams I observed were optimising campaigns based on CTR alone, without connecting spend to actual conversions and revenue. This pipeline builds the full picture.

---

## The Problem It Solves

Campaign managers often have data scattered across platform dashboards — Google Ads in one tab, Meta Ads in another, email reports in a CSV. There is no single view of which channel has the best ROAS this month vs last month, where cost per acquisition is creeping up, or whether a dip in revenue came from lower traffic or lower conversion rate.

This pipeline consolidates everything into one automated report.

---

## What I Built

A Python pipeline that ingests daily campaign data across 4 channels and 5 regions, computes KPIs, classifies channel health, and renders an interactive HTML dashboard — no BI tool required.

**Channels:** SEA · Display · Social Ads · Email  
**Regions:** France · Germany · UK · Spain · Italy

**KPIs computed:**
- ROAS (Return on Ad Spend)
- CTR (Click-Through Rate)
- CPC (Cost Per Click)
- CPA (Cost Per Acquisition)
- Conversion Rate
- Monthly spend and revenue trends

---

## Sample Output

```
Overall Performance (FY 2024)
─────────────────────────────
Total Spend:       €25,687,615
Total Revenue:     €108,244,620
Overall ROAS:      4.21x
Overall CTR:       4.48%
Total Conversions: 479,591

Channel Scorecard:
Channel      ROAS    CTR %   CPA (€)   Status
SEA          4.24    4.44    53.18     STRONG
Email        4.21    4.50    53.52     STRONG
Display      4.20    4.50    54.30     STRONG
Social Ads   4.20    4.50    53.26     STRONG

Best Region by ROAS: UK (4.37x)
```

---

## Project Structure

```
digital-campaign-dashboard/
├── data/
│   └── campaign_data.csv        # 7,300 daily records
├── src/
│   ├── generate_data.py         # Data generation (swap with real API feed)
│   ├── analysis.py              # KPI computation and classification
│   └── dashboard.py             # HTML report builder
├── reports/
│   ├── dashboard.html           # Interactive dashboard (open in browser)
│   ├── channel_performance.csv
│   ├── monthly_trend.csv
│   ├── region_performance.csv
│   ├── campaign_performance.csv
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

## What I Would Add Next

- Connect to Google Ads API and Meta Ads API for live data ingestion
- Week-over-week change indicators on the KPI header
- Budget pacing tracker — spend rate vs planned monthly budget
- Anomaly detection on daily CTR drops using rolling average comparison

---

## Tech Stack

`Python 3.11` · `pandas` · `Chart.js 4.4` · `JSON`

---

*Pavan Kumar Naganaboina — MSc Data Management & AI, ECE Paris 2025–2026*
