# Digital Campaign Performance Dashboard

An end-to-end analytics pipeline for tracking and optimising digital marketing campaign performance across channels, regions, and time periods.

Built to demonstrate performance marketing analytics skills — KPI tracking, ROAS analysis, channel benchmarking, and dashboard reporting relevant to digital marketing analyst roles.

---

## What It Does

Tracks and analyses digital campaign performance across four channels (SEA, Display, Social Ads, Email) and five regions (France, Germany, UK, Spain, Italy) over a full year.

Computes the following KPIs:
- **ROAS** (Return on Ad Spend)
- **CTR** (Click-Through Rate)
- **CPC** (Cost Per Click)
- **CPA** (Cost Per Acquisition)
- **Conversion Rate**
- Monthly spend and revenue trends
- Channel and region performance scorecard with STRONG / AVERAGE / WEAK classification

---

## Project Structure

```
digital-campaign-dashboard/
├── data/
│   └── campaign_data.csv        # 7,300 daily campaign records
├── src/
│   ├── generate_data.py         # Synthetic data generation
│   ├── analysis.py              # KPI computation pipeline
│   └── dashboard.py             # HTML dashboard generator
├── reports/
│   ├── dashboard.html           # Interactive performance dashboard
│   ├── channel_performance.csv
│   ├── monthly_trend.csv
│   ├── region_performance.csv
│   ├── campaign_performance.csv
│   └── summary.json
└── README.md
```

---

## Tech Stack

Python · pandas · SQL-style analytics · Chart.js · JSON

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

*Built by Pavan Kumar Naganaboina — MSc Data Management & AI, ECE Paris*
