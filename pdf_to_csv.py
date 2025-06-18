import pdfplumber
import pandas as pd
import sys
import os

def pdf_table_to_csv(pdf_path, output_csv):
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with pdfplumber.open(pdf_path) as pdf:
            all_tables = []
            for i, page in enumerate(pdf.pages):
                tables = page.extract_tables()
                for table in tables:
                    df = pd.DataFrame(table[1:], columns=table[0])
                    all_tables.append(df)
            if all_tables:
                full_df = pd.concat(all_tables, ignore_index=True)
                full_df.to_csv(output_csv, index=False)
                print(f"CSV saved to {output_csv}")
            else:
                print("No tables found in the PDF.")
    except Exception as e:
        print(f"Error processing PDF: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_to_csv.py input.pdf output.csv")
    else:
        pdf_path = sys.argv[1]
        output_csv = sys.argv[2]
        pdf_table_to_csv(pdf_path, output_csv)

