import pandas as pd

def compare_counties(t2w_xlsx_path, btn_csv_path):
    # Read county_name from t2w.xlsx
    t2w_df = pd.read_excel(t2w_xlsx_path)
    t2w_counties = set(t2w_df['county_name'].dropna().astype(str).str.strip())

    # Read County from btn.csv
    btn_df = pd.read_csv(btn_csv_path)
    btn_counties = set(btn_df['County'].dropna().astype(str).str.strip())

    # Find common and unique counties
    common = t2w_counties & btn_counties
    only_in_t2w = t2w_counties - btn_counties
    only_in_btn = btn_counties - t2w_counties

    print(f"Counties only in t2w.xlsx: {only_in_t2w}")
    print(f"Counties only in btn.csv: {only_in_btn}")
    return common

def filter_t2w_by_btn(t2w_xlsx_path, btn_csv_path, output_path):
    # Get set of counties from btn.csv
    btn_df = pd.read_csv(btn_csv_path)
    btn_counties = set(btn_df['County'].dropna().astype(str).str.strip())

    # Read t2w.xlsx and filter rows
    t2w_df = pd.read_excel(t2w_xlsx_path)
    filtered_df = t2w_df[t2w_df['county_name'].astype(str).str.strip().isin(btn_counties)]
    filtered_df.to_excel(output_path, index=False)
    print(f"Filtered t2w.xlsx saved to {output_path}")


common_counties = compare_counties('t2w.xlsx', 'btn.csv')
print(f"Common counties: {common_counties}")