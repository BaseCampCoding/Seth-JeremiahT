import random
from colorama import Fore
from colorama import Style

choices = ["Fire", "Water", "Grass", "Electric"]
fireOptions = ['Fire', 'fire', 'F', 'f']
waterOptions = ['Water', 'water', 'W', 'w']
grassOptions = ['Grass', 'grass', 'G', 'g']
electricOptions = ['Electric', 'electric', 'E', 'e']
yesOptions = ['Yes', 'yes', 'Y', 'y']
colors = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW]
playerWins = 0
comWins = 0
roundNum = 1
def validType(choice: str) -> bool: # Checks if the user's choice is valid.
    ''' Returns True if type is in the choices list. Returns False otherwise.

    >>> validType("Fire")
    True
    >>> validType("Grass")
    True
    >>> validType("Rock")
    False
    '''
    return choice in fireOptions or choice in waterOptions or choice in grassOptions or choice in electricOptions

def userSettings(): # Function to determine the player's type choice.
    playerChoice = ''
    while not validType(playerChoice):
        playerChoice = input("Please choose from these types: ")
        if playerChoice not in choices:
            print("Please choose a valid type!\n")
    return playerChoice

def comSettings(): # Function to determine the computer's type choice.
    comChoice = random.choice(choices)
    return comChoice

print("Here are your choices: ") # Lists the options available to the user.
count = 0
for item in choices:
    print(f"{colors[count]}{item}{Style.RESET_ALL}")
    count += 1
print("\nRemember, fire beats grass, grass beats water and electric, water beats fire, and electric beats fire and water!\n")

while True: # Main portion of RPS game
    print("")
    userChoice = userSettings() # Runs the previously defined function
    comChoice = comSettings() # Runs the previously defined function
    print("")

    # If statements to determine the winner of the match, adds the result to score.
    if userChoice in fireOptions:
        if comChoice == 'Fire':
            print("You both chose fire! It's a tie!")
            playerWins += 0
        elif comChoice == 'Water':
            print("The computer chose water! You lose!")
            comWins += 1
        elif comChoice == 'Grass':
            print("The computer choose grass! You win!")
            playerWins += 1
        elif comChoice == 'Electric':
            print("The computer choose electric! You lose!")
            comWins+=1

    elif userChoice in waterOptions:
        if comChoice == 'Water':
            print("You both chose water! It's a tie!")
            playerWins += 0
        elif comChoice == 'Grass':
            print("The computer chose grass! You lose!")
            comWins += 1
        elif comChoice == 'Fire':
            print("The computer choose fire! You win!")
            playerWins += 1
        elif comChoice == 'Electric':
            print("The computer choose electric! You lose!")
            comWins+=1

    elif userChoice in grassOptions:
        if comChoice == 'Grass':
            print("You both chose grass! It's a tie!")
            playerWins += 0
        elif comChoice == 'Fire':
            print("The computer chose fire! You lose!")
            comWins += 1
        elif comChoice == 'Water':
            print("The computer choose water! You win!")
            playerWins += 1
        elif comChoice == 'Electric':
            print("The computer choose electric! You win!")
            playerWins+=1
    elif userChoice in electricOptions:
        if comChoice == 'Electric':
            print("The computer choose electric! It's a tie!")
            playerWins +=0
        elif comChoice == 'Grass':
            print("The computer choose grass! You lose!")
            comWins+=1
        elif comChoice == 'Fire':
            print("The computer choose fire! You win!")
            playerWins+=1
        elif comChoice == 'Water':
            print("The computer choose water! You win!")
            playerWins+=1

    # Displays the amount of wins for the player and computer.
    print("")
    print(f"Player wins: {playerWins}")
    print(f"Computer wins: {comWins}")
    print("")

    # Asks the user if they want to play again, if 'y', the game loops back. Otherwise, the program ends.
    playAgain = input("Do you want to play again? [Y/N]")
    if playAgain in yesOptions:
        roundNum += 1
        print(f"Round {roundNum}")
    else:
        print("I hope you had fun!")
        break
