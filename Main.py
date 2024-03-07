# Importing necessary modules
import random
from listsforgenerating import first_names, last_names

# Create the player class
class Player:
    def __init__(self, name, team, position, ovr):
        # setting up different player ideas
        self.name = name
        self.team = team
        self.position = position
        self.ovr = ovr

# List to have all players for Team 1
Team1Players = []  # Total Rosters
Team1Sort = [] # So that we can sort the players into a proper depth chart
Team2Players = []  # Total Rosters
Team2Sort = []


# Setting a function to start the game 
def generate_playerstartgame():
    generatedplayer = 0 # Setting a variable to properly generate players
    team2swap = False # Swap teams after team 1 has been fully generated
    for i in range(104):
        generatedplayer += 1
        # Generate random first and last names
        Generaterandomfirstname = random.randint(0, 20)
        Generaterandomlastname = random.randint(0, 20)
        # Combining first and last names
        name = first_names[Generaterandomfirstname] + ' ' + last_names[Generaterandomlastname]
          # We need to generate both teams however so we will check if 52 players have been generated and then change team
        if generatedplayer <= 52 and team2swap == False : # it will equal 52 when it generates last player for the first team
            team = "Team 1"   
        elif generatedplayer == 53 and team2swap == False: # So we can reset generated player
            team = "Team 2"
            team2swap = True
            generatedplayer = 1
        else: 
            team = "Team 2"

        # Next we are going to generate a rating for the players so that the games arent just a 50/50
        ovr = random.randint(30,99)
        
     
        
       
        # We want to generate enough players in each position for the team 
        if generatedplayer  <= 7:
            position = "WR"
        elif generatedplayer <= 10: 
            position = "RB"
        elif generatedplayer <= 13:
            position = "QB"
        elif generatedplayer <= 16:
            position = "TE"
        elif generatedplayer <= 21:
            position = "T"
        elif generatedplayer <= 26:
            position = "G"
        elif generatedplayer <= 29:
            position = "C"
        elif generatedplayer <= 35:
            position = "CB"
        elif generatedplayer <= 41:
            position = "LB"
        elif generatedplayer <= 46:
            position = "DT"
        elif generatedplayer <= 52:
            position = "S"

        player = Player(name,team,position,ovr)
        if team2swap == False:
            Team1Players.append(player)
        else:
            Team2Players.append(player)
      

def sort_and_print_players(team_players):
    sorted_players = sorted(team_players, key=lambda x: (x.position, -x.ovr))
    current_position = ""
    for player in sorted_players:
        if player.position != current_position:
            current_position = player.position
            print("\nPosition: " + player.position + " ")
        print("Name: " + player.name + " OVR: " + str(player.ovr))


generate_playerstartgame()

print("Team 1 Players Sorted by Position and OVR:")
sort_and_print_players(Team1Players)

print("\nTeam 2 Players Sorted by Position and OVR:")
sort_and_print_players(Team2Players)