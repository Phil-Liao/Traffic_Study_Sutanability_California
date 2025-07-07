import openpyxl


def get_unique_values_from_excel(file_path, column_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    column_index = None
    for col in sheet.iter_cols(1, sheet.max_column):
        if col[0].value == column_name:
            column_index = col[0].column
            break

    if column_index is None:
        raise ValueError(f"Column '{column_name}' not found in the Excel file.")

    unique_values = {row[column_index - 1].value for row in sheet.iter_rows(min_row=2)}
    return unique_values


def check_empty_values_in_column(file_path, column_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    column_index = None
    for col in sheet.iter_cols(1, sheet.max_column):
        if col[0].value == column_name:
            column_index = col[0].column
            break

    if column_index is None:
        raise ValueError(f"Column '{column_name}' not found in the Excel file.")

    empty_rows = []
    for row in sheet.iter_rows(min_row=2):
        if row[column_index - 1].value is None:
            empty_rows.append(row[0].row)  # Append row number

    return empty_rows


# Example usage
hci_file_path = '/Users/philliao/Downloads/Code/IB-Math-IA/T2W/hci_transportation2work_42_ct_pl_co_re_st_12-12-13-revised-ada.xlsx'
reportyear_set = get_unique_values_from_excel(hci_file_path, 'reportyear')
print(f"Unique values in column 'reportyear':", reportyear_set)

empty_rows = check_empty_values_in_column(hci_file_path, 'pop_total')
if empty_rows:
    print(f"Rows with empty values in column 'pop_total':", empty_rows)
else:
    print("No empty values found in column 'pop_total'.")