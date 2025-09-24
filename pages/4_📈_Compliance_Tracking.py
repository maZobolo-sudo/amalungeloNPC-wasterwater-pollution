import streamlit as st, pandas as pd, matplotlib.pyplot as plt
from pathlib import Path
st.title("📈 Compliance & Trends")
WORKSPACE = st.secrets.get("workspace_key","default")
p = Path(f"tenants/{WORKSPACE}/reports/ww_compliance_history.csv")
p.parent.mkdir(parents=True, exist_ok=True)
up = st.file_uploader("Upload latest assessed CSV (with non_compliant column)", type=["csv"])
date = st.text_input("Snapshot date (YYYY-MM-DD)")
if up:
    df = pd.read_csv(up)
    rate = float(df.get("non_compliant", pd.Series()).mean())
    row = pd.DataFrame([{"date": date, "non_compliance_rate": rate}])
    if p.exists(): old = pd.read_csv(p); out = pd.concat([old,row], ignore_index=True)
    else: out = row
    out.to_csv(p, index=False); st.success(f"Snapshot appended to {p}")
if p.exists():
    hist = pd.read_csv(p)
    if not hist.empty:
        hist["date"] = pd.to_datetime(hist["date"], errors="coerce")
        hist = hist.sort_values("date")
        fig = plt.figure(figsize=(6,3)); plt.plot(hist["date"], hist["non_compliance_rate"], marker="o")
        plt.ylabel("Non-compliance rate"); st.pyplot(fig); st.dataframe(hist.tail(20))
