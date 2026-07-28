import streamlit as st
import sqlite3
import pandas as pd
from database import init_db, save_assessment

init_db()

def get_existing_vendor_names():
    conn = sqlite3.connect("vendor_risk.db")
    names = pd.read_sql_query(
        "SELECT DISTINCT vendor_name FROM assessments", conn
    )["vendor_name"].tolist()
    conn.close()
    return sorted(names)

st.title("Fintech Vendor Risk Assessment Tool")
st.write(
    "Third-party vendors are often assessed once, at onboarding, and never "
    "revisited — even though their security posture can change over time. "
    "This tool scores a vendor's trustworthiness based on key security "
    "practices, and keeps a history so you can track how that score "
    "changes with each reassessment."
)
st.divider()

st.header("Vendor Information")

existing_vendors = get_existing_vendor_names()
options = ["+ Add new vendor"] + existing_vendors
choice = st.selectbox("Vendor name (type to search existing vendors)", options)

if choice == "+ Add new vendor":
    vendor_name = st.text_input("Enter new vendor name")
else:
    vendor_name = choice

vendor_name = vendor_name.strip()

vendor_industry = st.selectbox(
    "Vendor category",
    ["Payment Processor", "Cloud Infrastructure", "KYC/Identity Verification",
     "Data Analytics", "Open-Source Library / Dependency", "Other"]
)

st.header("Security Practices")
mfa_enabled = st.checkbox("Vendor enforces multi-factor authentication (MFA)")
recent_breach = st.checkbox("Vendor has had a publicly known breach in the last 3 years")
soc2_certified = st.checkbox("Vendor holds a current SOC 2 (or equivalent) certification")
incident_response_plan = st.checkbox("Vendor has a documented incident response plan")

if st.button("Calculate Trust Score"):
    if not vendor_name:
        st.error("Please enter or select a vendor name before submitting.")
    else:
        trust_score = 100
        if recent_breach:
            trust_score -= 40
        if not mfa_enabled:
            trust_score -= 25
        if not soc2_certified:
            trust_score -= 20
        if not incident_response_plan:
            trust_score -= 15
        trust_score = max(trust_score, 0)

        if trust_score >= 80:
            risk_level = "Low Risk"
            recommendation = "Approve"
        elif trust_score >= 50:
            risk_level = "Medium Risk"
            recommendation = "Approve with monitoring"
        elif trust_score >= 25:
            risk_level = "High Risk"
            recommendation = "Requires further investigation"
        else:
            risk_level = "Critical Risk"
            recommendation = "Do not approve / escalate"

        save_assessment(
            vendor_name, vendor_industry, mfa_enabled, recent_breach,
            soc2_certified, incident_response_plan,
            trust_score, risk_level, recommendation
        )

        st.subheader("Trust Assessment Result")
        st.write(f"**Vendor:** {vendor_name} ({vendor_industry})")
        st.metric("Trust Score", f"{trust_score} / 100")
        st.write(f"**Risk Level:** {risk_level}")
        st.write(f"**Recommendation:** {recommendation}")
        st.success("This assessment has been saved.")