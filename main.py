import csv

def check_time_period_pattern(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

        expected_pattern = ['offpeak', 'peak']
        for i, row in enumerate(rows):
            if row['time_period'] != expected_pattern[i % len(expected_pattern)]:
                return i + 1  # Return row number (1-based index)

    return None

# Example usage
atsbr_file_path = '/Users/philliao/Downloads/Code/IB-Math-IA/ATSBR/atsbr.csv'
row_number = check_time_period_pattern(atsbr_file_path)
if row_number:
    print(f"Row number with mismatched time_period pattern: {row_number}")
else:
    print("All rows follow the time_period pattern.")