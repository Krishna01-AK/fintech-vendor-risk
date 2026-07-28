# Progress Log

## Current State
Working prototype with three real features: (1) a form to enter vendor 
info and answer security questions, (2) a Trust Score calculation 
(0-100, higher = better) with justified weighting based on breach 
history, MFA, SOC 2 certification, and incident response planning, 
(3) results are saved to a real SQLite database (vendor_risk.db, 
excluded from Git via .gitignore).

## Last Updated
2026-07-28

## Files that exist
- PROGRESS.md — this file
- app.py — main Streamlit app: form, scoring logic, display
- database.py — SQLite setup (init_db) and save function (save_assessment)
- .gitignore — excludes venv/, __pycache__/, .streamlit/, *.db
- venv/ — local virtual environment (not in Git, regenerate locally 
  via `python -m venv venv` if needed)

## Next Step
Build a "View Past Assessments" section: read all rows from 
vendor_risk.db and display them as a table (likely a second page or 
a section below the form). This is the feature that fulfils the core 
idea of the project — tracking a vendor's trust score over multiple 
assessments over time, not just a one-off calculation.

## Decisions Made (don't re-litigate these)
- Python + Streamlit + SQLite stack (beginner-friendly, fast to 
  working prototype)
- Target audience: fintech product/risk management portfolio
- Core idea: vendor risk/trust should be reassessed over time, not 
  scored once at onboarding
- Score is framed as "Trust Score" (100 = best) not "Risk Score" 
  (0 = best) — deliberate UX decision to avoid the misleading 
  intuitive read of a low number looking "good." (Own idea — good 
  catch, keep this reasoning for portfolio writeup.)
- Weighting: recent breach (-40) > no MFA (-25) > no SOC2 (-20) > 
  no incident response plan (-15). Reasoned defaults based on 
  severity, not yet statistically calibrated — flagged as future 
  work using real supply-chain-attack data.
- .db files excluded from Git; only schema/code is version controlled
- PowerShell execution policy set to RemoteSigned (one-time, per 
  machine)

## Open Questions / Blockers
None currently.