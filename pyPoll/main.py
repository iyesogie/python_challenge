import os
import csv

#create path
election_data_csv = os.path.join ("..","pyPoll", "resources2", "election_data.csv")

#determine variables
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []
#open csv file - election data
with open(election_data_csv,) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # create for loop
    for row in csvreader:
        # Count the number of votes
        count = count + 1
        # create list with names - candidatelist
        candidatelist.append(row[2])
        # Create a set from the candidatelist to get the unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)
        # y equals total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # z equals the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)
    
    #find winner    
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    
    #print results
    print("-------------------------")
    print("Election Results")   
    print("-------------------------")
    print("Total Votes :" + str(count))    
    print("-------------------------")
    for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
    print("-------------------------")
    print("The winner is: " + winner)
    print("-------------------------")



    
  