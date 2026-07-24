# Progress Log

## Current State
Full dev environment working end-to-end: Python, VS Code, Git, GitHub 
repo all connected. Streamlit installed and confirmed working with a 
minimal "hello world" app (app.py) that runs locally and shows in 
browser.

## Last Updated
2026-07-24

## Files that exist
- PROGRESS.md — this file
- app.py — minimal Streamlit test ("Fintech Vendor Risk Tool" title, 
  confirms setup works). Not yet the real app.
- venv/ — virtual environment folder (not pushed to GitHub, see note 
  below)

## Next Step
Build the first real feature: a Streamlit form where a user enters 
vendor details (name, industry, etc.) and answers a short set of 
security questions. No scoring logic yet — just capture the inputs 
and display them back, to prove the form works before adding 
calculation logic.

## Decisions Made (don't re-litigate these)
- Using Python + Streamlit + SQLite (beginner-friendly, fast to a 
  working prototype, everything learned is reusable Python)
- Target audience: fintech product/risk management portfolio, not 
  pure software engineering
- Core idea: vendor risk score should be re-assessed over time, not 
  scored once at onboarding
- PowerShell execution policy set to RemoteSigned to allow venv 
  activation (needed once per machine)

## Open Questions / Blockers
- Need to add a .gitignore so the venv/ folder never gets committed 
  (it's large, machine-specific, and shouldn't be in version control 
  — every collaborator/future-you regenerates their own venv locally)
- Haven't yet decided the exact list of security questions / scoring 
  weights — need to research a real framework (e.g. NIST CSF, Shared 
  Assessments SIG) before finalizing this