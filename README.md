# Wordle Statistics
A simple program that prints your wordle statistics.

Note: The following is a very simplistic version, there are many ways to improve it.

### The Game
Wordle is a game in which a user makes a set of attempts to guess at a word. 6 attempts are provided, else the user loses the game.

### Description
- `games.csv` has data for each game
- `users.csv` has data for users playing the game
- `guesses.csv` has data for guesses made by users across all the games

The output is some basic statistics for each user.

## Getting Started
Either docker or python has to be installed on your machine

## Executing project

### Python3 version
From the command line, run 
`python wordle_stats.py`

### Docker version
Docker has to be running on your machine. Then execute the following commands

`docker build . -t <image_name>`

`docker run <image_name>`

The output is a list of statistics for each user

### Acknowledgements:
Inspired by NY Times Wordle game.
https://www.nytimes.com/games/wordle/index.html
