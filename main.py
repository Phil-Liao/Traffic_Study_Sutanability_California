import csv

def get_district_names(file_path):
    """Returns a set of all unique district names from the given CSV file."""
    district_names = set()
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            district_names.add(row['time_period'])
    return district_names

# Example usage
if __name__ == "__main__":
    file_path = "ATSBS/Average_Transit_Speeds_by_Stop_Segments.csv"
    print(get_district_names(file_path))