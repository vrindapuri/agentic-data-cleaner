import streamlit as st
import pandas as pd
from agents.detection_agent import detect_issues
from agents.correction_agent import correct_data
from agents.enrichment_agent import enrich_data

st.title("AGENTIC DATA CLEANER")

uploaded_file = st.file_uploader("Please upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader(" Raw Uploaded Data")
    st.dataframe(df)

    if st.button("Run Cleaning Pipeline"):
        # Step 1: Detection
        detect_issues(df)

        # Step 2: Correction
        cleaned_df = correct_data(df)
        st.subheader("Here is your Cleaned Data!")
        st.dataframe(cleaned_df)

        # Step 3: Enrichment
        enriched_df = enrich_data(cleaned_df)
        st.subheader("Here is your Enriched Final Data!")
        st.dataframe(enriched_df)

        # Save to file
        enriched_df.to_csv("data/final_ui_enriched.csv", index=False)

        # Download button
        st.download_button(
            label="Go ahead, Download Final Enriched CSV!",
            data=enriched_df.to_csv(index=False).encode("utf-8"),
            file_name="final_cleaned_data.csv",
            mime="text/csv",
        )
