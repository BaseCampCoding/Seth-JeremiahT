# PokemonRPS

PokemonRPS is a game built in Python that is originally modelled after rock, paper, scissors, but with a twist. It has various Pokemon themes in it. 
Instead of rock, paper, scissors, there is fire, grass, ice, rock, and ground.
The player plays against a computer who randomly chooses their type.
Both the player and computer start with 100 health, and after each fight, the loser loses 20 health normally.
There is also a chance for attacks to miss or critical hit. If an attack misses, it does no damage. If it crits, it does double the damage.
It is only possible to miss an attack or get a critical hit if you won the fight.

Once the player reaches 0 health, the game ends and tells you the winner of the match.
It then asks if you would like to play again, and if yes, it restarts the game from the beginning.

## Usage
```python
Here are your choices: 
Fire
Grass
Rock
Ice
Ground

Remember:
    Fire beats grass and ice 
    Grass beats rock and ground
    Rock beats fire and ice
    Ice beats grass and ground
    Ground beats fire and rock!

Please choose from these types: Fire

The computer chose ice! You win!

Player health: 100
Computer health: 80
```
When the game starts, it displays the choices and type matchups.
It then asks for the user input, and determines the winner of the match and subtracts health where it's needed.
```python
The computer chose fire! You lose!

Player health: 0
Computer health: 60

You were defeated by the computer!

Do you want to play again? [Y/N]: Y
```
Once one of the players reaches 0 health, it will ask if you want to play again. If you type "Yes", "yes", "Y", or "y", it will loop the game back to the beginning and add one round to the counter.

# TKPokemonRPS
This is another version of the original PokemonRPS, but this one has been created with a GUI. It performs basically the same game, but has minor changes to inputs.

## Usage
![Initial Display](https://i.imgur.com/xvUxzM9.png)

This is what the opening screen looks like. You have 5 main buttons, one for each type. Each type you click on the button, it will act just like the original program when you input a type.
![Fight Display](https://i.imgur.com/26avpF5.png)

The fights go on until one player reaches 0 health. It also shows when either player gets a critical hit or a miss. Once the match is over and there is a winner, you can press the reset button to start the game over.

# Contributors
Seth Hogue and Jeremiah Tatum

