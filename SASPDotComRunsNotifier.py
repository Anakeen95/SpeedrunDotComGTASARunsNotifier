#!/usr/bin/env python3

# Imports the necessary libraries for this script execution
import json
import srcomapi, srcomapi.datatypes as dt
from termcolor import colored

# Initializes the Speedrun.com API
api = srcomapi.SpeedrunCom()

""" Main Program """

print(colored(f"Starting the script...", "yellow"))

print("\nProceeding to get the Grand Theft Auto San Andreas new submitted runs...\n")

# Searches for the game with the abbreviation "GTASA" (GTA: San Andreas) in the Speedrun.com database
# The result is returned as a list, and we take the first game result
gameSA = api.search(dt.Game, {"abbreviation": "GTASA"})[0]

# Fetches all runs for the game "GTA: San Andreas" (GTASA)
# Filtering runs that are in 'new' state (queued for review)
runs = api.search(dt.Run, {"game": gameSA.id, "status": "new"})

# Defines the list that will contain the runs information
runs_info = []

# Iterates over the runs
for run in runs:
    # The 'run.category' may already be the category name or ID, so use it directly
    run_details = {
        "id": run.id,
        "category": run.category if run.category else "Unknown Category",  # Uses the category as is, no need for another API call
        "submitted_date": run.date,
        "time": run.times['primary_t'], # primary time in seconds
        "players": [player.name for player in run.players],
        
        "platform": run.system['platform'] if 'platform' in run.system else "Unknown Platform" # Accesses the platform from run.system['platform']
    }
    runs_info.append(run_details)

# Check if the runs_info list is empty
if not runs_info:
    # If no runs are found, prints a custom message
    print(json.dumps([{"message": "No new runs to review found for Grand Theft Auto San Andreas"}], indent=4))
else:
    # If runs are found, print them as formatted JSON
    print("New runs submitted for Grand Theft Auto San Andreas:")

    print(json.dumps(runs_info, indent=4))

