import streamlit as st, pandas as pd
st.title("🏁 Overview")
st.write("Upload discharge monitoring data and assess **compliance** with simplified limits (demo).")
st.table(pd.DataFrame({
 "column":["date","plant","pH","BOD_mg_L","COD_mg_L","NH3_mg_L","Ecoli_cfu_100ml","PO4_mg_L","TSS_mg_L"],
 "desc":["date","plant name","5.5–9.5","≤25","≤75","≤1","≤1000","≤1","≤25"]
}))
