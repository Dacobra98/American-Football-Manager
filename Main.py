import random
import time
# Variables required before and after starting the game
Team1Player = []
Team2Player = []
Positions = ['QB', 'RB', 'WR', 'TE', 'T', 'G', 'C', 'G', 'T', 'DL', 'DT', 'DE', 'LB', 'CB', 'S', 'K', 'P']
generatedplayer = 0
team2swap = False
yardline = 0
playerside = ''
yardsgained = 0
Timeleft = 600
teamscores = {'Player': 0, 'Computer': 0}
play_outcome = 0
userchoice = 0
gameisrunning = True
yardsleft = 100
yardsuntilfirstdown = 0 


# Names for generating players
first_names = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Charles", "Thomas", "Christopher", "Daniel", "Matthew", "Anthony", "Donald", "Mark", "Paul", "Steven", "Andrew", "Kenneth", "Joshua", "Kevin", "Brian", "George", "Edward", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Nicholas", "Eric", "Stephen", "Jonathan", "Larry", "Justin", "Scott", "Brandon", "Benjamin", "Samuel", "Frank", "Gregory", "Raymond", "Alexander", "Patrick", "Jack", "Dennis", "Jerry", "Tyler", "Aaron", "Jose", "Henry", "Adam", "Douglas", "Nathan", "Peter", "Zachary", "Kyle", "Walter", "Harold", "Jeremy", "Ethan", "Carl", "Keith", "Roger", "Gerald", "Christian", "Terry", "Sean", "Arthur", "Austin", "Noah", "Lawrence", "Jesse", "Joe", "Bryan", "Billy", "Jordan", "Albert", "Dylan", "Bruce", "Willie", "Gabriel", "Alan", "Juan", "Louis", "Jonathan", "Wayne", "Bradley", "Liam", "Russell", "Lloyd"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington", "Butler", "Simmons", "Foster", "Gonzales", "Bryant", "Alexander", "Russell", "Griffin", "Diaz", "Hayes"]

class Player:
    def __init__(self, name, position, rating):
        self.name = name
        self.position = position
        self.rating = rating

# Directly determine the team based on the player's number
for i in range(34):
    name = random.choice(first_names) + ' ' + random.choice(last_names)
    rating = random.randint(70, 99)
    position = Positions[i % len(Positions)]  # Loop through positions
    player = Player(name, position, rating)
    (Team2Player if i >= 17 else Team1Player).append(player)

# Now we will infrom the users about the quality of both teams

# Initialize sums and counts for Team 1 categories
offensive_sum_team1 = defensive_sum_team1 = special_teams_sum_team1 = 0
offensive_count_team1 = defensive_count_team1 = special_teams_count_team1 = 0

# Initialize sums and counts for Team 2 categories
offensive_sum_team2 = defensive_sum_team2 = special_teams_sum_team2 = 0
offensive_count_team2 = defensive_count_team2 = special_teams_count_team2 = 0

# Position categories
offensive_positions = ['QB', 'RB', 'WR', 'TE', 'T', 'G', 'C']
defensive_positions = ['DL', 'DT', 'DE', 'LB', 'CB', 'S']
special_teams_positions = ['K', 'P']

# Calculate sums and counts for Team 1
for player in Team1Player:
    if player.position in offensive_positions:
        offensive_sum_team1 += player.rating
        offensive_count_team1 += 1
    elif player.position in defensive_positions:
        defensive_sum_team1 += player.rating
        defensive_count_team1 += 1
    elif player.position in special_teams_positions:
        special_teams_sum_team1 += player.rating
        special_teams_count_team1 += 1

# Calculate sums and counts for Team 2
for player in Team2Player:
    if player.position in offensive_positions:
        offensive_sum_team2 += player.rating
        offensive_count_team2 += 1
    elif player.position in defensive_positions:
        defensive_sum_team2 += player.rating
        defensive_count_team2 += 1
    elif player.position in special_teams_positions:
        special_teams_sum_team2 += player.rating
        special_teams_count_team2 += 1

# Calculate and round averages for Team 1
team1_offensive_avg = round(offensive_sum_team1 / offensive_count_team1) if offensive_count_team1 else 0
team1_defensive_avg = round(defensive_sum_team1 / defensive_count_team1) if defensive_count_team1 else 0
team1_special_teams_avg = round(special_teams_sum_team1 / special_teams_count_team1) if special_teams_count_team1 else 0

# Calculate and round averages for Team 2
team2_offensive_avg = round(offensive_sum_team2 / offensive_count_team2) if offensive_count_team2 else 0
team2_defensive_avg = round(defensive_sum_team2 / defensive_count_team2) if defensive_count_team2 else 0
team2_special_teams_avg = round(special_teams_sum_team2 / special_teams_count_team2) if special_teams_count_team2 else 0

