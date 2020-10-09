import random
import tkinter as tk 

choices = ("Fire", "Grass", "Rock", "Ice", "Ground")
playerHealth = 100
comHealth = 100
winner = ''
playerCrit = ''
comCrit = ''
playerMiss = ''
comMiss = ''
comGameWinner = ''
playerGameWinner = ''

class menu: #Puts all functions under the same class.
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

    def resetGame(self): # Function to reset the game.
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

    def random_computer_choice(self): # Computer randomly chooses a type.
        return random.choice(choices) 

    def result(self, human_choice,com_choice): # Determines the winner of the fight.
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
            if userChoice == "Fire":
                    if comChoice == 'Fire':
                        playerHealth -= 0
                        comHealth -= 0
                        winner = 'It was a tie!'
                    elif comChoice == 'Ground':
                        playerHealth -= self.comDamage()
                        playerHealth = max(playerHealth, 0)
                        winner = 'Computer'
                    elif comChoice == 'Rock':
                        playerHealth -= self.comDamage()
                        playerHealth = max(playerHealth, 0)
                        winner = 'Computer'
                    elif comChoice == 'Grass':
                        comHealth -= self.playerDamage()
                        comHealth = max(comHealth, 0)
                        winner = 'You'
                    elif comChoice == 'Ice':
                        comHealth -= self.playerDamage()
                        comHealth = max(comHealth, 0)
                        winner = 'You'

            elif userChoice == "Grass":
                if comChoice == 'Grass':
                    playerHealth -= 0
                    comHealth -= 0
                    winner = 'It was a tie!'
                elif comChoice == 'Fire':
                    playerHealth -= self.comDamage()
                    playerHealth = max(playerHealth, 0)
                    winner = 'Computer'
                elif comChoice == 'Ice':
                    playerHealth -= self.comDamage()
                    max(playerHealth, 0)
                    winner = 'Computer'
                elif comChoice == 'Rock':
                    comHealth -= self.playerDamage()
                    comHealth = max(comHealth, 0)
                    winner = 'You'
                elif comChoice == 'Ground':
                    comHealth -= self.playerDamage()
                    comHealth = max(comHealth, 0)
                    winner = 'You'
            
            elif userChoice == "Rock":
                if comChoice == 'Rock':
                    playerHealth -= 0
                    comHealth -= 0
                    winner = 'It was a tie!'
                elif comChoice == 'Grass':
                    playerHealth -= self.comDamage()
                    playerHealth = max(playerHealth, 0)
                    winner = 'Computer'
                elif comChoice == "Ground":
                    playerHealth -= self.comDamage()
                    playerHealth = max(playerHealth, 0)
                    winner = 'Computer'
                elif comChoice == 'Fire':
                    comHealth -= self.playerDamage()
                    comHealth = max(comHealth, 0)
                    winner = 'You'
                elif comChoice == 'Ice':
                    comHealth -= self.playerDamage()
                    comHealth = max(comHealth, 0)
                    winner = 'You'

            elif userChoice == "Ice":
                if comChoice == 'Ice':
                    playerHealth -= 0
                    comHealth -= 0
                    winner = 'It was a tie!'
                elif comChoice == 'Fire':
                    playerHealth -= self.comDamage()
                    playerHealth = max(playerHealth, 0)
                    winner = 'Computer'
                elif comChoice == 'Rock':
                    playerHealth -= self.comDamage()
                    playerHealth = max(playerHealth, 0)
                    winner = 'Computer'
                elif comChoice == 'Grass':
                    comHealth -= self.playerDamage()
                    comHealth = max(comHealth, 0)
                    winner = 'You'
                elif comChoice == 'Ground':
                    comHealth -= self.playerDamage()
                    comHealth = max(comHealth, 0)
                    winner = 'You'

            elif userChoice == "Ground":
                if comChoice == 'Ground':
                    playerHealth -= 0
                    comHealth -= 0
                    winner = 'It was a tie!'
                elif comChoice == 'Grass':
                    playerHealth -= self.comDamage()
                    playerHealth = max(playerHealth, 0)
                    winner = 'Computer'
                elif comChoice == 'Ice':
                    playerHealth -= self.comDamage()
                    playerHealth = max(playerHealth, 0)
                    winner = 'Computer'
                elif comChoice == 'Fire':
                    comHealth -= self.playerDamage()
                    comHealth = max(comHealth, 0)
                    winner = 'You'
                elif comChoice == 'Rock':
                    comHealth -= self.playerDamage()
                    comHealth = max(comHealth, 0)
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
        

    def fire(self): #
        global userChoice
        global comChoice
        userChoice ='Fire'
        comChoice = self.random_computer_choice()
        self.result(userChoice ,comChoice)

    def grass(self):
        global userChoice
        global comChoice
        userChoice='Grass'
        comChoice=self.random_computer_choice()
        self.result(userChoice,comChoice)

    def ice(self):
        global userChoice
        global comChoice
        userChoice='Ice'
        comChoice=self.random_computer_choice() 
        self.result(userChoice,comChoice)

    def rock(self):
        global userChoice
        global comChoice
        userChoice= 'Rock'
        comChoice=self.random_computer_choice() 
        self.result(userChoice,comChoice)

    def ground(self):
        global userChoice
        global comChoice
        userChoice='Ground'
        comChoice=self.random_computer_choice() 
        self.result(userChoice,comChoice) 


menu()