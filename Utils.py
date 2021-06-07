import os
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


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

def Screen_cleaner():
    os.system('cls')
