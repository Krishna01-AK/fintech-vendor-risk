import streamlit as st

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

if st.button("Review Answers"):
    st.subheader("Summary")
    st.write(f"**Vendor name:** {vendor_name}")
    st.write(f"**Category:** {vendor_industry}")
    st.write(f"**MFA enforced:** {mfa_enabled}")
    st.write(f"**Recent breach:** {recent_breach}")
    st.write(f"**SOC 2 certified:** {soc2_certified}")
    st.write(f"**Incident response plan:** {incident_response_plan}")