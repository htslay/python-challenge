# Import just in case
import os

# Module to read CSV file
import csv

# Create CSV path
csvpath = os.path.join('Resources', 'election_data.csv')

# Variables
# ---------
total_votes = 0

# Lists to track data values
candidates = []
num_votes = []
percent_votes = []

# Read using CSV module
with open(csvpath) as csvfile:

    # Specifies delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row
    csv_header = next(csvreader)

    # Read every row after header
    for row in csvreader:
        
        # Update vote counter
        total_votes += 1

        # Check to see if current candidate is in Candidates list
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    # Convert to percentage and add to % votes list
    for votes in num_votes:
        percentage = round((votes/total_votes) * 100, 3)
        percent_votes.append(percentage)

    # Determine winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# Information Output (terminal)
print("Election Results")
print("----------------")
print(f"Total Votes: {total_votes}")
print(f"--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {num_votes[i]} = {percent_votes[i]}%")
print(f"---------------------------")
print(f"Winner: {winning_candidate}")
print(f"---------------------------")

# Information Output (text file)
output = open("Analysis/output.txt", "w")

line1 = "Election Results"
line2 = "----------------"
line3 = str(f"Total Votes: {total_votes}")
line4 = str(f"--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {num_votes[i]} = {percent_votes[i]}%")
    output.write('{}\n'.format(line))
line5 = str(f"---------------------------")
line6 = str(f"Winner: {winning_candidate}")
line7 = str(f"---------------------------")
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
