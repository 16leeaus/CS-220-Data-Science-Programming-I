import csv

data = {}

def load_table(name):
    f = open(name)
    reader = csv.reader(f)
    header = next(reader)[1:]
    for row in reader:
        data[row[0]] = dict(zip(header, row[1:]))
    f.close()

def cell(row_name, col_name):
    if len(data) == 0:
        raise Exception(f"call load_table first")
    if not row_name in data:
        raise Exception(f"no row named {repr(row_name)} in data")
    row = data[row_name]
    if not col_name in row:
        raise Exception(f"no col named {repr(col_name)} in data")
    return row[col_name]
