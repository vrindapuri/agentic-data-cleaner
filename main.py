import pandas as pd
from agents.detection_agent import detect_issues
from agents.correction_agent import correct_data

# Load raw data
df = pd.read_csv('data/input_messy.csv')

# Run detection
issues = detect_issues(df)

# Run correction
cleaned_df = correct_data(df)

print("\n✅ Cleaned Data Preview:")
print(cleaned_df.head())

print("\nCheck 'logs/correction_log.txt' for what was fixed.")
from agents.enrichment_agent import enrich_with_llm

# Enrich with Gemini
enriched_df = enrich_with_llm(cleaned_df)

print("\n✅ Enriched Data Preview:")
print(enriched_df.head())
