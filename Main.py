# Hello hope you are doing well, my code is fairly long, so to make it easier for you here is all of the functions that
# apply to the rubric
#
#
#
# I will have detailed comments on how all elements are met within the function, just use crtl+f (windows) or cmd+f (mac)
# and search the function name to find it quickly




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
    return sorted_players
            

    
##################################
##################################
##################################
# Setting variables for the game 
yardline = 0 # Determines the yard line the ball is on
playerside = ''# We will set what side of the ball the player is on too this 
team1returner = []  # Saving the returners within these lists
team2returner = []  # Saving the returners within these lists
yardsgained = 0 # yards gained in any play 
Timeleft = 600 # 600 seconds in 10 minutes, the length of our game will be 10 'minutes' (not real time)
team1score = 0
team2score = 0
playrandomizer = 0 # this will be randomized to determine what happens in a play


# All functions now on will create the important functions within the game
def timeformat(timeleft):
    minutes = timeleft // 60
    seconds = timeleft % 60
    return f"{minutes:02d}:{seconds:02d}"
    

def print_best_players_by_position(team_players): # used so that we can get the best players of both teams 
    positions = ["WR", "RB", "QB", "TE", "T", "G", "C", "CB", "LB", "DT", "S"]
    best_players = {}

    for position in positions:
        best_player = None
        for player in team_players:
            if player.position == position:
                if best_player is None or player.ovr > best_player.ovr:
                    best_player = player
        if best_player:
            best_players[position] = best_player

    total_ovr = 0
    for player in best_players.values():
        total_ovr += player.ovr
    average_ovr = total_ovr / len(best_players)
    average_ovr = round(average_ovr, 0)
    return average_ovr

def yards(type,gained,yardline):# this will be used so that we cant print where the ball is 
   
    if type == "defense":
        if yardline + gained > 50:
            output = 100 - (yardline + gained)
            print("The ball is on your", output, "yard line")
 =----------lp0l            output = yardline + gained
            print("The ball is on their", output, "yard line")
    else:
        if yardline + gained > 50:
            output = 100 - (yardline + gained)
            print("The ball is on their", output, "yard line")
        else:
            output = yardline + gained
            print("The ball is on your", output, "yard line")
    return output


# This function will take place when the user kicks the ball
def kickingfunction(playerside,yardline):
   # We want this function to be weighted, so we will generate a random number for the output
    output = random.randint(0,200) # a 50% chance for a touch back, and then a one percent chance for every yard if we already know that it is not a touchback
    if output <= 100:
        print("\n", team2returner.name, "has elected to take a touchback:")
        output = 25 # needs to be 25 so the yard function can properly add it
        yardline = 0
        yards(playerside,output,yardline)
    elif output == 200: # This means that it is a touchdown
        print(team2returner.name,"Has scored a touchdown on the kick off!")
    else: # this means it is not a touch back 
        # it needs to be formated, this is doen by removing the 100 for a touchback
        output -= 100
        print("\n", team2returner.name, "has returned it for", output, "yards!")
        yards(playerside,output,yardline)
    yardsgained = output 
    return yardsgained
# This function will take place when the user recives the ball 
def recivingfunction(playerside,yardline):
     # We want this function to be weighted, so we will generate a random number for the output
    output = random.randint(1,200) # a 50% chance for a touch back, and then a one percent chance for every yard if we already know that it is not a touchback
    if output <= 100:
        print("\n", team1returner.name, "has elected to take a touchback:")
        output = 25 # needs to be 25 so the yard function can properly add it
        yardline = 0
        yards(playerside,output,yardline)
    elif output == 200: # This means that it is a touchdown
        print(team1returner.name,"Has scored a touchdown on the kick off!")
        playerside = "defense"
    else: # this means it is not a touch back 
        # it needs to be formated, this is done by removing the 100 for a touchback
        output -= 100
        print("\n", team1returner.name, "has returned it for", output, "yards!")
        yards(playerside,output,yardline)
    yardsgained = output 
    return yardsgained

