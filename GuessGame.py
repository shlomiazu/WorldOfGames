from time import sleep
import random


def generate_number(level):
    secret_number = random.randint(1, level)
    return secret_number


def get_guess_from_user(level):
    while True:
        level = str(level + 1)
        try:
            user_choice = int(input("Please guess a number From 1 to " + level + " "))
            if 0 < user_choice <= int(level):
                break
            else:
                print("The number you set is not between 1 to " + level)
        except ValueError:
            print("please enter a valid number ")

    return user_choice


def compare_results(secret_number, user_choice):
    if user_choice == secret_number:
       return True
    else:
       return False


def play2(level):

    print('\n' + '\n Hello and welcome to the game "Guess the Number."\n' 
          'In this game you will need to guess the number that was\n'
          ' chosen by the computer based on the difficulty you selected. Good luck!\n')
    sleep(4)
    print("Computer guess a number")
    a = 'THINKING...'
    for i in range(10):
        print(a[i], sep=' ', end=' ', flush=True),
        sleep(0.5)
    print("ok i am ready")
    secret_number = generate_number(level)
    user_choice = int(get_guess_from_user(level))
    if compare_results(secret_number, user_choice):
        print("Well done you guessed it right,\n You're a champion")
        return True
    else:
        print("the computer number was " + str(secret_number))
        print("Your number was " + str(user_choice))
        print("Too bad you could not guess the computer number, please try again")
        return False


