import random
import tkinter as tk 
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
playerHealth = 100
comHealth = 100
winner = ''
playerCrit = ''
comCrit = ''
playerMiss = ''
comMiss = ''
comGameWinner = ''
playerGameWinner = ''

class menu:
    def __init__(self):
        self.game = tk.Tk()
        self.game.geometry("600x520")
        self.game.title("Rock Paper Scissors Game")
        button1 = tk.Button(text=" Fire ",bg="red", height=2, width=20, command=self.fire)
        button1.grid(column=0,row=1)
        button2 = tk.Button(text=" Grass ",bg="green", height=2, width=20, command=self.grass)
        button2.grid(column=0,row=2)
        button3 = tk.Button(text=" Ice ",bg="lightblue", height=2, width=20 ,command=self.ice)
        button3.grid(column=0,row=3)
        button4 = tk.Button(text=" Rock ",bg="brown", height=2, width=20, command=self.rock)
        button4.grid(column=0,row=4)
        button5 = tk.Button(text=" Ground ",bg="yellow", height=2, width=20, command=self.ground)
        button5.grid(column=0,row=5)
        playAgainText = tk.Label(text="Reset?")
        playAgainText.grid(column=0, row=7)
        button6 = tk.Button(text="Yes", height=2, width=5, command=self.resetGame)
        button6.grid(column=0, row=8)
        self.game.mainloop()

    def playerDamage(self): # Shows the damage given if the player wins, with the chance of missing.
        playerDamage = 20
        global playerMiss
        global playerCrit
        missAttack = random.randint(1, 5)
        if missAttack == 1:
            playerDamage = 0
            print("\nYour attack missed!")
            playerMiss = 'Your attack missed!'
        critAttack = random.randint(1, 5)
        if playerDamage != 0 and critAttack == 1:
            playerDamage *= 2
            print("You got a critical hit!")
            playerCrit = 'You got a critical hit!'
        return playerDamage

    def resetGame(self):
        global playerHealth
        global comHealth
        self.game.destroy()
        playerHealth = 100
        comHealth = 100
        menu()

    def comDamage(self): # Shows the damage given if the computer wins, with the chance of missing.
        comDamage = 20
        global comMiss
        global comCrit
        missAttack = random.randint(1, 5)
        if missAttack == 1:
            comDamage = 0
            print("\nThe computer's attack missed!")
            comMiss = "The computer's attack missed!"
        critAttack = random.randint(1, 5)
        if comDamage != 0 and critAttack == 1:
            comDamage *= 2
            print("The computer got a critical hit!")
            comCrit = 'The computer got a critical hit!'
        return comDamage

    def random_computer_choice(self):
        return random.choice(choices) 

    def result(self, human_choice,com_choice):
        global userChoice
        global userChoice
        global playerHealth
        global comHealth
        global winner
        global playerCrit
        global playerMiss
        global comCrit
        global comMiss
        global playerGameWinner
        global comGameWinner
        if playerHealth > 0 and comHealth > 0:
            if userChoice in fireOptions:
                    if comChoice == 'Fire':
                        playerHealth -= 0
                        comHealth -= 0
                        winner = 'It was a tie!'
                    elif comChoice == 'Ground':
                        playerHealth -= self.comDamage()
                        winner = 'Computer'
                    elif comChoice == 'Rock':
                        playerHealth -= self.comDamage()
                        winner = 'Computer'
                    elif comChoice == 'Grass':
                        comHealth -= self.playerDamage()
                        winner = 'You'
                    elif comChoice == 'Ice':
                        comHealth -= self.playerDamage()
                        winner = 'You'

            elif userChoice in grassOptions:
                if comChoice == 'Grass':
                    playerHealth -= 0
                    comHealth -= 0
                    winner = 'It was a tie!'
                elif comChoice == 'Fire':
                    playerHealth -= self.comDamage()
                    winner = 'Computer'
                elif comChoice == 'Ice':
                    playerHealth -= self.comDamage()
                    winner = 'Computer'
                elif comChoice == 'Rock':
                    comHealth -= self.playerDamage()
                    winner = 'You'
                elif comChoice == 'Ground':
                    comHealth -= self.playerDamage()
                    winner = 'You'
            
            elif userChoice in rockOptions:
                if comChoice == 'Rock':
                    playerHealth -= 0
                    comHealth -= 0
                    winner = 'It was a tie!'
                elif comChoice == 'Grass':
                    playerHealth -= self.comDamage()
                    winner = 'Computer'
                elif comChoice == "Ground":
                    playerHealth -= self.comDamage()
                    winner = 'Computer'
                elif comChoice == 'Fire':
                    comHealth -= self.playerDamage()
                    winner = 'You'
                elif comChoice == 'Ice':
                    comHealth -= self.playerDamage()
                    winner = 'You'

            elif userChoice in iceOptions:
                if comChoice == 'Ice':
                    playerHealth -= 0
                    comHealth -= 0
                    winner = 'It was a tie!'
                elif comChoice == 'Fire':
                    playerHealth -= self.comDamage()
                    winner = 'Computer'
                elif comChoice == 'Rock':
                    playerHealth -= self.comDamage()
                    winner = 'Computer'
                elif comChoice == 'Grass':
                    comHealth -= self.playerDamage()
                    winner = 'You'
                elif comChoice == 'Ground':
                    comHealth -= self.playerDamage()
                    winner = 'You'

            elif userChoice in groundOptions:
                if comChoice == 'Ground':
                    playerHealth -= 0
                    comHealth -= 0
                    winner = 'It was a tie!'
                elif comChoice == 'Grass':
                    playerHealth -= self.comDamage()
                    winner = 'Computer'
                elif comChoice == 'Ice':
                    playerHealth -= self.comDamage()
                    winner = 'Computer'
                elif comChoice == 'Fire':
                    comHealth -= self.playerDamage()
                    winner = 'You'
                elif comChoice == 'Rock':
                    comHealth -= self.playerDamage()
                    winner = 'You'
            text_area = tk.Text(master=self.game,height=12,width=60,bg="#FFFF99")
            text_area.grid(column=0,row=6)
            if playerHealth <= 0:
                comGameWinner = 'The computer is the winner of the game!'
            elif comHealth <= 0:
                playerGameWinner = 'You are the winner of the game!'
            answer = '''
            Your Choice: {uc}
            Computer's Choice : {cc}
            Winner: {w}
            {pcr}{cpr}
            {pm}{cm}
            Your Health : {u}
            Computer Health : {c}

            {pgw}{cgw}
            
            '''.format(uc=userChoice,cc=comChoice,w=winner,pcr= playerCrit, cpr=comCrit, pm=playerMiss, cm=comMiss, u=playerHealth,c=comHealth, pgw=playerGameWinner, cgw=comGameWinner)
            text_area.insert(tk.END,answer)
            playerCrit = ''
            playerMiss = ''
            comCrit = ''
            comMiss = ''
            playerGameWinner = ''
            comGameWinner = ''
        

    def fire(self):
        global userChoice
        global comChoice
        userChoice ='fire'
        comChoice = self.random_computer_choice()
        self.result(userChoice ,comChoice)

    def grass(self):
        global userChoice
        global comChoice
        userChoice='grass'
        comChoice=self.random_computer_choice()
        self.result(userChoice,comChoice)

    def ice(self):
        global userChoice
        global comChoice
        userChoice='ice'
        comChoice=self.random_computer_choice() 
        self.result(userChoice,comChoice)

    def rock(self):
        global userChoice
        global comChoice
        userChoice= 'rock'
        comChoice=self.random_computer_choice() 
        self.result(userChoice,comChoice)

    def ground(self):
        global userChoice
        global comChoice
        userChoice='ground'
        comChoice=self.random_computer_choice() 
        self.result(userChoice,comChoice) 


menu()