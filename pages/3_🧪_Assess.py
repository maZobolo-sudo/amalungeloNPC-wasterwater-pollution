import streamlit as st, pandas as pd, matplotlib.pyplot as plt
from pathlib import Path
from src.eval import assess
st.title("🧪 Compliance Assessment")
WORKSPACE = st.secrets.get("workspace_key","default")
p = Path(f"tenants/{WORKSPACE}/data/discharge.csv")
if not p.exists(): st.warning("No data found. Use Data Intake."); st.stop()
df = pd.read_csv(p)
out = assess(df); st.dataframe(out.head())
rate = out["non_compliant"].mean() if "non_compliant" in out else 0
st.metric("Non-compliance rate", f"{rate:.0%}")
fig = plt.figure(figsize=(6,3))
(out.groupby("plant")["non_compliant"].mean()*100).plot(kind="bar")
plt.ylabel("% samples non-compliant"); st.pyplot(fig)
csv = out.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download assessed CSV", csv, "assessed_discharge.csv", "text/csv")
