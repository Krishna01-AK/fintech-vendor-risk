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
    st.subheader("All Assessments")
    st.dataframe(df)

    st.subheader("Vendor Trust Score Over Time")

    vendor_list = sorted(df["vendor_name"].unique())
    selected_vendor = st.selectbox("Select a vendor to view history", vendor_list)

    vendor_df = df[df["vendor_name"] == selected_vendor].sort_values("assessed_at")

    if len(vendor_df) < 2:
        st.write(f"Only one assessment on record for {selected_vendor} — need at least two to show a trend.")
        st.dataframe(vendor_df[["assessed_at", "trust_score", "risk_level", "recommendation"]])
    else:
        chart_data = vendor_df.set_index("assessed_at")["trust_score"]
        st.line_chart(chart_data)
        st.dataframe(vendor_df[["assessed_at", "trust_score", "risk_level", "recommendation"]])