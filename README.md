# Matching Game
A small command line game I made for a university assignment.

## How To Play
After selecting the number of players and the difficulty level, each player will have to select two cards. If those cards are a match,
the player will be awarded with an amount of points. Afterwards, it's the next player's turn. The above process repeats itself until no more cards are closed.

### Points
The point system works like this:
```
Ace cards(A) reward 1 point.
1..10 cards have a value equal to their number.
J, Q & K cards reward 10 points.
```

### Combinations
The game features three card combinations that result in unique events. Selecting two J cards, allows the current player to
play again. Selecting two K cards, results in the next player losing his turn. Finally, guessing a K and a Q card(in any order)
gives the current player the ability to choose a third card. If the third card does not result in any match, then all three cards will be hidden again.
Otherwise, only the card that doesn't match will be hidden.

## Built With
All you need to run this game is a command line and [Python version 3](https://www.python.org/).
Run the following command in a UNIX terminal and the game should start.
```
$ python3 main.py
```

## Notes
For presentation purposes, I reveal all cards one time before the game starts.

## License
This software is licensed under the MIT License. For more details check [LICENSE.txt](LICENSE.txt).