# Punts the ball 
def puntfunction(playerside,team,yardline):
    print("THE BALL IS BEING PUNTED")
    playrandomizer = random.randint(30,70)
    yardline = yardline + playrandomizer
    if yardline >= 100:
        yardline = 20
        print(team[0].name,"has punted the ball for a touchback")
    else:
        yardline = 100 - yardline
        print(team[0].name,"has punted the ball")
    playerside = "defense"
    yardsgained = 0
    yards(playerside, yardsgained, yardline)
    return playerside
def fgfunction(playerside):
    print("You have kicked a fg")

down = 1 # What down it is, starts on first down 
yardsleft = 10 # Yards left until first down 
firstdown = False # Will keep track if the last play was a first down 
onthegoalline = False
# This function will be responsible for the offense of the game
def offense(offensive_players, yardline,playerside,Timeleft,yardsleft,team1score,team2score):
    yardsgained = 0
    down = 1
    onthegoalline = False
    print("\n")
    while playerside == "offense" and Timeleft > 0: # We want the funtion to loop while the user plays on offense and time is left on the clock 
        yardsgained = 0
        if down > 4 and yardsleft > 0:# Turn over on downs
            print("Turnover on downs")
            playerside == "defense"
            return
        if yardsleft <= 0: # means a first down took place
            print("FIRST DOWN")
            if yardline <90: # not on the goal line 
                down = 1
                yardsleft = 10
            else: 
                down = 1
                onthegoalline = True

        print("You are on offense.")
        yards(playerside, yardsgained,yardline)
        if onthegoalline == False:
            print(down,"&",yardsleft, timeformat(Timeleft),"left, You:",team1score,"Computer:",team2score)
        else: 
            print(down,"& goal", timeformat(Timeleft),"left")
        # Now we will ask the user what play they will like to run, but first we will set it to 0 
        if down != 4 and Timeleft > 60 : # We do not want to allow the user to punt unless its fourth down or with very little time     
            userinput = int(input("Would you like to call for a pass (1) or a run (2)"))
        elif down != 4 and Timeleft > 60 : #Allow them to kick close to the goal when time is expering,
            userinput = int(input("Would you like to call for a pass (1), a run (2)Team1Players[35].position or kick a fg (4)"))
        elif down == 4 and Timeleft > 60 and yardline > 60: # allow the user to kick close to the goal 
            userinput = int(input("Would you like to call for a pass (1), a run (2) or kick a fg (4)"))
        elif down == 4 and Timeleft > 60 and yardline <= 60:
            userinput = int(input("Would you like to call for a pass (1), a run (2) or a punt(3)"))
        elif down == 4 and Timeleft < 60:
            userinput = int(input("Would you like to call for a pass (1), a run (2) or a punt(3), or kick a fg (4)")) 
        print("\n") 
        if userinput == 1: # this is a pass
            userinput = int(input("Would you like to throw a short pass(1) or a long pass(2)"))  
            print("You have called for a pass")
                # We will first run a chance for an interception or a sack it will be a 10% chance of a sack, and a 3% chance of a pick all else will continue on
            playrandomizer = random.randint(1,100)
            if playrandomizer <= 3:
                print("THE PASS HAS BEEN INTERCEPTED")
                playerside = "defense"
                yardline = 100 - yardline # flip the field
                Timeleft -= random.randint(5,15) # Time Burned by the sack 
                return
            elif playrandomizer <= 13: # all under 13 will be flagged by the first if, so this will only capture 4-13
                yardsgained -= random.randint(1,10) # random yards lost in the sack 
                print("THE QUARTERBACK HAS BEEN SACKED BY", Team2Players[9-11].name, "For a loss of",yardsgained,"yards")
                Timeleft -= random.randint(5,15) # Time Burned by the sack 
                down += 1
                yardsleft = yardsleft - yardsgained
            else: 
                # this means the pass was successful 
                if userinput == 1: # This means it is a short pass, which is more likely to take place, but gain less yards
                    # We will make it a 75% chance for a completion
                    playrandomizer = random.randint(1,100)
                    if playrandomizer <= 75: # It was a sucessful pass
                        yardsgained = random.randint(1,15)
                        print(Team1Players[random.randint(45,49)].name,"Has Caught a pass for",yardsgained,"yards")
                        Timeleft -= random.randint(5,10) # Time Burned by the play 
                        down += 1
                        yardsleft = yardsleft - yardsgained
                    else:
                        print("INCOMPLETE PASS")
                        Timeleft -= random.randint(5,10)
                        down += 1
                else: # This means it is a long pass, which is less likely to take place, but longer distance
                    # We will make it a 50% chance for a completion
                    playrandomizer = random.randint(1,100)
                    if playrandomizer <= 50: # It was a sucessful pass
                        yardsgained = random.randint(15,30)
                        print(Team1Players[random.randint(45,49)].name,"Has Caught a pass for",yardsgained,"yards")
                        Timeleft -= random.randint(10,15) # Time Burned by the play 
                        down += 1
                        yardsleft = yardsleft - yardsgained
                    else:
                        print("INCOMPLETE PASS")
                        Timeleft -= random.randint(5,10)
                        down += 1
        elif userinput == 2: # this means it will be a run play
            playrandomizer = random.randint(1,100) # We will have a 30% chance of a TFL and a 70% chance of moving forawrd 
            if playrandomizer <= 30:
                yardsgained -= random.randint(1,5) # random yards lost in the sack 
                print("A TFL BY", Team2Players[9-11].name, "For a loss of",yardsgained,"yards")
                Timeleft -= random.randint(1,5) # Time Burned by the sack 
                down += 1
                yardsleft = yardsleft - yardsgained
            else: # this means it passed our check, 
                # We will no allow for the rush
                playrandomizer = random.randint(1,150)
                Timeleft -= random.randint(1,10)
                yardsgained = playrandomizer // 10
                down += 1
                print("A", yardsgained, "yard rush by", Team1Players[random.randint(28,29)].name)
                yardsleft -= yardsgained
        elif userinput == 3: # the user is punting
            playerside = puntfunction(playerside,Team1Players,yardline)
        elif userinput == 4: # The user is kicking a field goal
            playerside = fgfunction(playerside)
        
    
