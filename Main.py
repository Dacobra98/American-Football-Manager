# Importing necessary modules
import random
from listsforgenerating import first_names, last_names

# Create the player class
class Player:
    def __init__(self, name, team, position, age, salary):
        # setting up different player ideas
        self.name = name
        self.team = team
        self.position = position
        self.age = age
        self.salary = salary

# List to have all players
players = []


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
    
        # We want to generate enough players in each position for the team 
        if generatedplayer <= 7:
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
        # We need to generate both teams however so we will check if 52 players have been generated and then change team
        if generatedplayer <= 52 and team2swap == False : # it will equal 52 when it generates last player for the first team
            team = "Team 1"
            
        elif generatedplayer == 53 and team2swap == False: # So we can reset generated player
            team = "Team 2"
            team2swap = True
            generatedplayer = 1
        else: 
            team = "Team 2"

            
        age = 22
        salary = generatedplayer
        
        #Running it through player instance and appending to the list
        player = Player(name, team, position, age, salary)
        players.append(player)

generate_playerstartgame()
# Printing player details
for player in players:
       
    print("Name:", player.name, "Team:", player.team, "Position:", player.position,"Age:", player.age,"Salary: $", player.salary)
