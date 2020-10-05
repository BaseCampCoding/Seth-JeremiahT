# Pokemon Rock, Paper, Scissors!

## Project Description and Motivation:
- We have decided to make a game of Rock, Paper, Scissors; but with a theme of Pokemon.
- The thought process behind this was that we wanted to try and find something somewhat original to do, but not making it crushingly hard to make for ourselves.
- This will follow the same general rules of Rock, Paper, Scissors (i.e. "This type beats that type"), but themed around Pokemon types (Water, Fire, Grass, etc.)

## Prior Art
There have been many other games like this, where someone takes Rock, Paper, Scissors, and adds their own twist/theme to it. We decided to go with Pokemon for our theme because it provides a simple type comparison system, much like Rock, Paper, Scissors, and it can easily be expanded to be more complex if we wanted.

## Core User Workflows
- User choices:
  - Program displays the different choices and matchups of the types to the user.
  - User chooses from the given choices.
- "Combat":
  - Opponent choice generation: At the beginning of each round of RPS, the AI will randomly choose a type from the list.
  - Match determination: Once both sides have chosen a type, the program will determine the winner of the match, and add the result to the score.
- End of Match/Rinse and Repeat:
  - Once the result is determined, the score is added to the scoreboard, and the match resets.
  - This loop keeps going until the user types quit.
