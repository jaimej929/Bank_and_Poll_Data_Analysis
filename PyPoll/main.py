import os
import csv

# paths to files
csvpath = os.path.join("Resources","election_data.csv")
csv_output = os.path.join("Analysis", "election_results.txt")

total_votes = 0

canidate_list = []

canidate_name = [""]

canidate_votes = []

each_vote_total = 0

# open csv

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    header = next(csvreader)

    first_row =next(csvreader)
    total_votes +=1
     

    
    for row in csvreader:
        
        total_votes += 1
        
output = (
    f"  Election Results\n"
    f"---------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------\n")
   
print(output)

with open(csv_output, "w") as txt_file:
    txt_file.write(output)
