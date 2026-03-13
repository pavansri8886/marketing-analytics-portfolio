# Competitor Benchmarking Analysis — Power Tools Market

Before you can optimise your own marketing, you need to know where you stand. This project maps Ingersoll Rand's pricing, digital presence, and share of voice against five major competitors across five product categories.

The goal was not just to collect data — it was to produce actionable findings: where is Ingersoll Rand priced higher than the market? Where are competitors outranking us on organic search? Which categories are we losing share of voice in?

---

## The Problem It Solves

Without a structured benchmarking framework, competitor analysis is just browsing websites and guessing. This pipeline produces repeatable, comparable outputs — the same KPIs measured the same way for every brand, every month.

---

## What I Built

A Python pipeline that benchmarks 6 brands across 5 product categories on pricing, customer ratings, SEO visibility, share of voice, and organic vs paid traffic split — with category-level price positioning relative to Ingersoll Rand.

**Brands analysed:** Ingersoll Rand · Bosch Professional · Makita · DeWalt · Milwaukee · Metabo

**Categories:** Impact Wrenches · Drills · Grinders · Compressors · Ratchets

---

## Sample Output

```
Ingersoll Rand Position Summary
─────────────────────────────────
Avg Price:          €315.85  (3rd highest of 6 brands)
Avg Rating:         4.20     (lowest of 6 brands — improvement opportunity)
Share of Voice:     18.29%
Top Competitor SOV: DeWalt (19.08%)

Digital Presence:
IR ranks 4th out of 6 on share of voice
IR is the only brand with 100% paid search presence
IR has lowest SEO visibility score (53.38 vs DeWalt 68.32)

Category Pricing vs Competitors (selected):
Compressors — IR is cheapest across all 5 competitors
Impact Wrenches — IR is priced higher than DeWalt by 166%
Ratchets — IR is priced higher than Makita by 271%
```

---

## Key Finding

Ingersoll Rand's customer rating (4.20) is the lowest of all 6 brands benchmarked. Every competitor scores above 4.30. This is the clearest opportunity for a marketing and product team to investigate — is it a product issue, a review volume issue, or a customer satisfaction issue?

---

## Project Structure

```
competitor-benchmarking/
├── data/
│   ├── product_benchmarks.csv   # 30 brand-category records
│   └── traffic_benchmarks.csv   # 72 monthly traffic records
├── src/
│   ├── generate_data.py         # Data generation
│   ├── analysis.py              # Benchmarking pipeline
│   └── dashboard.py             # HTML dashboard builder
├── reports/
│   ├── dashboard.html           # Interactive dashboard
│   ├── pricing_benchmark.csv
│   ├── digital_presence.csv
│   ├── category_price_comparison.csv
│   ├── rating_comparison.csv
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

## Price Positioning Classification

| Label | Meaning |
|---|---|
| IR CHEAPER | Competitor price is more than 2% above IR |
| IR PRICIER | Competitor price is more than 2% below IR |
| SIMILAR | Within 2% of IR price |

---

## What I Would Add Next

- Web scraping layer to pull real pricing from retailer sites weekly
- Google Trends integration for search demand share by brand
- Social sentiment analysis using Twitter/Reddit mentions
- Automated monthly report email with delta vs prior month

---

## Tech Stack

`Python 3.11` · `pandas` · `Chart.js 4.4` · `JSON`

---

*Pavan Kumar Naganaboina — MSc Data Management & AI, ECE Paris 2025–2026*
