import pandas as pd
import re

# Define valid industries
VALID_INDUSTRIES = ["Healthcare", "Technology", "Retail", "Finance", "Education", "Hospitality"]

def detect_issues(df: pd.DataFrame):
    log = []

    # 1. Detect missing values
    missing = df[df.isnull().any(axis=1)]
    if not missing.empty:
        log.append(f"[Missing] Found {len(missing)} rows with missing values.")

    # 2. Detect duplicate rows
    duplicates = df[df.duplicated()]
    if not duplicates.empty:
        log.append(f"[Duplicate] Found {len(duplicates)} duplicate rows.")

    # 3. Detect invalid email addresses
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    invalid_emails = df[~df['email'].astype(str).str.match(email_pattern, na=False)]
    if not invalid_emails.empty:
        log.append(f"[Invalid Email] Found {len(invalid_emails)} rows with malformed emails.")

    # 4. Detect invalid industries
    invalid_industries = df[~df['industry'].isin(VALID_INDUSTRIES)]
    if not invalid_industries.empty:
        log.append(f"[Invalid Industry] Found {len(invalid_industries)} rows with unrecognized industries.")

    # Save log to file
    with open('logs/detection_log.txt', 'w') as f:
        for line in log:
            f.write(line + "\n")

    print("✅ Detection complete. Log written to logs/detection_log.txt")

    # Return dataframes for correction agent
    return {
        "missing": missing,
        "duplicates": duplicates,
        "invalid_emails": invalid_emails,
        "invalid_industries": invalid_industries
    }
