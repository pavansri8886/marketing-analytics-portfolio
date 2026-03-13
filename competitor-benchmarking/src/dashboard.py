"""
dashboard.py - Competitor Benchmarking Dashboard
"""
import pandas as pd, json, os

summary   = json.load(open("reports/summary.json"))
pricing   = pd.read_csv("reports/pricing_benchmark.csv")
digital   = pd.read_csv("reports/digital_presence.csv")
ratings   = pd.read_csv("reports/rating_comparison.csv")
cat_comp  = pd.read_csv("reports/category_price_comparison.csv")

def pos_badge(s):
    c = {"IR CHEAPER":"#27ae60","IR PRICIER":"#e74c3c","SIMILAR":"#f39c12"}.get(s,"#aaa")
    return f'<span style="background:{c};color:white;padding:2px 8px;border-radius:10px;font-size:11px;font-weight:bold">{s}</span>'

def tbl(df, badge_col=None):
    rows=""
    for _,r in df.iterrows():
        cells=""
        for col in df.columns:
            v=r[col]
            if col==badge_col: cells+=f"<td>{pos_badge(v)}</td>"
            elif isinstance(v,float): cells+=f"<td>{v:,.2f}</td>"
            else: cells+=f"<td>{v}</td>"
        rows+=f"<tr>{cells}</tr>"
    heads="".join(f"<th>{c.replace('_',' ').title()}</th>" for c in df.columns)
    return f"<table><thead><tr>{heads}</tr></thead><tbody>{rows}</tbody></table>"

brands      = digital["brand"].tolist()
sov_vals    = digital["avg_sov"].tolist()
rating_brands = ratings["brand"].tolist()
rating_vals   = ratings["avg_rating"].tolist()
price_brands  = pricing["brand"].tolist()
price_vals    = pricing["avg_price"].tolist()

html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<title>Competitor Benchmarking Dashboard</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Segoe UI',sans-serif;background:#f0f2f5;color:#222}}
header{{background:#1a1a2e;color:white;padding:24px 36px}}
header h1{{font-size:22px;font-weight:700}}
header p{{font-size:12px;color:#aaa;margin-top:3px}}
.kpi-row{{display:flex;gap:16px;padding:24px 36px 0;flex-wrap:wrap}}
.kpi{{background:white;border-radius:8px;padding:18px 22px;flex:1;min-width:140px;
      box-shadow:0 2px 6px rgba(0,0,0,.07);border-top:4px solid #1a1a2e}}
.kpi .val{{font-size:26px;font-weight:700;color:#1a1a2e}}
.kpi .lbl{{font-size:11px;color:#777;margin-top:3px;text-transform:uppercase;letter-spacing:.5px}}
.section{{background:white;border-radius:8px;margin:20px 36px 0;padding:20px 24px;
          box-shadow:0 2px 6px rgba(0,0,0,.07)}}
.section h2{{font-size:14px;font-weight:700;color:#1a1a2e;margin-bottom:14px;
             padding-left:8px;border-left:4px solid #e94560}}
table{{width:100%;border-collapse:collapse;font-size:12px}}
th{{background:#f8f9fc;text-align:left;padding:9px 10px;color:#555;font-weight:600;border-bottom:2px solid #eee}}
td{{padding:9px 10px;border-bottom:1px solid #f0f0f0}}
tr:hover td{{background:#fafafa}}
.two-col{{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:20px 36px 0}}
.two-col .section{{margin:0}}
.chart-wrap{{height:200px;position:relative}}
footer{{text-align:center;padding:28px;color:#aaa;font-size:11px}}
</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
</head><body>
<header>
  <h1>Competitor Benchmarking Dashboard — Power Tools Market</h1>
  <p>Pricing &middot; Share of Voice &middot; Digital Presence &middot; Customer Ratings</p>
</header>
<div class="kpi-row">
  <div class="kpi"><div class="val">{summary['brands_analysed']}</div><div class="lbl">Brands Analysed</div></div>
  <div class="kpi"><div class="val">{summary['categories_covered']}</div><div class="lbl">Categories</div></div>
  <div class="kpi"><div class="val">€{summary['ir_avg_price']:.0f}</div><div class="lbl">IR Avg Price</div></div>
  <div class="kpi"><div class="val">{summary['ir_avg_rating']}</div><div class="lbl">IR Avg Rating</div></div>
  <div class="kpi"><div class="val">{summary['ir_share_of_voice_pct']}%</div><div class="lbl">IR Share of Voice</div></div>
  <div class="kpi"><div class="val">{summary['top_competitor_by_sov']}</div><div class="lbl">Top Competitor SOV</div></div>
</div>
<div class="two-col">
  <div class="section">
    <h2>Share of Voice by Brand</h2>
    <div class="chart-wrap"><canvas id="sovChart"></canvas></div>
  </div>
  <div class="section">
    <h2>Average Price by Brand</h2>
    <div class="chart-wrap"><canvas id="priceChart"></canvas></div>
  </div>
</div>
<div class="section">
  <h2>Digital Presence &amp; Share of Voice</h2>
  {tbl(digital[["brand","seo_score","avg_organic_k","avg_paid_k","avg_sov","avg_bounce"]])}
</div>
<div class="two-col">
  <div class="section">
    <h2>Customer Rating Comparison</h2>
    {tbl(ratings)}
  </div>
  <div class="section">
    <h2>Pricing &amp; Product Position</h2>
    {tbl(pricing[["brand","avg_price","total_products","avg_discount","avg_stock"]])}
  </div>
</div>
<div class="section">
  <h2>Category Price Comparison vs Ingersoll Rand</h2>
  {tbl(cat_comp[["brand","category","avg_price_eur","ir_price","price_diff_pct","position"]], badge_col="position")}
</div>
<footer>Competitor Benchmarking Dashboard &middot; Python &middot; pandas &middot; Chart.js &middot; Ingersoll Rand Power Tools</footer>
<script>
new Chart(document.getElementById('sovChart'),{{
  type:'bar',
  data:{{
    labels:{brands},
    datasets:[{{label:'Share of Voice %',data:{sov_vals},
      backgroundColor:['rgba(233,69,96,0.85)','rgba(26,26,46,0.75)','rgba(26,26,46,0.6)','rgba(26,26,46,0.5)','rgba(26,26,46,0.4)','rgba(26,26,46,0.3)'],
      borderRadius:4}}]
  }},
  options:{{responsive:true,maintainAspectRatio:false,plugins:{{legend:{{display:false}}}},scales:{{y:{{beginAtZero:true}}}}}}
}});
new Chart(document.getElementById('priceChart'),{{
  type:'bar',
  data:{{
    labels:{price_brands},
    datasets:[{{label:'Avg Price (€)',data:{price_vals},
      backgroundColor:['rgba(233,69,96,0.85)','rgba(26,26,46,0.75)','rgba(26,26,46,0.6)','rgba(26,26,46,0.5)','rgba(26,26,46,0.4)','rgba(26,26,46,0.3)'],
      borderRadius:4}}]
  }},
  options:{{responsive:true,maintainAspectRatio:false,plugins:{{legend:{{display:false}}}},scales:{{y:{{beginAtZero:true}}}}}}
}});
</script>
</body></html>"""

os.makedirs("reports", exist_ok=True)
with open("reports/dashboard.html","w") as f: f.write(html)
print("Dashboard saved.")
