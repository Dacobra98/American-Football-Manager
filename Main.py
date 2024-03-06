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

# Function to generate a player
def generate_player():  
    # Generate random first and last names
    Generaterandomfirstname = random.randint(0, 20)
    Generaterandomlastname = random.randint(0, 20)
    # Combining first and last names
    name = first_names[Generaterandomfirstname] + ' ' + last_names[Generaterandomlastname]

  
    team = 'Yes'
    position = 'Sure'
    age = 22
    salary = 2000
    
    #Running it through player instance and appending to the list
    player = Player(name, team, position, age, salary)
    players.append(player)

# Generate one player
for i in range(20):
    generate_player()

# Printing player details
for player in players:
       
    print("Name:", player.name, "Team:", player.team, "Position:", player.position,"Age:", player.age,"Salary: $", player.salary)
