import pandas as pd

# Creating one common naming convention 
COLUMN_MAPPING = {

    "ID": "MEMBER_ID",
    "Unique ID": "MEMBER_ID",

    "Name": "MEMBER_NAME",
    "Member Name": "MEMBER_NAME",

    "DOB": "DOB",
    "Date of Birth": "DOB",

    "TierCode": "TIER_CODE",
    "Tier Type": "TIER_CODE",

    "EnrollmentDate": "ENROLLMENT_DATE",
    "Date of Enrollment": "ENROLLMENT_DATE",

    "Flight Date": "LAST_FLIGHT_DATE",
    "FlightDate": "LAST_FLIGHT_DATE",
    "Date of Flight": "LAST_FLIGHT_DATE",

    "Individual or Corporate": "MEMBER_TYPE"

}


EXPECTED_COLUMNS = [

    "MEMBER_ID",
    "MEMBER_NAME",
    "DOB",
    "TIER_CODE",
    "ENROLLMENT_DATE",
    "LAST_FLIGHT_DATE",
    "COUNTRY"

]


COUNTRY_MAPPING = {

    "IND": "IND",
    "USA": "USA",
    "AUS": "AUS"

}


def standardize_columns(df, country):

    # Rename columns
    df = df.rename(columns=COLUMN_MAPPING)

    # Add country information
    df["COUNTRY"] = COUNTRY_MAPPING[country]

    # Add missing expected columns
    for column in EXPECTED_COLUMNS:

        if column not in df.columns:

            df[column] = pd.NA

    # Keep common columns and additional attributes
    additional_columns = [
        column for column in df.columns if column not in EXPECTED_COLUMNS
    ]

    df = df[EXPECTED_COLUMNS + additional_columns]

    # Convert member ID into string
    df["MEMBER_ID"] = df["MEMBER_ID"].astype("string")

    return df