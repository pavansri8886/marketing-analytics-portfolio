# Competitor Benchmarking Analysis — Power Tools Market

A Python pipeline that benchmarks Ingersoll Rand against five major power tools competitors across pricing, digital presence, share of voice, customer ratings, and category-level positioning.

## What It Analyses

- Average pricing per brand and category vs Ingersoll Rand
- Share of voice and organic vs paid traffic split
- SEO visibility score and bounce rate comparison
- Customer rating and review volume per brand
- Category-level price positioning: IR CHEAPER / SIMILAR / IR PRICIER

## Competitors Covered

Ingersoll Rand · Bosch Professional · Makita · DeWalt · Milwaukee · Metabo

## Categories Covered

Impact Wrenches · Drills · Grinders · Compressors · Ratchets

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
