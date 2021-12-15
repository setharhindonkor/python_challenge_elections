###### Objectives ######

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

###### Output ######

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------

# Import Packages
import os
import csv
# Set Path
csv_path = os.path.join("Resources","election_data.csv")
#input_file = "Resources/budget_data.csv"

#Define List
voter_id_list = []
county_list = []
candidate_list = []
unique_candidates_list = []
candidates_total_list = []
total_per_candidate=[]
candidate_percent_list=[]


#Define Variables:

number_of_votes = 0
candidates_total=0

# Open the csv file for reading
with open(csv_path,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

#Loop through rows of files    
    for row in csvreader:
        number_of_votes +=1
        voter_id_list.append(int(row[0]))
        county_list.append(row[1])
        candidate_list.append(row[2])
    unique_candidates_list = set(candidate_list)
    unique_candidates_list=list(unique_candidates_list)

    #print(unique_candidates_list)
    #print(number_of_votes)
    for name in unique_candidates_list:
        #candidate_list.count(name) 
        candidates_total=candidate_list.count(name)
        candidates_total_list.append(candidates_total)
    data=sorted(zip(unique_candidates_list,candidates_total_list),reverse=True,key=lambda x:x[1])
             
#Winner of election based on popular vote

winner_vote=max(candidates_total_list)
max_index=candidates_total_list.index(winner_vote)
winner=unique_candidates_list[max_index]

# Print Analysis

print(str("Election Results"))
print(str("-------------------------"))
print(str("Total Votes: ")+ str(number_of_votes) )
print(str("------------------------"))
for x in data:
    print(x[0] + ": " + str(format((x[1]/number_of_votes)*100, ".3f")) + "% " + "("+str(x[1])+")") 
print(str("-------------------------"))    
print("Winner: " + str(winner))
print(str("-------------------------"))


#Open text file(analysis.txt) for writing
f = open("analysis.txt", "w")

# Write data to text file
f.write(str("Election Results"))
f.write(str("\n") + str("-------------------------"))
f.write(str("\n") + str("Total Votes: ")+ str(number_of_votes) )
f.write(str("\n") + str("------------------------\n"))
for x in data:
    f.write(x[0] + ": " + str(format((x[1]/number_of_votes)*100, ".3f")) + "% " + "("+str(x[1])+")"+ str("\n")) 
f.write(str("-------------------------\n"))    
f.write("Winner: " + str(winner))
f.write(str("\n") + str("-------------------------"))

# Close text file
f.close()