# Import just in case
import os

# Module to read CSV file
import csv

# Create CSV path
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read using CSV module
with open(csvpath) as csvfile:

    # Specifies delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Variables
    row_count = 0
    net_total = 0

    # Read every row after header
    for row in csvreader:
        
        # Finds the number of rows, which is the number of months
        row_count += 1
        net_total += int(row[1])


print("Done with CSV")
print(f"Number of months: {row_count}")
print(f"Net total: ${net_total}")