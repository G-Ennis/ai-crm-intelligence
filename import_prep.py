import pandas as pd
import re
from pathlib import Path

def load_excel(file_path):
    try:
        df = pd.read_excel(file_path)

        print("\nExcel file loaded successfully!")
        print(f"Total rows: {len(df)}")
        print(f"Total columns: {len(df.columns)}")

        return df

    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None

def clean_column_names(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    print("\nColumn names standardized.")

    return df

def extract_email_domains(df):

    if "email" not in df.columns:
        print("\nNo email column found. Skipping domain extraction.")
        return df

    df["email_domain"] = (
        df["email"]
        .astype(str)
        .str.strip()
        .str.extract(r'@([^@\s]+)', expand=False)
        .str.lower()
    )

    print("\nEmail domains extracted successfully.")

    return df     

def detect_missing_data(df):

    missing = df.isnull().sum()

    print("\n--- MISSING DATA REPORT ---")

    for column, count in missing.items():
        if count > 0:
            print(f"{column}: {count} missing values")

    if missing.sum() == 0:
        print("No missing information detected!")

    return df        

def export_to_csv(df, output_path):

    try:
        df.to_csv(output_path, index=False, encoding="utf-8-sig")

        print("\nCSV export completed successfully!")
        print(f"Saved file: {output_path}")

    except Exception as e:
        print(f"Error exporting CSV: {e}")

def process_file(input_path, output_path):

    print("\n=== CRM IMPORT PREPARATION TOOL ===")

    df = load_excel(input_path)

    if df is None:
        return

    df = clean_column_names(df)

    df = extract_email_domains(df)

    df = detect_missing_data(df)

    export_to_csv(df, output_path)

    print("\n=== PROCESSING COMPLETE ===")     


if __name__ == "__main__":

    input_file = input("Enter Excel file path: ")

    output_file = input("Enter output CSV filename: ")

    process_file(input_file, output_file)