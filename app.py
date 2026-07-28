import streamlit as st
from database import init_db, save_assessment

init_db()

st.title("Fintech Vendor Risk Assessment Tool")
st.write("Enter details about a third-party vendor to assess their risk.")

st.header("Vendor Information")
vendor_name = st.text_input("Vendor name")
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