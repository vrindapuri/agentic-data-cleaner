import pandas as pd
from fuzzywuzzy import process

VALID_INDUSTRIES = ["Healthcare", "Technology", "Retail", "Finance", "Education", "Hospitality"]

def correct_data(df: pd.DataFrame):
    log = []

    # 1. Remove duplicate rows
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    removed = before - after
    if removed > 0:
        log.append(f"[Duplicate Removal] Removed {removed} duplicate rows.")

    # 2. Standardize industries using fuzzy matching
    def correct_industry(industry):
        if pd.isna(industry):
            return industry
        match, score = process.extractOne(industry, VALID_INDUSTRIES)
        return match if score >= 80 else industry  # only correct if confident

    df['industry'] = df['industry'].astype(str).str.strip()
    df['industry'] = df['industry'].apply(correct_industry)
    log.append(f"[Industry Fix] Applied fuzzy matching to 'industry' column.")

    # 3. Clean emails (strip whitespace, lowercase)
    df['email'] = df['email'].astype(str).str.strip().str.lower()

    # 4. Save cleaned output
    df.to_csv("data/output_clean.csv", index=False)
    log.append("[Save] Cleaned data saved to data/output_clean.csv")

    # 5. Save correction log
    with open("logs/correction_log.txt", "w") as f:
        for line in log:
            f.write(line + "\n")

    print("✅ Correction complete. Log written to logs/correction_log.txt")
    return df
