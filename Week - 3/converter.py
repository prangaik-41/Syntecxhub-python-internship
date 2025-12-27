import argparse
import logging
import sys
import pandas as pd

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def clean_data(df):
    # Normalize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Handle missing values
    df.fillna("", inplace=True)

    # Parse date columns if name contains 'date'
    for col in df.columns:
        if "date" in col:
            try:
                df[col] = pd.to_datetime(df[col], errors="coerce").dt.strftime("%Y-%m-%d")
                df[col].fillna("", inplace=True)
            except Exception:
                logging.warning(f"Date parsing skipped for column: {col}")

    # Rename columns starting with 'id' to 'record_id'
    rename_map = {col: "record_id" for col in df.columns if col.startswith("id")}
    if rename_map:
        df.rename(columns=rename_map, inplace=True)

    return df

def convert_csv_to_excel(input_file, output_file):
    try:
        logging.info(f"Reading CSV file: {input_file}")
        df = pd.read_csv(input_file)

        logging.info("Cleaning and normalizing data...")
        df = clean_data(df)

        logging.info(f"Writing Excel file: {output_file}")
        df.to_excel(output_file, index=False, engine="openpyxl")

        logging.info("CSV to Excel conversion completed successfully.")
    except FileNotFoundError:
        logging.error("Input file not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        logging.error("CSV file is empty or invalid.")
        sys.exit(1)
    except pd.errors.ParserError:
        logging.error("CSV file is corrupted or badly formatted.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        sys.exit(1)

def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Convert CSV to Excel (.xlsx)")
    parser.add_argument("-i", "--input", required=True, help="Path to input CSV file")
    parser.add_argument("-o", "--output", required=True, help="Path to output Excel file (.xlsx)")

    args = parser.parse_args()

    if not args.output.endswith(".xlsx"):
        logging.error("Output file must have a .xlsx extension.")
        sys.exit(1)

    convert_csv_to_excel(args.input, args.output)

if __name__ == "__main__":
    main()
