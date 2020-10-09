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
    >>> validType("Electric")
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

def playerDamage(): # Shows the damage given if the player wins, with the chance of missing.
    playerDamage = 20
    missAttack = random.randint(1, 5)
    if missAttack == 1:
        playerDamage = 0
        print("\nYour attack missed!")
    critAttack = random.randint(1, 5)
    if playerDamage != 0 and critAttack == 1:
        playerDamage *= 2
        print("You got a critical hit!")
    return playerDamage

def comDamage(): # Shows the damage given if the computer wins, with the chance of missing.
    comDamage = 20
    missAttack = random.randint(1, 5)
    if missAttack == 1:
        comDamage = 0
        print("\nThe computer's attack missed!")
    critAttack = random.randint(1, 5)
    if comDamage != 0 and critAttack == 1:
        comDamage *= 2
        print("The computer got a critical hit!")
    return comDamage

   
def main(): # Main function of RPS game
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
    
    while playerHealth > 0 and comHealth > 0:
        print("")
        userChoice = userSettings() # Runs the previously defined function
        comChoice = comSettings() # Runs the previously defined function
        print("")

        # If statements to determine the winner of the match, subtracts health from losers total health.
        if userChoice in fireOptions:
            if comChoice == 'Fire':
                print(f"You both chose {Fore.RED}fire{Style.RESET_ALL}! It's a tie!")
                playerHealth -= 0
                comHealth -= 0
            elif comChoice == 'Ground':
                print(f"The computer chose {Fore.LIGHTYELLOW_EX}ground{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
                playerHealth = max(playerHealth, 0)
            elif comChoice == 'Rock':
                print(f"The computer chose {Fore.YELLOW}rock{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
                playerHealth = max(playerHealth, 0)
            elif comChoice == 'Grass':
                print(f"The computer chose {Fore.GREEN}grass{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()
                comHealth = max(comHealth, 0)
            elif comChoice == 'Ice':
                print(f"The computer chose {Fore.BLUE}ice{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()
                comHealth = max(comHealth, 0)

        elif userChoice in grassOptions:
            if comChoice == 'Grass':
                print(f"You both chose {Fore.GREEN}grass{Style.RESET_ALL}! It's a tie!")
                playerHealth -= 0
                comHealth -= 0
            elif comChoice == 'Fire':
                print(f"The computer chose {Fore.RED}fire{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
                playerHealth = max(playerHealth, 0)
            elif comChoice == 'Ice':
                print(f"The computer chose {Fore.BLUE}ice{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
                playerHealth = max(playerHealth, 0)
            elif comChoice == 'Rock':
                print(f"The computer chose {Fore.YELLOW}rock{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()
                comHealth = max(comHealth, 0)
            elif comChoice == 'Ground':
                print(f"The computer chose {Fore.LIGHTYELLOW_EX}ground{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()
                comHealth = max(comHealth, 0)
        
        elif userChoice in rockOptions:
            if comChoice == 'Rock':
                print(f"You both chose {Fore.YELLOW}rock{Style.RESET_ALL}! It's a tie!")
                playerHealth -= 0
                comHealth -= 0
            elif comChoice == 'Grass':
                print(f"The computer chose {Fore.GREEN}grass{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
                playerHealth = max(playerHealth, 0)
            elif comChoice == "Ground":
                print(f"The computer chose {Fore.LIGHTYELLOW_EX}ground{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
                playerHealth = max(playerHealth, 0)
            elif comChoice == 'Fire':
                print(f"The computer chose {Fore.RED}fire{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()
                comHealth = max(comHealth, 0)
            elif comChoice == 'Ice':
                print(f"The computer chose {Fore.BLUE}ice{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()
                comHealth = max(comHealth, 0)

        elif userChoice in iceOptions:
            if comChoice == 'Ice':
                print(f"You both chose {Fore.BLUE}ice{Style.RESET_ALL}! It's a tie!")
                playerHealth -= 0
                comHealth -= 0
            elif comChoice == 'Fire':
                print(f"The computer chose {Fore.RED}fire{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
                playerHealth = max(playerHealth, 0)
            elif comChoice == 'Rock':
                print(f"The computer chose {Fore.YELLOW}rock{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
                playerHealth = max(playerHealth, 0)
            elif comChoice == 'Grass':
                print(f"The computer chose {Fore.GREEN}grass{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()
                comHealth = max(comHealth, 0)
            elif comChoice == 'Ground':
                print(f"The computer chose {Fore.LIGHTYELLOW_EX}ground{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()
                comHealth = max(comHealth, 0)

        elif userChoice in groundOptions:
            if comChoice == 'Ground':
                print(f"You both chose {Fore.LIGHTYELLOW_EX}ground{Style.RESET_ALL}! It's a tie!")
                playerHealth -= 0
                comHealth -= 0
            elif comChoice == 'Grass':
                print(f"The computer chose {Fore.GREEN}grass{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
                playerHealth = max(playerHealth, 0)
            elif comChoice == 'Ice':
                print(f"The computer chose {Fore.BLUE}ice{Style.RESET_ALL}! You lose!")
                playerHealth -= comDamage()
                playerHealth = max(playerHealth, 0)
            elif comChoice == 'Fire':
                print(f"The computer chose {Fore.RED}fire{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()
                comHealth = max(comHealth, 0)
            elif comChoice == 'Rock':
                print(f"The computer chose {Fore.YELLOW}rock{Style.RESET_ALL}! You win!")
                comHealth -= playerDamage()
                comHealth = max(comHealth, 0)

        # Displays the amount of health that the player and computer have left.
        print("")
        print(f"Player health: {playerHealth}")
        print(f"Computer health: {comHealth}")
        print("")

        if playerHealth <= 0:
            print("You were defeated by the computer!\n")
        elif comHealth <= 0:
            print("You defeated the computer!\n")

main()

# Asks the user if they want to play again, if 'y', the game loops back. Otherwise, the program ends.
while True:
    playAgain = input("Do you want to play again? [Y/N]: ")
    if playAgain in yesOptions:
        roundNum += 1
        print(f"Round {roundNum}")
        main()
    else:
        print("\nI hope you had fun!")
        break
