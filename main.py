import pandas as pd

def get_district_name_set(csv_path):
    df = pd.read_csv(csv_path)
    district_name_set = set(df['district_name'].dropna().unique())
    print('Set of all data in the "district_name" column:', district_name_set)
    return district_name_set

# Example usage:
get_district_name_set('avgts.csv')
