import random
from colorama import Fore
from colorama import Style

choices = ("Fire", "Grass", "Rock", "Ice", "Ground")
fireOptions = ('Fire', 'fire', 'F', 'f')
grassOptions = ('Grass', 'grass', 'Gra', 'gra')
rockOptions = ('Rock', 'rock', 'R', 'r')
iceOptions = ('Ice', 'ice', 'I', 'i')
groundOptions = ('Ground', 'ground', 'Gro', 'gro')
yesOptions = ('Yes', 'yes', 'Y', 'y')
zippedOptions = list(zip(fireOptions, grassOptions, rockOptions, iceOptions, groundOptions))
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.LIGHTBLUE_EX, Fore.LIGHTYELLOW_EX]
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
    for item in zippedOptions:
        if choice in item:
            return True

def userSettings(): # Function to determine the player's type choice.
    playerChoice = ''
    while not validType(playerChoice):
        playerChoice = input("Please choose from these types: ")
        if not validType(playerChoice):
            print("Please choose a valid type!\n")
    return playerChoice

def comSettings(): # Function to determine the computer's type choice.
    comChoice = random.choice(choices)
    return comChoice

# Placeholder variables until health mechanism is finished.
def playerDamage():
    playerDamage = 20
    missAttack = random.randint(1, 5)
    if missAttack == 1:
        playerDamage = 0
        print("\nYour attack missed!")
    return playerDamage

def comDamage():
    comDamage = 20
    missAttack = random.randint(1, 5)
    if missAttack == 1:
        comDamage = 0
        print("\nThe computer's attack missed!")
    return comDamage

   
def main():
    playerHealth = 100
    comHealth = 100
    print("Here are your choices: ") # Lists the options available to the user.
    count = 0
    for item in choices:
        print(f"{colors[count]}{item}{Style.RESET_ALL}")
        count += 1
    # Prints the type matchups with matching colors.
    print(f'''\nRemember:
    {Fore.RED}Fire{Style.RESET_ALL} beats {Fore.GREEN}grass{Style.RESET_ALL} and {Fore.BLUE}ice {Style.RESET_ALL}
    {Fore.GREEN}Grass{Style.RESET_ALL} beats {Fore.YELLOW}rock{Style.RESET_ALL} and {Fore.LIGHTYELLOW_EX}ground
    {Fore.YELLOW}Rock{Style.RESET_ALL} beats {Fore.RED}fire{Style.RESET_ALL} and {Fore.BLUE}ice{Style.RESET_ALL}
    {Fore.BLUE}Ice{Style.RESET_ALL} beats {Fore.GREEN}grass{Style.RESET_ALL} and {Fore.LIGHTYELLOW_EX}ground{Style.RESET_ALL}
    {Fore.LIGHTYELLOW_EX}Ground{Style.RESET_ALL} beats {Fore.RED}fire{Style.RESET_ALL} and {Fore.YELLOW}rock{Style.RESET_ALL}!''')
    while playerHealth > 0 and comHealth > 0: # Main portion of RPS game
        print("")
        userChoice = userSettings() # Runs the previously defined function
        comChoice = comSettings() # Runs the previously defined function
        print("")

        # If statements to determine the winner of the match, adds the result to score.
        if userChoice in fireOptions:
            if comChoice == 'Fire':
                print(f"You both chose {Fore.RED}fire{Style.RESET_ALL}! It's a tie!")
                playerHealth -= 0
                comHealth -= 0
            elif comChoice == 'Ground':
                print(f"The computer chose {Fore.LIGHTYELLOW_EX}ground{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
            elif comChoice == 'Rock':
                print(f"The computer chose {Fore.YELLOW}rock{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
            elif comChoice == 'Grass':
                print(f"The computer chose {Fore.GREEN}grass{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()
            elif comChoice == 'Ice':
                print(f"The computer chose {Fore.BLUE}ice{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()

        elif userChoice in grassOptions:
            if comChoice == 'Grass':
                print(f"You both chose {Fore.GREEN}grass{Style.RESET_ALL}! It's a tie!")
                playerHealth -= 0
                comHealth -= 0
            elif comChoice == 'Fire':
                print(f"The computer chose {Fore.RED}fire{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
            elif comChoice == 'Ice':
                print(f"The computer chose {Fore.BLUE}ice{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
            elif comChoice == 'Rock':
                print(f"The computer chose {Fore.YELLOW}rock{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()
            elif comChoice == 'Ground':
                print(f"The computer chose {Fore.LIGHTYELLOW_EX}ground{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()
        
        elif userChoice in rockOptions:
            if comChoice == 'Rock':
                print(f"You both chose {Fore.YELLOW}rock{Style.RESET_ALL}! It's a tie!")
                playerHealth -= 0
                comHealth -= 0
            elif comChoice == 'Grass':
                print(f"The computer chose {Fore.GREEN}grass{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
            elif comChoice == "Ground":
                print(f"The computer chose {Fore.LIGHTYELLOW_EX}ground{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
            elif comChoice == 'Fire':
                print(f"The computer chose {Fore.RED}fire{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()
            elif comChoice == 'Ice':
                print(f"The computer chose {Fore.BLUE}ice{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()

        elif userChoice in iceOptions:
            if comChoice == 'Ice':
                print(f"You both chose {Fore.BLUE}ice{Style.RESET_ALL}! It's a tie!")
                playerHealth -= 0
                comHealth -= 0
            elif comChoice == 'Fire':
                print(f"The computer chose {Fore.RED}fire{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
            elif comChoice == 'Rock':
                print(f"The computer chose {Fore.YELLOW}rock{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
            elif comChoice == 'Grass':
                print(f"The computer chose {Fore.GREEN}grass{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()
            elif comChoice == 'Ground':
                print(f"The computer chose {Fore.LIGHTYELLOW_EX}ground{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()

        elif userChoice in groundOptions:
            if comChoice == 'Ground':
                print(f"You both chose {Fore.LIGHTYELLOW_EX}ground{Style.RESET_ALL}! It's a tie!")
                playerHealth -= 0
                comHealth -= 0
            elif comChoice == 'Grass':
                print(f"The computer chose {Fore.GREEN}grass{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
            elif comChoice == 'Ice':
                print(f"The computer chose {Fore.BLUE}ice{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
            elif comChoice == 'Fire':
                print(f"The computer chose {Fore.RED}fire{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()
            elif comChoice == 'Rock':
                print(f"The computer chose {Fore.YELLOW}rock{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()
        # Displays the amount of wins for the player and computer.
        print("")
        print(f"Player health: {playerHealth}")
        print(f"Computer health: {comHealth}")
        print("")

        if playerHealth == 0:
            print("You were defeated by the computer!")
        elif comHealth == 0:
            print("You defeated the computer!")

main()

# Asks the user if they want to play again, if 'y', the game loops back. Otherwise, the program ends.
while True:
    playAgain = input("Do you want to play again? [Y/N]: ")
    if playAgain in yesOptions:
        roundNum += 1
        print(f"Round {roundNum}")
        main()
    else:
        print("I hope you had fun!")
        break