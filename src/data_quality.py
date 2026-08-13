from pathlib import Path
import pandas as pd


# Find the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Location of the raw dataset
CSV_PATH = PROJECT_ROOT / "data" / "online_shoppers_intention.csv"


def main():
    # Load the dataset
    df = pd.read_csv(CSV_PATH)

    print("=" * 60)
    print("DATA QUALITY REPORT")
    print("=" * 60)

    # ---------------------------------------------------------
    # 1. Dataset dimensions
    # ---------------------------------------------------------
    print("\n1. DATASET SIZE")
    print(f"Rows:    {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]:,}")

    # ---------------------------------------------------------
    # 2. Column names and data types
    # ---------------------------------------------------------
    print("\n2. DATA TYPES")
    print(df.dtypes.to_string())

    # ---------------------------------------------------------
    # 3. Missing values
    # ---------------------------------------------------------
    print("\n3. MISSING VALUES")

    missing = df.isnull().sum()
    missing_percentage = (missing / len(df)) * 100

    missing_report = pd.DataFrame({
        "missing_values": missing,
        "missing_percentage": missing_percentage.round(2)
    })

    print(missing_report.to_string())

    # ---------------------------------------------------------
    # 4. Duplicate rows
    # ---------------------------------------------------------
    print("\n4. DUPLICATE ROWS")

    duplicate_count = df.duplicated().sum()

    print(f"Duplicate rows: {duplicate_count:,}")

    # ---------------------------------------------------------
    # 5. Unique values in categorical columns
    # ---------------------------------------------------------
    print("\n5. CATEGORICAL VARIABLES")

    categorical_columns = df.select_dtypes(
        include=["object", "str", "bool", "category"]
    ).columns

    for column in categorical_columns:
        print(f"\n{column}:")
        print(df[column].value_counts(dropna=False).to_string())

    # ---------------------------------------------------------
    # 6. Numerical summary
    # ---------------------------------------------------------
    print("\n6. NUMERICAL VARIABLES")

    numerical_columns = df.select_dtypes(
        include=["number"]
    ).columns

    print(
        df[numerical_columns]
        .describe()
        .round(2)
        .to_string()
    )

    # ---------------------------------------------------------
    # 7. Revenue / conversion check
    # ---------------------------------------------------------
    print("\n7. REVENUE / CONVERSION")

    print(df["Revenue"].value_counts().to_string())

    conversion_rate = df["Revenue"].mean() * 100

    print(
        f"\nOverall conversion rate: "
        f"{conversion_rate:.2f}%"
    )

    # ---------------------------------------------------------
    # 8. Date-related information
    # ---------------------------------------------------------
    print("\n8. TIME PERIOD")

    print("Months represented:")
    print(df["Month"].value_counts().sort_index().to_string())

    # ---------------------------------------------------------
    # 9. Final assessment
    # ---------------------------------------------------------
    print("\n9. SUMMARY")

    if missing.sum() == 0:
        print("\u2705 No missing values found.")
    else:
        print(f"\u26A0\uFE0F {missing.sum():,} missing values found.")

    if duplicate_count == 0:
        print("\u2705 No duplicate rows found.")
    else:
        print(f"\u26A0\uFE0F {duplicate_count:,} duplicate rows found.")

    print(
        f"\u2705 Dataset contains {len(df):,} sessions "
        f"and {len(df.columns)} variables."
    )

    print("=" * 60)


if __name__ == "__main__":
    main()