####################
####################
####################

def timeformat(timeleft): # Used to format the tgime
    minutes = timeleft // 60
    seconds = timeleft % 60
    return f"{minutes:02d}:{seconds:02d}"


def yards(yardsgained, yardline, playerside):
    # Assuming yardline ranges from 0 to 100, where 0 is the player's end zone and 100 is the opponent's end zone.
    new_yardline = yardline + yardsgained  # Move down the field based on yards gained.
    if playerside == "defense":
        if new_yardline >= 100:  # Touchdown condition
            print("Touchdown!")
            # Reset for kickoff or scoring logic here.
        else:
            if new_yardline > 50:  # On the opponent's side
                print(f"The ball is on your {100 - new_yardline} yard line.")
            else:  # On the player's side
                print(f"The ball is on their {new_yardline} yard line.")
    else:
        if new_yardline >= 100:  # Touchdown condition
            print("Touchdown!")
            # Reset for kickoff or scoring logic here.
        else:
            if new_yardline > 50:  # On the opponent's side
                print(f"The ball is on their {100 - new_yardline} yard line.")
            else:  # On the player's side
                print(f"The ball is on your {new_yardline} yard line.")

    return new_yardline

def recivingfunction(playerside, yardline):
    input("Press enter to recieve the kick") # not actually taking input, just allowing the user to control when they want to recive the ball
    yardline = 0 # yardline will reset because it is kickoff 
    yardsgained = 25 # Putting them on the 25 yard line
    print(Team1Player[2].name, "has elected to take a touchback") 
    yardline = yards(yardsgained, yardline, playerside)
    return yardline 

def kickingfunction(playerside, yardline):
    input("Press enter to kick the ball") # not actually taking input, just allowing the user to control when they want to kick the ball
    yardline = 0 # yardline will reset because it is kickoff 
    yardsgained = 25 # Putting them on the 25 yard line
    print(Team2Player[2].name, "has elected to take a touchback")
    return yardline     

def offense(playerside):
    playerside = "defense"
    return playerside 

def defense(playerside, yardline, teamscores, Timeleft):
    down = 1  # Set it to first down
    yardsToGo = 10  # Set it to first and ten
    while playerside == "defense" and Timeleft > 0:
        if down > 4:  # Turnover on downs
            print("Turnover on downs!")
            playerside = "offense"
            break  # Exiting the loop and switching sides

        # Display down, yards to go, and time left
        print(f"\nDown: {down} & {yardsToGo}, Time left: {timeformat(Timeleft)}, Score - You: {teamscores['Player']}, Computer: {teamscores['Computer']}")

        play_outcome = random.randint(1, 100)
        if play_outcome <= 60:  # Gain
            yards_gained = random.randint(1, 10)
            print(f"Computer gained {yards_gained} yards.")
        elif play_outcome <= 90:  # Loss
            yards_gained = -random.randint(1, 5)
            print(f"Computer lost {-yards_gained} yards.")
        elif play_outcome <= 95:  # Turnover
            print("Turnover! Player's ball.")
            playerside = "offense"
            break
        else:  # Touchdown
            print("Computer scores a touchdown!")
            teamscores['Computer'] += 7
            playerside = "reciving"
            break

        # Update yardline and yards to go based on the play outcome
        yardline += yards_gained
        yardsToGo -= yards_gained

        # Call the yards function to display the new yardline
        yardline = yards(yards_gained, yardline, playerside)  # Update and print the new yard line

        if yardline >= 100:  # Correcting for a touchdown
            print("Computer scored a touchdown!")
            teamscores['Computer'] += 7
            playerside = "reciving"
            break

        if yardsToGo <= 0:  # Achieved a first down
            down = 1
            yardsToGo = 10
            print("First down!")
        else:
            down += 1

        Timeleft -= random.randint(1, 10)  # Decrement time

        if down > 4 and yardsToGo > 0:  # Check for turnover on downs after updating for the current play
            print("Turnover on downs!")
            playerside = "offense"
            break
    time.sleep(1)

    return playerside, yardline, teamscores, Timeleft

