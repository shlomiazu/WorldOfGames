import GuessGame
import MemoryGame
import CurrencyRouletteGame
import Score



def welcome(name):
    return "Hello" + " " + name + " " + "and welcome to the World of Games (WoG).\n"\
                                        "Here you can find many cool games to play."


def load_game():
    print("Game List:")
    list_game = {1: "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back",
                 2: "Guess Game - guess a number and see if you chose like the computer",
                 3: "Currency Roulette - try and guess the value of a random amount of USD in ILS"}

    for i in list_game:
        print(i, list_game[i])


def checking_result_of_game():
    while True:
        try:
            game_number = int(input("Please choose a game to play:" + " "))
            if 0 < game_number <= 3:
                break
            else:
               print("The game does not exist, Please select a game from 1-3" + " ")
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    return game_number


def checking_result_of_level():
    while True:
        try:
            level = int(input("Please select the difficulty level between 1-5:" + " "))
            if 0 < level <= 5:
                break
            else:
                print("Please select the difficulty level between 1-5: " + " ")
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    return level


def game_selection(game_number, level):

    if game_number == 2:
        result_of_game = GuessGame.play2(level)
        Score.calculate_score(level, result_of_game)
    elif game_number == 1:
         result_of_game = MemoryGame.play1(level)
         Score.calculate_score(level, result_of_game)
    elif game_number == 3:
        result_of_game = CurrencyRouletteGame.play3(level)
        Score.calculate_score(level, result_of_game)
    else:
        print("jjjjjjjj")
