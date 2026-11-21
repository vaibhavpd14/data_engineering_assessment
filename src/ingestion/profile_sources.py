import pandas as pd
from pathlib import Path

# look for row file in base folder then data/raw
BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data" / "raw"

# these are tha files exist in raw
FILES = [
    "IND.xlsx",
    "USA.xlsx",
    "AUS.xlsx"
]


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
    for file_name in FILES:

        profile_file(file_name)


if __name__ == "__main__":

    main()