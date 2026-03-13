"""
dashboard.py - E-commerce KPI Tracker HTML Dashboard
"""
import pandas as pd, json, os

summary = json.load(open("reports/summary.json"))
channel = pd.read_csv("reports/channel_scorecard.csv")
monthly = pd.read_csv("reports/monthly_trend.csv")

def badge(s):
    c={"HIGH PERFORMER":"#27ae60","AVERAGE":"#f39c12","NEEDS ATTENTION":"#e74c3c"}.get(s,"#aaa")
    return f'<span style="background:{c};color:white;padding:2px 8px;border-radius:10px;font-size:11px;font-weight:bold">{s}</span>'

def tbl(df, badge_col=None):
    rows=""
    for _,r in df.iterrows():
        cells=""
        for col in df.columns:
            v=r[col]
            if col==badge_col: cells+=f"<td>{badge(v)}</td>"
            elif isinstance(v,float): cells+=f"<td>{v:,.2f}</td>"
            else: cells+=f"<td>{v}</td>"
        rows+=f"<tr>{cells}</tr>"
    heads="".join(f"<th>{c.replace('_',' ').title()}</th>" for c in df.columns)
    return f"<table><thead><tr>{heads}</tr></thead><tbody>{rows}</tbody></table>"

m_labels=monthly["month"].tolist()
m_rev=monthly["revenue"].round(0).tolist()
m_conv=monthly["avg_conv"].tolist()

html=f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<title>E-Commerce KPI Tracker</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Segoe UI',sans-serif;background:#f0f2f5;color:#222}}
header{{background:#0F4C75;color:white;padding:24px 36px}}
header h1{{font-size:22px;font-weight:700}}
header p{{font-size:12px;color:#aaa;margin-top:3px}}
.kpi-row{{display:flex;gap:16px;padding:24px 36px 0;flex-wrap:wrap}}
.kpi{{background:white;border-radius:8px;padding:18px 22px;flex:1;min-width:130px;
      box-shadow:0 2px 6px rgba(0,0,0,.07);border-top:4px solid #0F4C75}}
.kpi .val{{font-size:26px;font-weight:700;color:#0F4C75}}
.kpi .lbl{{font-size:11px;color:#777;margin-top:3px;text-transform:uppercase;letter-spacing:.5px}}
.section{{background:white;border-radius:8px;margin:20px 36px 0;padding:20px 24px;
          box-shadow:0 2px 6px rgba(0,0,0,.07)}}
.section h2{{font-size:14px;font-weight:700;color:#0F4C75;margin-bottom:14px;
             padding-left:8px;border-left:4px solid #1B98E0}}
table{{width:100%;border-collapse:collapse;font-size:12px}}
th{{background:#f8f9fc;text-align:left;padding:9px 10px;color:#555;font-weight:600;border-bottom:2px solid #eee}}
td{{padding:9px 10px;border-bottom:1px solid #f0f0f0}}
tr:hover td{{background:#f7faff}}
.chart-wrap{{height:210px;position:relative}}
footer{{text-align:center;padding:28px;color:#aaa;font-size:11px}}
</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
</head><body>
<header>
  <h1>E-Commerce KPI Tracker</h1>
  <p>Conversion Funnel &middot; Channel Performance &middot; Revenue Analytics  |  FY 2024</p>
</header>
<div class="kpi-row">
  <div class="kpi"><div class="val">{summary['total_revenue']}</div><div class="lbl">Total Revenue</div></div>
  <div class="kpi"><div class="val">{summary['total_orders']:,}</div><div class="lbl">Total Orders</div></div>
  <div class="kpi"><div class="val">{summary['avg_conv_rate_pct']}%</div><div class="lbl">Avg Conv Rate</div></div>
  <div class="kpi"><div class="val">{summary['avg_bounce_rate_pct']}%</div><div class="lbl">Avg Bounce Rate</div></div>
  <div class="kpi"><div class="val">€{summary['avg_order_value']}</div><div class="lbl">Avg Order Value</div></div>
  <div class="kpi"><div class="val">{summary['avg_cart_abandonment_pct']}%</div><div class="lbl">Cart Abandonment</div></div>
</div>
<div class="section">
  <h2>Monthly Revenue &amp; Conversion Rate Trend</h2>
  <div class="chart-wrap"><canvas id="monthlyChart"></canvas></div>
</div>
<div class="section">
  <h2>Channel Performance Scorecard</h2>
  {tbl(channel[["channel","total_sessions","total_revenue","avg_conv_rate","avg_bounce","avg_cart_abandon","status"]], badge_col="status")}
</div>
<footer>E-Commerce KPI Tracker &middot; Python &middot; pandas &middot; Chart.js</footer>
<script>
new Chart(document.getElementById('monthlyChart'),{{
  type:'bar',
  data:{{
    labels:{m_labels},
    datasets:[
      {{label:'Revenue (€)',data:{m_rev},backgroundColor:'rgba(15,76,117,0.75)',borderRadius:4,yAxisID:'y'}},
      {{label:'Conv Rate %',data:{m_conv},type:'line',borderColor:'#1B98E0',tension:0.4,fill:false,yAxisID:'y1'}}
    ]
  }},
  options:{{responsive:true,maintainAspectRatio:false,
    scales:{{y:{{beginAtZero:true}},y1:{{position:'right',min:0,grid:{{drawOnChartArea:false}}}}}}
  }}
}});
</script>
</body></html>"""

os.makedirs("reports",exist_ok=True)
with open("reports/dashboard.html","w") as f: f.write(html)
print("Dashboard saved.")
