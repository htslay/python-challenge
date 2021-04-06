# Import just in case
import os

# Module to read CSV file
import csv

# Create CSV path
csvpath = os.path.join('Resources', 'budget_data.csv')

# Variables
    row_count = 0
    net_total = 0
    # Current profit or loss value for a given month
    value = 0
    # Current delta between month and previous month
    delta = 0

    # Lists to track data values
    dates = []
    changes = []

# Read using CSV module
with open(csvpath) as csvfile:

    # Specifies delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row
    csv_header = next(csvreader)

    # Read every row after header
    for row in csvreader:
        
        # Finds the number of rows, which is the number of months
        row_count += 1

        # Updates total net profits/losses
        net_total += int(row[1])

        # Adds current month to date list
        dates.append(row[0])

        # Calculates delta and adds to changes list
        delta = int(row[1]) - value
        changes.append(delta)

        # Updates value for next caluculation
        value = int(row[1])


print("Done with CSV")
print(f"Number of months: {row_count}")
print(f"Net total: ${net_total}")