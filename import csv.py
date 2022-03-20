import csv
with open('foo.csv') as f:
    reader = csv.reader(f, skipinitialspace=True)
    header = next(reader)
    a = [dict(zip(header, map(int, row))) for row in reader]
print a  