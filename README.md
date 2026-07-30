# Fintech Vendor Risk Assessment Tool

A working prototype that scores and tracks the security risk of 
third-party vendors used by fintech companies — built to replace the 
common "assess once at onboarding and never again" approach with an 
ongoing, trackable trust score.

## The Problem

Fintech companies rely heavily on third-party vendors — payment 
processors, cloud infrastructure, KYC providers, open-source 
libraries. These vendors are typically assessed once, during 
onboarding, using a static questionnaire. But a vendor's security 
posture isn't static — it can weaken over time (a new breach, an 
expired certification) or improve. Most vendor risk processes have no 
built-in way to notice that change.

## What This Tool Does

- Captures key security signals about a vendor (MFA usage, breach 
  history, SOC 2 certification, incident response planning)
- Calculates a **Trust Score** (0–100, higher = more trustworthy) 
  using explicit, justified weights based on the severity of each 
  factor — not an arbitrary scale
- Saves every assessment permanently, rather than overwriting the 
  previous one
- Lets you view a vendor's trust score **over time**, across multiple 
  assessments, as a trend chart — the core idea the project is built 
  around

## Scoring Methodology

Starting from a baseline of 100, points are deducted based on:

| Factor | Penalty | Reasoning |
|---|---|---|
| Recent known breach | -40 | Demonstrated past failure, the strongest risk signal |
| No MFA enforced | -25 | Foundational access control; its absence is a structural weakness |
| No SOC 2 certification | -20 | No independent verification of controls exists |
| No incident response plan | -15 | Affects response to incidents, not likelihood of one occurring |

**Known limitation:** these weights are reasoned defaults based on 
relative severity, not statistically calibrated against real attack 
outcome data. A natural next step would be validating (or adjusting) 
these weights against a real supply-chain-attack dataset.

## Tech Stack

- **Python** — core logic
- **Streamlit** — web interface (chosen for fast iteration to a 
  working prototype)
- **SQLite** — lightweight persistent storage
- **pandas** — data handling and filtering

## Running Locally
git clone https://github.com/Krishna01-AK/fintech-vendor-risk.git
cd fintech-vendor-risk
python -m venv venv
venv\Scripts\activate
pip install streamlit pandas
streamlit run app.py

## Project Background

This project began as a rebuild of a weak academic project — the 
original included only static UI mockups with no working logic behind 
them. This version replaces that with a fully functional prototype: 
real scoring logic, real persistent storage, and a genuine 
demonstration of the core idea (risk changes over time) using actual 
saved data.