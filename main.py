import csv

def check_objectid_pattern(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

        for i in range(1, len(rows), 2):
            objectid_2n = int(rows[i - 1]['OBJECTID'])
            objectid_2n_plus_1 = int(rows[i]['OBJECTID'])

            if objectid_2n + 1 != objectid_2n_plus_1:
                return rows[i]

    return None

def calculate_percentage_below_zero(file_path, column_name):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        total_rows = 0
        below_zero_count = 0

        for row in reader:
            total_rows += 1
            if float(row[column_name]) < 0:
                below_zero_count += 1

        percentage = (below_zero_count / total_rows) * 100 if total_rows > 0 else 0
        return percentage

def get_column_data(file_path, column_name):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        column_data = [float(row[column_name]) for row in reader]
    return column_data

# Example usage
file_path = '/Users/philliao/Downloads/Code/IB-Math-IA/ATSBS/atsbs_merged.csv'

column_name = 'p50_mph'
percentage_below_zero = calculate_percentage_below_zero(file_path, column_name)
print(f"Percentage of data in column '{column_name}' less than 0: {percentage_below_zero:.2f}%")

