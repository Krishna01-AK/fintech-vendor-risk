import streamlit as st
import sqlite3
import pandas as pd

st.title("Past Vendor Assessments")

conn = sqlite3.connect("vendor_risk.db")
df = pd.read_sql_query("SELECT * FROM assessments ORDER BY assessed_at DESC", conn)
conn.close()

if df.empty:
    st.info("No assessments yet. Go to the main page to assess a vendor.")
else:
    st.dataframe(df)