generate_playerstartgame()
# We will have this in a while loop so that the user keeps going until they start the game
userchoice = 0 # So That we can track the users choices throughout
while userchoice != 1:
    # Now we generate the game for the user, we will come up with a popup of options before they start the game

    print("\nTutorial:")
    print("In order to select an option type the number associated with the option, showcased in the parentheses ex. (1) or (2)")
    print("\nWelcome to football coach! What Would you like to do?")
    userchoice = int(input("Start the game!(1)"))
    if userchoice == 1:
        # Sorts the lists, and then saves it back under team 2 players to keep an accurate depth chart. 
        Team1Players = sort_and_print_players(Team1Players)
        
    
    if userchoice == 1:
        # Sorts the lists, and then saves it back under team 2 players to keep an accurate depth chart. 
        Team2Players = sort_and_print_players(Team2Players)
        
    else:
        print("ERROR! use a correct input next time!")

# Now we need to inform the user of the quality of their team 

userchoice = 0
while userchoice != 99: # user is unlikely to type 99, and therfore if the user inputs a wrong input choice it will loop them through this gain
    print("\n\n\n\nWelcome to the game coach!")
    print("Your team is",print_best_players_by_position(Team1Players),"Overall")
    print("Your opponent's team is",print_best_players_by_position(Team2Players),"Overall")  # inform the players o ftheir team 
    userchoice = int(input("Would you like to start the game by kicking(1) or receiving(2)"))
    # Saving both returners on each team fo the rest of the game
    team1returner = Team1Players[45]  # Access the best wr on the team
    team2returner = Team2Players[45]  # Access the best wr on the second team 


        player = Player(name,team,position,ovr)
        if team2swap == False:
            Team1Players.append(player)
        else:
            Team2Players.append(player)

# Creating the function to sort the players into depth chart, and print the info to the user


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

