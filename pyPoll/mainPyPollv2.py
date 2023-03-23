#Import necessary packages
import os
import csv

# Set a filepath to open up the election_data csv file
csvpath = os.path.join('Resources', 'election_data.csv')

#setting global variables(s counters, list to grab candidate's names, a dcitionary to store data)
total_votes = 0
#candidate_votes = []
candidates_list = []
candidates = {}

#Method for reading csv files
with open(csvpath, 'r') as csvfile:

    #CSV reader identifies delimiter and variable that holds the contents
    csvreader = (csv.reader(csvfile, delimiter = ','))
    #Move through the header
    next(csvreader)
    #For loop that iterates through each row. Establish current_candidate variable
    #and then check it against candidate name in in each row. When they are different,
    #append new name to candidates_list and set name as key value and value inside key to 1.
    #This value refledts number of votes for candidate. If name is found in candidates_list,
    #just add 1 to vote count.
    for row in csvreader:
        total_votes = total_votes + 1
        current_candidate = (row[2])
        if current_candidate not in candidates_list:
            candidates_list.append(current_candidate)
            candidates[current_candidate] = 1
        elif current_candidate in candidates_list:
            candidates[current_candidate] += 1
    #Add Total votes to dictionary and find percentages for each candidate
    candidates["Total_Votes"] = total_votes
    c1_percentage = (float(candidates["Charles Casper Stockham"]))/total_votes * 100
    c1_percentage_rounded = (round(c1_percentage, 3))
    c2_percentage = float(candidates['Diana DeGette'])/total_votes * 100
    c2_percentage_rounded = (round(c2_percentage, 3))
    c3_percentage = float(candidates['Raymon Anthony Doane'])/total_votes * 100
    c3_percentage_rounded = (round(c3_percentage, 3))
    
    #Run logic to find winner of the election
    if (candidates["Charles Casper Stockham"] > candidates['Diana DeGette']) and (candidates["Charles Casper Stockham"] > candidates['Raymon Anthony Doane']):
        winner = candidates_list[0]
    elif (candidates['Diana DeGette'] > candidates["Charles Casper Stockham"]) and (candidates['Diana DeGette'] > candidates['Raymon Anthony Doane']):
        winner = candidates_list[1]
    elif (candidates['Raymon Anthony Doane'] > candidates['Diana DeGette']) and (candidates['Raymon Anthony Doane'] > candidates["Charles Casper Stockham"]):
        winner = candidates_list[2]

    #Create Analysis printout report
    lines = (

        f"\nElection Results"
        f"\n------------------------------\n"
        f"Total Votes: {total_votes}"
        f"\n------------------------------"
        f"\nCharles Casper Stockham:  {c1_percentage_rounded}% ({candidates['Charles Casper Stockham']})"
        f"\n\nDiana LeGette:  {c2_percentage_rounded}% ({candidates['Diana DeGette']})"
        f"\n\nRaymon Anthony Doane: {c3_percentage_rounded}% ({candidates['Raymon Anthony Doane']})"
        f"\n------------------------------\n"
        f"Winner: {winner}"
        f"\n------------------------------\n"
    )
    #Print to terminal
    print(lines)

    # Specify the file to write to
    output_path = os.path.join("Analysis", "poll_analysis.txt")

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w') as poll_analysis:
        poll_analysis.write(lines)

