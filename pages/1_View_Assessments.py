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
    display_df = df.copy()
    yes_no_columns = ["mfa_enabled", "recent_breach", "soc2_certified", "incident_response_plan"]
    for col in yes_no_columns:
        display_df[col] = display_df[col].map({1: "Yes", 0: "No"})

    display_df = display_df.rename(columns={
        "vendor_name": "Vendor",
        "vendor_category": "Category",
        "mfa_enabled": "MFA Enabled",
        "recent_breach": "Recent Breach",
        "soc2_certified": "SOC 2 Certified",
        "incident_response_plan": "IR Plan",
        "trust_score": "Trust Score",
        "risk_level": "Risk Level",
        "recommendation": "Recommendation",
        "assessed_at": "Assessed At"
    })

    st.subheader("All Assessments")
    st.dataframe(
        display_df[["Vendor", "Category", "MFA Enabled", "Recent Breach",
                     "SOC 2 Certified", "IR Plan", "Trust Score",
                     "Risk Level", "Recommendation", "Assessed At"]],
        hide_index=True
    )

    st.subheader("Vendor Trust Score Over Time")

    vendor_list = sorted(df["vendor_name"].unique())
    selected_vendor = st.selectbox("Select a vendor to view history", vendor_list)

    vendor_df = df[df["vendor_name"] == selected_vendor].sort_values("assessed_at")

    if len(vendor_df) < 2:
        st.write(f"Only one assessment on record for {selected_vendor} — need at least two to show a trend.")
        st.dataframe(
            vendor_df[["assessed_at", "trust_score", "risk_level", "recommendation"]]
            .rename(columns={"assessed_at": "Assessed At", "trust_score": "Trust Score",
                              "risk_level": "Risk Level", "recommendation": "Recommendation"}),
            hide_index=True
        )
    else:
        chart_data = vendor_df.set_index("assessed_at")["trust_score"]
        st.line_chart(chart_data)
        st.dataframe(
            vendor_df[["assessed_at", "trust_score", "risk_level", "recommendation"]]
            .rename(columns={"assessed_at": "Assessed At", "trust_score": "Trust Score",
                              "risk_level": "Risk Level", "recommendation": "Recommendation"}),
            hide_index=True
        )