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

    # Read every row after header
    for row in csvreader:
        print(row)

print("Done with CSV")