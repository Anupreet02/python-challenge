import os 
import csv

#path to the csv file
csv_path = r"PyPoll\Resources\election_data.csv"

#set the variables
total_votes = 0
candidates = {}
winner = ""
winning_count = 0


#open and read the csv file 
with open (csv_path)as csv_file:
    csvreader = csv.reader (csv_file,delimiter =",")
    #read the header row first
    csv_header = next(csvreader)

    #read through each row after header 
    for row in csvreader:
        Ballot_ID = row[0]
        County = row [1]
        Candidate = row[2]

        #calculate total votes
        total_votes +=1

        # candidates count
        if Candidate not in candidates:
            candidates[Candidate] = 0
        #add a vote to the candidates's count
        candidates[Candidate] +=1
       
#calculate the result
results = []
for Candidate, votes in candidates.items():
    percentage = (votes/total_votes)*100
    results.append((Candidate,percentage,votes))

    #determine the winner 
    if votes > winning_count:
        winning_count = votes 
        winner = Candidate

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, percentage, votes in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
                                         

