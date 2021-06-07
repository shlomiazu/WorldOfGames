from random import randrange
import os
from time import sleep

def generate_sequence(level):
    group_number = [randrange(1, 101) for i in range(level+1)]
    return group_number



def get_list_from_user():
    while True:
        try:
            input_string = input("Enter the number that you remember  separated by space: ")
            user_list = input_string.split()
            # convert each item to int type
            for i in range(len(user_list)):
                user_list[i] = int(user_list[i])
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    return user_list


def checking_list_equal(arr1, arr2, len_arr1, len_arr2):

    if len_arr1 != len_arr2:
        return False
    arr1.sort()
    arr2.sort()
    for i in range(0, len_arr1 - 1):
        if arr1[i] != arr2[i]:
            return False
        return True

def play1(level):
    print('\n' + '\n Hello and welcome to the game "Lets see your memory."\n'
                 'In this game you will need to remember  the number that was\n'
                 'display by the computer based on the difficulty you selected. Good luck!\n')
    sleep(4)
    print("Be ready :-)")
    arr1 = generate_sequence(level)
    print(arr1)
    sleep(5)
    os.system('cls')
    arr2 = get_list_from_user()
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    result = checking_list_equal(arr1, arr2, len_arr1, len_arr2)
    if(result):
        print("Well done you remember it right,\n You're a champion")
        return True
    else:
        print("the computer number was " + str(arr1))
        print("Your number was " + str(arr2))
        print("Too bad you could not guess the computer number, please try again")
        return False
