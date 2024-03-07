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
      

# Creating the function to sort the players into depth chart, and print the info to the user

def sort_and_print_players(team_players):
    sorted_players = sorted(team_players, key=lambda x: (x.position, -x.ovr))
    current_position = ""
    for player in sorted_players:
        if player.position != current_position:
            current_position = player.position
            print("\nPosition: " + player.position + " ")
        print("Name: " + player.name + " OVR: " + str(player.ovr))

   



    
##################################
##################################
##################################
# Setting variables for the game 
yardline = 0 # Determines the yard line the ball is on
touchdownside = False # If they are on the touchdown side of the field or not, if they are than it will count down, if not they will count up

# All functions now on will create the important functions within the game.


# This function will take place when the user kicks the ball
def kickingfunction():
   print("test")

# This function will take place when the user recives the ball 
def recivingfunction():
     # We want this function to be weighted, so we will generate a random number for the output
    output = random.randint(0,200) # a 50% chance for a touch back, and then a one percent chance for every yard if we already know that it is not a touchback
    if output <= 100:
        print("\nTouchback!")
        print("The ball is on your 25 yard line")
        yardline = 0
        touchdownside = False
    elif output == 200: # This means that it is a touchdown
        print("\nTouchdown!")
    else: # this means it is not a touch back 
        # it needs to be formated, this is doen by removing the 100 for a touchback
        output -= 100
        print("\nhas returned it for", output, "yards!")
        yardline = 0
        if output > 50:
            output = output - 50
            touchdownside = True
            print("The ball is on their",output," yard line")
        else:
            print("The ball is on your",output," yard line")

generate_playerstartgame()
# We will have this in a while loop so that the user keeps going until they start the game
userchoice = 0 # So That we can track the users choices throughout
while userchoice != 1:
    # Now we generate the game for the user, we will come up with a popup of options before they start the game

    print("\nTutorial:")
    print("In order to select an option type the number associated with the option, showcased in the parentheses ex. (1) or (2)")
    print("\nWelcome to football coach! What Would you like to do?")
    userchoice = int(input("Generate the teams and start the game(1)"))
    if userchoice == 1:
        print("Your Players Sorted by Position and OVR:")
        sort_and_print_players(Team1Players)
    if userchoice == 1:
        print("\nOpponents Players Sorted by Position and OVR:")
        sort_and_print_players(Team2Players)
        leavetheloop = input("Press any key when you are ready to leave this menu!") # Just to slow down the user so they have to make an input inorder to leave the sorting function
    else:
        print("ERROR! use a correct input next time!")
        
        
userchoice = 0
while userchoice != 99: # user is unlikely to type 99, and therfore if the user inputs a wrong input choice it will loop them through this gain
    print("\n\n\n\nWelcome to the game coach!")
    userchoice = int(input("Would you like to start the game by kicking(1) or receiving(2)"))
    if userchoice == 1:
        # The user has kicked
        kickingfunction()
        userchoice = 99
    elif userchoice == 2:
        # The user has recived
        recivingfunction()
        userchoice = 99
    else:
        print("ERROR! please put a correct input this time.")
    



generate_playerstartgame()

print("Team 1 Players Sorted by Position and OVR:")
sort_and_print_players(Team1Players)

print("\nTeam 2 Players Sorted by Position and OVR:")
sort_and_print_players(Team2Players)

