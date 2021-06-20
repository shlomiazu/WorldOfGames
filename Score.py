import os


def calculate_score (level, result_of_game):
    if result_of_game == True:
        score = (level*3)+5
        add_score_to_file(score)
        print("Your score is of this game is : " + str(score))
    else:
        print("Your score of this game is : 0")


def add_score_to_file (score):
    if os.stat("Scores.txt").st_size == 0:
        sum = 0
        total = str(sum + score)
        SCORES_FILE_NAME = open("Scores.txt", 'w')
        SCORES_FILE_NAME.write(total)
        SCORES_FILE_NAME.close()
    else:
        f = open("Scores.txt", "r")
        sum = int(f.readline())
        f.close()
        total = str(sum + score)
        SCORES_FILE_NAME = open("Scores.txt", 'w')
        SCORES_FILE_NAME.write(total)
        SCORES_FILE_NAME.close()