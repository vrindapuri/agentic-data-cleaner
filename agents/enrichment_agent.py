import os
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-pro")


# Rename this line ⬇️
def enrich_data(df: pd.DataFrame):

    log = []

    def call_gemini(row):
        prompt = f"""
        A customer record is missing some fields. Fill in the missing fields based on available ones.

        customer_id: {row.get('customer_id')}
        name: {row.get('name')}
        email: {row.get('email')}
        industry: {row.get('industry')}
        spend: {row.get('spend')}

        Return a Python dictionary with:
        {{
          "name": (if missing),
          "industry": (if missing),
          "spend": (if missing)
        }}
        """
        try:
            response = model.generate_content(prompt)
            return eval(response.text)
        except Exception as e:
            log.append(f"[Gemini Error] {str(e)}")
            return {"name": None, "industry": None, "spend": None}

    # Enrich each row
    for index, row in df.iterrows():
        if pd.isnull(row["name"]) or pd.isnull(row["industry"]) or pd.isnull(row["spend"]):
            guesses = call_gemini(row)
            for field in ["name", "industry", "spend"]:
                if pd.isnull(row[field]) and guesses.get(field):
                    df.at[index, field] = guesses[field]
                    log.append(f"[Enriched] Row {index} — filled {field} with {guesses[field]}")

    df.to_csv("data/final_enriched.csv", index=False)
    log.append("[Save] Enriched data saved to data/final_enriched.csv")

    with open("logs/enrichment_log.txt", "w") as f:
        for entry in log:
            f.write(entry + "\n")

    print("✅ Enrichment complete. Log written to logs/enrichment_log.txt")
    return df
