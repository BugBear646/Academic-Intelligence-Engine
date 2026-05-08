import pandas as pd
import os


def export_csv(records, college_name):

    if not records:

        print("No records to export.")

        return

    os.makedirs(
        "data/exports",
        exist_ok=True
    )

    safe_name = (
        college_name
        .lower()
        .replace(" ", "_")
    )

    filename = (
        f"data/exports/"
        f"{safe_name}_professors.csv"
    )

    df = pd.DataFrame(records)

    df.to_csv(
        filename,
        index=False
    )

    print(f"\nCSV exported: {filename}")