# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_list = []
candidate_dict = dict()

# Winning Candidate and Winning Count Tracker
winner = ["", 0]

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    i = 0
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        if i == 0:    
            candidate_list.append(row[2])
            candidate_dict.update({row[2]: {"votes": 0, "perc": 0}})
            i += 1

        # If the candidate is not already in the candidate list, add them
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            candidate_dict.update({row[2]: {"votes": 0, "perc": 0}})

        # Add a vote to the candidate's count
        for c in candidate_list:
            if c == row[2]:
                candidate_dict[row[2]]["votes"] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Loop through the candidates to determine vote percentages and identify the winner
    for c in candidate_list:

        # Get the vote count and calculate the percentage
        candidate_dict[c]["perc"] = round((candidate_dict[c]["votes"] / total_votes) * 100, 3)

        # Update the winning candidate if this one has more votes
        if candidate_dict[c]["votes"] > winner[1]:
            winner[0] = c
            winner[1] = candidate_dict[c]["votes"]

    # Prepare the output info for the terminal and text file
    output = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
        f"{candidate_list[0]}: {candidate_dict[candidate_list[0]]["perc"]}% ({candidate_dict[candidate_list[0]]["votes"]})\n"
        f"{candidate_list[1]}: {candidate_dict[candidate_list[1]]["perc"]}% ({candidate_dict[candidate_list[1]]["votes"]})\n"
        f"{candidate_list[2]}: {candidate_dict[candidate_list[2]]["perc"]}% ({candidate_dict[candidate_list[2]]["votes"]})\n"
        f"-------------------------\n"
        f"Winner: {winner[0]}\n"
        f"-------------------------"
    )
    # Print the output to the terminal
    print(output)

    # Save the winning candidate summary to the text file
    txt_file.write(output)