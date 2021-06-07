import Utils

def calculate_score (level, result_of_game):
    if result_of_game == True:
        score = (level*3)+5
        Utils.add_score_to_file(score)
        print("Your score is of this game is : " + str(score))
    else:
        print("Your score is of this game is : 0")


