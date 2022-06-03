Rock-Paper-Scissors is a simple two-player game where, at a signal, players make figures with their hands, representing a rock, a piece of paper, or a pair of scissors. The winner is determined according to a set of rules. You can find the official rules under the Resources.

 

A brief summary:

If the two players choose the same “character” it’s a tie, and the game repeats
Rock beats Scissors
Paper beats Rock
Scissors beats Paper

One player will be controlled by the computer and the other player controlled by you - the user (i.e CPU vs Player). 

A list stores all possible options:
"R" for "rock", 
"P" for "paper", 
"S" for "scissors".

When the program is run, the user is asked to pick an option between "R", "P" or "S"

If user input is invalid (not amongst our options), an error is printed, and program asks for their input again.

The `choice` function from the inbuilt Python `random` module is used to make a choice for CPU player(computer).
Both players move in the format: `Player (Rock) : CPU (Paper)`

Check both player's moves: 
If there is a winner, print the winner, and the program ends. 
If it's a tie (the computer and player pick the same move), the game is restarted
