import sqlite3
from datetime import datetime

DB_NAME = "vendor_risk.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assessments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vendor_name TEXT NOT NULL,
            vendor_category TEXT NOT NULL,
            mfa_enabled INTEGER,
            recent_breach INTEGER,
            soc2_certified INTEGER,
            incident_response_plan INTEGER,
            trust_score INTEGER,
            risk_level TEXT,
            recommendation TEXT,
            assessed_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_assessment(vendor_name, vendor_category, mfa_enabled, recent_breach,
                     soc2_certified, incident_response_plan,
                     trust_score, risk_level, recommendation):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO assessments (
            vendor_name, vendor_category, mfa_enabled, recent_breach,
            soc2_certified, incident_response_plan,
            trust_score, risk_level, recommendation, assessed_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        vendor_name, vendor_category, int(mfa_enabled), int(recent_breach),
        int(soc2_certified), int(incident_response_plan),
        trust_score, risk_level, recommendation,
        datetime.now().isoformat()
    ))
    conn.commit()
    conn.close()