import csv
import datetime
from dataclasses import dataclass
from typing import Any


# represents user
@dataclass(frozen=True)
class User:
    user_id: int
    name: str


# represents a game on a specific day
@dataclass(frozen=True)
class Game:
    game_id: int
    game_date: datetime
    solution: str


# represents a guess for the word - corresponds to an entry in the wordle grid
@dataclass(frozen=True)
class Guess:
    user_id: int
    game_id: int
    guess_num: int  # Guess number in grid
    word: str


# represents statistics for a user
@dataclass
class UserStats:
    user_id: int
    user_name: str = None
    num_wins: int = 0
    num_fails: int = 0
    sum_guesses_to_win: int = 0  # sum of guesses made across winning games

    @property
    def num_played(self):
        return self.num_wins + self.num_fails

    @property
    def percent_wins(self):
        """
        percent of games won
        """
        return f"{round(self.num_wins * 100 / self.num_played, 1)}"

    @property
    def avg_guesses_to_win(self):
        """
        average number of guesses in winning a game
        """
        return f"{round(self.sum_guesses_to_win / self.num_wins, 1)}"

    def __str__(self):
        """
        Overwrites __str__ so that it has a printable value
        """
        
        str_val = f"""
        User ID: {self.user_id}, User: {self.user_name.upper()}
        Played: {self.num_played}, Win %: {self.percent_wins}, Average # Guesses to Win: {self.avg_guesses_to_win}
        ***********"""
        return str_val


def read_file(fname: str, item_class: Any):
    """
    Reads a file and returns a list of objects.
    """
    item_list = []
    with open(fname, mode='r') as file:
        reader = csv.DictReader(file)
        for line in reader:
            # converts line read to specified class
            item_list.append(item_class(**line))
    return item_list


if __name__ == "__main__":
    """
    Reads wordle guess files and print statstics for users.
    """

    # read data files into objects
    users = read_file(fname='dataset/users.csv', item_class=User)
    games = read_file(fname='dataset/games.csv', item_class=Game)
    guesses = read_file(fname='dataset/guesses.csv', item_class=Guess)

    # list of user statistics
    all_user_stats = []

    # calculate statistics
    for user in users:
        user_id = user.user_id
        user_stats = UserStats(user_id=user_id, user_name=user.name)

        # iterate across all games
        for game in games:
            game_id = game.game_id

            # the guesses this user made for this game
            user_guesses = list(guess for guess in guesses if
                                guess.user_id == user_id and guess.game_id == game_id)

            # user won this game
            if game.solution in [item.word for item in user_guesses]:
                user_stats.num_wins += 1
                user_stats.sum_guesses_to_win += len(user_guesses)
            # user did not win the game
            else:
                user_stats.num_fails += 1

        all_user_stats.append(user_stats)

    # print statistics for each user
    for user_stats in all_user_stats:
        print(user_stats)
