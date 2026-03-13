"""
dashboard.py
Generates interactive HTML dashboard for campaign performance.
"""
import pandas as pd
import json
import os

summary  = json.load(open("reports/summary.json"))
channels = pd.read_csv("reports/channel_performance.csv")
monthly  = pd.read_csv("reports/monthly_trend.csv")
regions  = pd.read_csv("reports/region_performance.csv")
campaigns= pd.read_csv("reports/campaign_performance.csv")

def status_badge(s):
    c = {"STRONG":"#27ae60","AVERAGE":"#f39c12","WEAK":"#e74c3c"}.get(s,"#aaa")
    return f'<span style="background:{c};color:white;padding:2px 10px;border-radius:10px;font-size:11px;font-weight:bold">{s}</span>'

def tbl(df, badge_col=None):
    rows = ""
    for _, r in df.iterrows():
        cells = ""
        for col in df.columns:
            v = r[col]
            if col == badge_col:
                cells += f"<td>{status_badge(v)}</td>"
            elif isinstance(v, float):
                cells += f"<td>{v:,.2f}</td>"
            else:
                cells += f"<td>{v}</td>"
        rows += f"<tr>{cells}</tr>"
    heads = "".join(f"<th>{c.replace('_',' ').title()}</th>" for c in df.columns)
    return f"<table><thead><tr>{heads}</tr></thead><tbody>{rows}</tbody></table>"

m_labels = monthly["month"].tolist()
m_spend  = monthly["spend"].round(0).tolist()
m_roas   = monthly["roas"].tolist()
ch_labels= channels["channel"].tolist()
ch_roas  = channels["roas"].tolist()

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Digital Campaign Performance Dashboard</title>
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{font-family:'Segoe UI',sans-serif;background:#f0f2f5;color:#222}}
  header{{background:#1B3A6B;color:white;padding:24px 36px}}
  header h1{{font-size:22px;font-weight:700}}
  header p{{font-size:12px;color:#aaa;margin-top:3px}}
  .kpi-row{{display:flex;gap:16px;padding:24px 36px 0;flex-wrap:wrap}}
  .kpi{{background:white;border-radius:8px;padding:18px 24px;flex:1;min-width:140px;
        box-shadow:0 2px 6px rgba(0,0,0,.07);border-top:4px solid #1B3A6B}}
  .kpi .val{{font-size:28px;font-weight:700;color:#1B3A6B}}
  .kpi .lbl{{font-size:11px;color:#777;margin-top:3px;text-transform:uppercase;letter-spacing:.5px}}
  .section{{background:white;border-radius:8px;margin:20px 36px 0;padding:20px 24px;
            box-shadow:0 2px 6px rgba(0,0,0,.07)}}
  .section h2{{font-size:14px;font-weight:700;color:#1B3A6B;margin-bottom:14px;
               padding-left:8px;border-left:4px solid #0EA5E9}}
  table{{width:100%;border-collapse:collapse;font-size:12px}}
  th{{background:#f8f9fc;text-align:left;padding:9px 10px;color:#555;
      font-weight:600;border-bottom:2px solid #eee}}
  td{{padding:9px 10px;border-bottom:1px solid #f0f0f0}}
  tr:hover td{{background:#fafbff}}
  .two-col{{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:20px 36px 0}}
  .two-col .section{{margin:0}}
  .chart-wrap{{height:200px;position:relative}}
  footer{{text-align:center;padding:28px;color:#aaa;font-size:11px}}
</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
</head>
<body>
<header>
  <h1>Digital Campaign Performance Dashboard</h1>
  <p>Performance &amp; Digital Marketing Analytics  |  FY 2024</p>
</header>
<div class="kpi-row">
  <div class="kpi"><div class="val">{summary['total_spend']}</div><div class="lbl">Total Spend</div></div>
  <div class="kpi"><div class="val">{summary['total_revenue']}</div><div class="lbl">Total Revenue</div></div>
  <div class="kpi"><div class="val">{summary['overall_roas']}x</div><div class="lbl">Overall ROAS</div></div>
  <div class="kpi"><div class="val">{summary['overall_ctr_pct']}%</div><div class="lbl">Overall CTR</div></div>
  <div class="kpi"><div class="val">{summary['total_conversions']:,}</div><div class="lbl">Total Conversions</div></div>
</div>
<div class="two-col">
  <div class="section">
    <h2>Monthly Spend &amp; ROAS Trend</h2>
    <div class="chart-wrap"><canvas id="monthlyChart"></canvas></div>
  </div>
  <div class="section">
    <h2>ROAS by Channel</h2>
    <div class="chart-wrap"><canvas id="channelChart"></canvas></div>
  </div>
</div>
<div class="section">
  <h2>Channel Performance Scorecard</h2>
  {tbl(channels[["channel","total_spend","total_revenue","roas","ctr_pct","cpa","status"]], badge_col="status")}
</div>
<div class="two-col">
  <div class="section">
    <h2>Region Performance</h2>
    {tbl(regions)}
  </div>
  <div class="section">
    <h2>Campaign Performance</h2>
    {tbl(campaigns)}
  </div>
</div>
<footer>Digital Campaign Performance Dashboard &middot; Built with Python &middot; pandas &middot; Chart.js</footer>
<script>
new Chart(document.getElementById('monthlyChart'),{{
  type:'bar',
  data:{{
    labels:{m_labels},
    datasets:[
      {{label:'Spend (€)',data:{m_spend},backgroundColor:'rgba(27,58,107,0.75)',borderRadius:4,yAxisID:'y'}},
      {{label:'ROAS',data:{m_roas},type:'line',borderColor:'#0EA5E9',tension:0.4,fill:false,yAxisID:'y1'}}
    ]
  }},
  options:{{responsive:true,maintainAspectRatio:false,
    scales:{{y:{{beginAtZero:true}},y1:{{position:'right',min:0,grid:{{drawOnChartArea:false}}}}}}
  }}
}});
new Chart(document.getElementById('channelChart'),{{
  type:'bar',
  data:{{
    labels:{ch_labels},
    datasets:[{{label:'ROAS',data:{ch_roas},backgroundColor:['rgba(27,58,107,0.8)','rgba(14,165,233,0.8)','rgba(39,174,96,0.8)','rgba(243,156,18,0.8)'],borderRadius:4}}]
  }},
  options:{{responsive:true,maintainAspectRatio:false,plugins:{{legend:{{display:false}}}},scales:{{y:{{beginAtZero:true}}}}}}
}});
</script>
</body></html>"""

os.makedirs("reports", exist_ok=True)
with open("reports/dashboard.html","w") as f:
    f.write(html)
print("Dashboard saved.")
