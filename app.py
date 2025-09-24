import streamlit as st
from pathlib import Path
st.set_page_config(page_title="💩 Wastewater Pollution Tracker (Green Drop / NWA / NEMA)", layout="wide")
creds = st.secrets.get("credentials", {})
users, pwds, roles, names = (creds.get("usernames",[]), creds.get("passwords",[]),
                             creds.get("roles",[]), creds.get("names",[]))
def login_box():
    st.sidebar.header("Sign in")
    u = st.sidebar.text_input("Username", value=st.session_state.get("user",""))
    p = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Sign in"):
        if u in users:
            i = users.index(u)
            if p == pwds[i]:
                st.session_state["user"]=u; st.session_state["role"]=roles[i]; st.session_state["name"]=names[i]; st.rerun()
        st.sidebar.error("Invalid credentials")
if users and "user" not in st.session_state:
    login_box(); 
    if "user" not in st.session_state: st.stop()
role = st.session_state.get("role","viewer"); name = st.session_state.get("name","Guest")
WORKSPACE = st.secrets.get("workspace_key","default")
ORG = st.secrets.get("org_name","Your Organization")
for sub in ["data","models","reports"]: Path(f"tenants/{WORKSPACE}/{sub}").mkdir(parents=True, exist_ok=True)
st.title("💩 Wastewater Pollution Tracker (Green Drop / NWA / NEMA)")
st.caption(f"{ORG} • Signed in as **{name}** (role: {role}) • Workspace: **{WORKSPACE}**")
st.sidebar.success("Use the pages to navigate →")
