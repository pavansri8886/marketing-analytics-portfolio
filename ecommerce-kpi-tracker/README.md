# E-Commerce KPI Tracker

A Python analytics pipeline tracking e-commerce performance across acquisition channels, conversion funnel stages, and revenue trends.

## What It Tracks

- Sessions, bounce rate, pages per session by channel
- Add to cart rate, checkout rate, conversion rate
- Cart abandonment rate
- Revenue, orders, average order value
- Monthly trends and channel scorecards

## Channel Status Classification

- **HIGH PERFORMER** — conversion rate above 3%
- **AVERAGE** — conversion rate 1.5% to 3%
- **NEEDS ATTENTION** — conversion rate below 1.5%

## Tech Stack

Python · pandas · Chart.js · JSON

## How to Run

```bash
pip install pandas numpy
cd src
python generate_data.py
python analysis.py
python dashboard.py
open ../reports/dashboard.html
```

*Built by Pavan Kumar Naganaboina — MSc Data Management & AI, ECE Paris*
