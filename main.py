import pandas as pd


def sort_by_county_name(xlsx_path):
    df = pd.read_excel(xlsx_path, sheet_name='mode_of_transportation')
    sorted_df = df.sort_values(by='county_fips')
    # No file overwrite, just return the sorted DataFrame
    return sorted_df

# Example usage:
sort_by_county_name('t2w.xlsx')
