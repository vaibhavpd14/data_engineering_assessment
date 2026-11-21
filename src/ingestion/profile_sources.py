import pandas as pd
from pathlib import Path

# look for row file in base folder then data/raw
BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data" / "raw"

# these will check files exist in raw
def discover_files():

    files = list(DATA_DIR.glob("*.xlsx"))

    if not files:
        print("No Excel files found in the raw directory.")
        return []

    return files


def profile_file(file_name):

    file_path = DATA_DIR / file_name

    print("\n" + "=" * 60)
    print(f"FILE NAME: {file_name}")
    print("=" * 60)

    # Read Excel file
    df = pd.read_excel(file_path)

    # Dataset dimensions
    print("\nDataset Shape:")
    print(df.shape)

    # Column names
    print("\nColumn Names:")
    print(df.columns.tolist())

    # Data types
    print("\nData Types:")
    print(df.dtypes)

    #Checking Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    #Checking Duplicate records
    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    # Unique values
    print("\nUnique Values:")
    print(df.nunique())

    # First five records
    print("\nSample Records:")
    print(df.head())


def main():
    # itereting through all files 
    files = discover_files()

    if not files:
        return "no files to execute"

    print(f"\nTotal Excel Files Found: {len(files)}")

    for file_path in files:

        profile_file(file_path)


if __name__ == "__main__":

    main()