import os
import csv
print(os.getcwd())
# Set file path
csv_path1 = os.path.join("election_data_1.csv")
csv_path2 = os.path.join("election_data_2.csv")

# Read file
with open(csv_path1, 'r', newline="") as csv_infile:
    csvreader = csv.reader(csv_infile, delimiter=",")

# Print Header
    print("Election Results")
    print("-------------------------")

# Output to txt file "Output.txt"
    text_file = open("Output.txt", "w")
    text_file.write("Election Results")
    text_file.write("-------------------------")

# Skip the header
    next(csvreader)

# Compile the Voter IDs into a list    
    csvreader = list(csvreader)
# Find the length of the list (total number of Voter ID's)    
total_votes = len(csvreader)
print("Total Votes:", total_votes)
text_file.write("Total Votes:" + str(total_votes))
print("-------------------------")
text_file.write("-------------------------")
    
# Initialize empty list to hold names of candidates
Candidates = []
# Iterate throughout each row in csvreader and compile
for row in csvreader:
    if row[2] not in Candidates:
        Candidates.append(row[2])

# Create dictionary to store candidate votes
candidate_vote = {}
# Set number of votes
num_votes = 0

# Add up the total number of times each candidate name appears throughout list
for row in csvreader:
    if row[2] not in candidate_vote.keys():
        candidate_vote.update({row[2]:num_votes})
    if row[2] in candidate_vote.keys():
        candidate_vote[row[2]] += 1
        
# Print out candidate names, percentage, and total votes per candidate       
for keys, votes in candidate_vote.items():
    print(keys , ":" , str((votes/total_votes)*100), "%" , "(",str(votes),")")

    out_str = str(keys) + ":" + str((votes/total_votes)*100) + "%" + "(" + str(votes) + ")"
    
    text_file.write(out_str)
print("-------------------------")
text_file.write("-------------------------")

# Declare the winner by finding candidate with max votes
winner = max(candidate_vote.values())
for key, value in candidate_vote.items():
    if winner == value:
        print("Winner :" , key)
        text_file.write("Winner :" + str(key))

text_file.close()    
    



    
