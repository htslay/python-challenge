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

# The rest of the math!    
# ---------------------

# Average Change in profits/losses between months
avg_change = sum(changes)/len(changes)

# Greatest increase in profits
greatest_increase = max(changes)
greatest_index = changes.index(greatest_increase)
greatest_month = dates[greatest_index]

# Greatest loss in profits
greatest_loss = min(changes)
loss_index = changes.index(greatest_loss)
loss_month = dates[loss_index]

# Information Output (terminal)
print("Finanical Analysis")
print("------------------")
print(f"Number of months: {row_count}")
print(f"Net total: ${net_total}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: ${greatest_increase} during {greatest_month}")
print(f"Greatest Loss in Profits: ${greatest_loss} during {loss_month}")