def offense(yardline, teamscores, Timeleft):
    down = 1
    yardsToGo = 10
    while down <= 4 and yardsToGo > 0 and Timeleft > 0:
        # Include the time left in the game status message
        print(f"\nYou are on offense {down} & {yardsToGo}. Time left: {timeformat(Timeleft)}.")
        play_choice = input("Choose your play: Run (1), Pass (2), Kick (3): ")

        if play_choice == "1":  # Run play
            yards_gained = random.randint(-2, 8)  # Randomize yards gained, can be negative
            play_result = "run"
        elif play_choice == "2":  # Pass play
            yards_gained = random.randint(-5, 15)  # Higher variance for pass plays
            play_result = "pass"
        elif play_choice == "3":  # Kick play, simplified as a punt or field goal attempt
            print("Kicking the ball...")
            return "defense", 100 - yardline, teamscores, Timeleft  # Simplified switch to defense

        yardline += yards_gained
        yardsToGo -= yards_gained
        Timeleft -= random.randint(5, 15)  # Reduce time

        # Include the time left in the play result message
        print(f"Play result: {play_result}. Yards gained: {yards_gained}. New yardline: {yardline}. Time left: {timeformat(Timeleft)}.")

        if yardsToGo <= 0:  # Check for first down
            down = 1
            yardsToGo = 10
            print("First down! Time left: {timeformat(Timeleft)}.")
        else:
            down += 1

        if yardline >= 100:  # Touchdown
            print(f"Touchdown! Time left: {timeformat(Timeleft)}.")
            teamscores['Player'] += 7  # Update score
            return "defense", 25, teamscores, Timeleft  # Simplified switch to defense after scoring

    if down > 4:  # Turnover on downs
        print(f"Turnover on downs! Time left: {timeformat(Timeleft)}.")
        return "defense", 100 - yardline, teamscores, Timeleft

    return "offense", yardline, teamscores, Timeleft


        



# We will have this in a while loop so that the user keeps going until they start the game
while userchoice != 2:
    # Now we generate the game for the user, we will come up with a popup of options before they start the game

    print("\nTutorial:")
    print("In order to select an option type the number associated with the option, showcased in the parentheses ex. (1) or (2)")
    print("You will only play offense, defense will be simulated, have fun!")
    print("\nWelcome to football coach! What Would you like to do?")
    userchoice = int(input("See the teams!(1), Start the game (2)"))
    if userchoice == 1:
        print("\nYour Team:")
        for player in Team1Player:
        # Format and print the player's details: Name, Position, Rating
            print("Name:", player.name, "Position:", player.position, "Rating:", player.rating)
        
        print("\nOpponents Team:")
        
        for player in Team2Player:
            # Format and print the player's details: Name, Position, Rating
            print("Name:", player.name, "Position:", player.position, "Rating:", player.rating)
        leavetheloop = input("Press any key when you are ready to leave this menu!") # Just to slow down the user so they have to make an input inorder to leave the sorting function
        
    elif userchoice != 2: # Check if the user actually tried to start the game if they didnt look at the teams, 
        print("ERROR! use a correct input next time!")

# Now we can print out the ovrs for every team
print(f"\nYour Team - Offensive OVR: {team1_offensive_avg}, Defensive OVR: {team1_defensive_avg}, Special Teams OVR: {team1_special_teams_avg}")
print(f"Opponent - Offensive OVR: {team2_offensive_avg}, Defensive OVR: {team2_defensive_avg}, Special Teams OVR: {team2_special_teams_avg}")

# Next we will have a coin flip to decide if the user choses or if the AI choses
# first we shall check what the user would like to call for the coint flip
userinput = int(input("Now it is time for the coin flip, what would you like to call? Heads(1) or Tails(2)"))
playrandomizer = random.randint(1,2)
if userinput == playrandomizer:
    userinput = int(input("You have won the coin flip! Would you like to kick(1) or recieve(2)"))
    if userinput == 1:
        playerside = "defense"
        yardline = kickingfunction(playerside, yardline)
    else:
        playerside = "offense"
        yardline = recivingfunction(playerside, yardline)
else:
    if playrandomizer == 1:
        print("It was Heads, your opponent has elected to recieve")
        playerside = "defense"
        yardline = kickingfunction(playerside, yardline)
    else:
        print("It was Tails, your opponent has elected to recieve")
        playerside = "defense"
        yardline = kickingfunction(playerside, yardline)

while gameisrunning == True:# While this is true we will continue the game,
    if playerside == "offense":
        playerside, yardline, teamscores, Timeleft = offense(yardline, teamscores, Timeleft)
    elif playerside == "defense":
        playerside, yardline, teamscores, Timeleft  = defense(playerside, yardline, teamscores, Timeleft)
    elif playerside == "kicking":
        playerside = "defense"
        yardline = kickingfunction(playerside, yardline)
    elif playerside == "reciving":
        playerside = "offense"
        yardline = recivingfunction(playerside,yardline)
    
        
    

 # End of game
if teamscores['Player'] > teamscores['Computer']:
    print("\nPlayer wins!")
elif teamscores['Player'] < teamscores['Computer']:
    print("\nComputer wins!")
else:
    print("\nIt's a tie!")
