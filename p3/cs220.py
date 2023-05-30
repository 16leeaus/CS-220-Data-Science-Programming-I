__data = {}

def load_table(name):    
    """load_table(name) opens a table in a CSV file named 'name'"""
    import csv
    f = open(name)
    reader = csv.reader(f)
    header = next(reader)[1:]
    for row in reader:
        __data[row[0]] = dict(zip(header, row[1:]))
    f.close()
    print("ROWS:")
    print(", ".join(sorted(__data.keys())[:20]), "\n")
    print("COLUMNS:")
    print(", ".join(header))

def cell(row_name, col_name):
    """cell(row_name, col_name) returns the value as a string at the specified location in the table opened by a previous 'load_table' call"""
    if len(__data) == 0:
        raise Exception(f"call load_table first")
    row_name = str(row_name)
    if not row_name in __data:
        raise Exception(f"no row named {repr(row_name)} in data")
    row = __data[row_name]
    if not col_name in row:
        raise Exception(f"no col named {repr(col_name)} in data")
    return row[col_name]

def row_count():
    """row_count() returns the number of rows in the table loaded by load_table(...)"""
    if len(__data) == 0:
        raise Exception(f"call load_table first")
    return len(__data)
