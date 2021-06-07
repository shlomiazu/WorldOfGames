from Live import welcome, load_game, checking_result_of_game, \
    checking_result_of_level, game_selection
import MainScores


# player name
user_name = input("Hello what is your name ?\n")
print(welcome(user_name))
load_game()
game_number = checking_result_of_game()
level = checking_result_of_level()
game_selection(game_number, level)
MainScores.display()
def waht_next():
    while True:
        try:
            choice = int(input(""))
            if 0 < choice <= 3:
                if choice == 1:
                    load_game()
                    game_number = checking_result_of_game()
                    level = checking_result_of_level()
                    game_selection(game_number, level)
                    MainScores.display()
                elif choice == 2:
                    MainScores.call_to_flask()
                elif choice == 3:
                    print("See you next time bye bye ")
                    file = open("Scores.txt", "r+")
                    file.truncate(0)
                    file = open("Scores.txt", 'w')
                    file.write("0")
                    file.close()
                    break
            else:
                print("The option does not exist, Please select for a new game or Look at your Score ")
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

waht_next()







