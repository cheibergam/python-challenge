import os
import csv

# File path based on the relative path
filepath = "./Resources/election_data.csv"

# Opening CSV file
csvfile = open(filepath, 'r')
csvreader = csv.reader(csvfile, delimiter=',')

# Initialising the variables to process CSV file
poll_report_dict = {}
total_votes = 0

# Header of the CSV file
header = next(csvreader)

# Extracting the required data from the CSV file
for row in csvreader:
    # Counting the new vote being processed
    total_votes = total_votes + 1
    
    # Getting the name of the candidate
    candidate = row[2]
    
    #Updating the countier of the canidate in the dictionary
    if candidate in poll_report_dict:
        poll_report_dict[candidate] = poll_report_dict[candidate] + 1
    else:
        poll_report_dict[candidate] = 1

# Closing CSV file
csvfile.close()
    
# Identifying the Winner
candidates = list(poll_report_dict.keys())  # List of cadidates from the dictionary
votes = list(poll_report_dict.values())     # List of votes from the dictionary
index_winner = votes.index(max(votes))      # Identify the index with the Max number of votes
winner = candidates[index_winner]           # String with the name of the Winner (and dictionary key)

# Initialising the variables to prepare the report and identify the winner
result_string = []
winner_key = ""

# Preparing the result string for the election report
for key in poll_report_dict:
    # Calculating the percentage of votes for each voted candidate
    percent = round((float(poll_report_dict[key])*100/total_votes),3)
    
    # Preparing the string with the details of the candidate, number of votes, and % of votes
    candidate_string = key + ": " + str(percent) + "% (" + str(poll_report_dict[key]) + ")"
    result_string.append(candidate_string)

# Writing the results TXT file in the analysis folder
with open('./analysis/results.txt', 'w') as f:
    f.write ("Election Results\n")
    f.write ("-------------------------\n")
    f.write ("Total Votes: " + str(total_votes) + "\n")
    f.write ("-------------------------\n")
    for s in result_string:
        f.write (s + "\n")
    f.write ("-------------------------\n")
    f.write ("Winner: " + winner + "\n")
    f.write ("-------------------------")
    f.close()

# Printing the report in the screen
print ("Election Results")
print ("-------------------------")
print ("Total Votes: " + str(total_votes))
print ("-------------------------")
for s in result_string:
    print (s)
print ("-------------------------")
print ("Winner: " + winner)
print ("-------------------------")