playerside = ''# We will set what side of the ball the player is on too this 

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
    




# All functions now on will create the important functions within the game.
def yards(type,gained):# this will be used so that we cant print where the ball is 
    if type == "defense":
        # This means the first 50 yards is their yards the last 50 is yours
        if yardline + gained > 50:
            output = 100 - (yardline + gained)
            print("The ball is on your",output," yard line")
        else:
            output = yardline + gained
            print("The ball is on their",output," yard line")
    else:
        # This means the first 50 yards is their yards the last 50 is yours
        if yardline + gained > 50:
            output = 100 - (yardline + gained)
            print("The ball is on their",output," yard line")
        else:
            output = yardline + gained
            print("The ball is on your",output," yard line")

# This function will take place when the user kicks the ball
def kickingfunction():
   # We want this function to be weighted, so we will generate a random number for the output
    output = random.randint(0,200) # a 50% chance for a touch back, and then a one percent chance for every yard if we already know that it is not a touchback
    if output <= 100:
        print("\nTouchback!")
        yardline = 0
        output = 25 # needs to be 25 so the yard function can properly add it
        yards(playerside,output)
    elif output == 200: # This means that it is a touchdown
        print("\nTouchdown!")
    else: # this means it is not a touch back 
        # it needs to be formated, this is doen by removing the 100 for a touchback
        output -= 100
        print("\nhas returned it for", output, "yards!")
        yards(playerside,output)

# This function will take place when the user recives the ball 
def recivingfunction():
     # We want this function to be weighted, so we will generate a random number for the output
    output = random.randint(1,200) # a 50% chance for a touch back, and then a one percent chance for every yard if we already know that it is not a touchback
    if output <= 100:
        print("\nTouchback!")
        output = 25 # needs to be 25 so the yard function can properly add it
        yardline = 0
        yards(playerside,output)
    elif output == 200: # This means that it is a touchdown
        print("\nTouchdown!")
    else: # this means it is not a touch back 
        # it needs to be formated, this is doen by removing the 100 for a touchback
        output -= 100
        print("\nhas returned it for", output, "yards!")
        yards(playerside,output)
    
generate_playerstartgame()

# We will have this in a while loop so that the user keeps going until they start the game
userchoice = 0 # So That we can track the users choices throughout
while userchoice != 1:
    # Now we generate the game for the user, we will come up with a popup of options before they start the game

    print("\nTutorial:")
    print("In order to select an option type the number associated with the option, showcased in the parentheses ex. (1) or (2)")
    print("\nWelcome to football coach! What Would you like to do?")
    userchoice = int(input("Start the game and see the teams!(1)"))
    if userchoice == 1:
        print("\nYour Players Sorted by Position and OVR:")
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
        userchoice = 99
        playerside = "defense"

        yardline = kickingfunction(playerside,yardline)

        kickingfunction()

    elif userchoice == 2:
        # The user has recived
        userchoice = 99
        playerside = "offense"

        yardline = recivingfunction(playerside,yardline)
    else:
        print("ERROR! please put a correct input this time.")

gameisrunning = True
while gameisrunning == True: # Have this function run while the game continues in order to, loop all functions of the game
    if playerside == "offense": # We will call an offensive function if they are on offense
        offense(Team1Players, yardline,playerside,Timeleft,yardsleft,team1score,team2score)
        gameisrunning = "false"
    elif playerside == "defense": # We will call a defensive function if they are on defense
        defense()
        gameisrunning = "false"
    elif playerside == "kickoff": # We will run the kickoff function
        kickingfunction(playerside,yardline)
        gameisrunning = "false"
    elif playerside == "return": # We will run the return function 
        recivingfunction(playerside,yardline)
        gameisrunning = "false"
    

        recivingfunction()
    else:
        print("ERROR! please put a correct input this time.")

    


print("Team 1 Players Sorted by Position and OVR:")
sort_and_print_players(Team1Players)

print("\nTeam 2 Players Sorted by Position and OVR:")
sort_and_print_players(Team2Players)



