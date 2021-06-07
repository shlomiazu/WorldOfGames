import requests
from random import randrange

api_key = "9d06f313210e33fb8f3d48b6c02b2848"
url = "http://api.exchangeratesapi.io/v1/latest?access_key="+api_key+"&symbols=USD,ILS"
requests = requests.get(url)
json = requests.json()


def get_money_interval(level):
    # random number for exchange
    mount = randrange(1, 100)
    # get exchange rate
    usd_rate = json.get("rates").get("USD")
    ils_rate = json.get("rates").get("ILS")
    # Convert from United States Dollar (USD) to Israeli Sheqel
    exchange_rate = mount*ils_rate
    return (int(mount), int(exchange_rate))


def get_guess_from_user(mount):
    # get user guess and catch exception
    while True:
        try:
            user_guess = int(input("please exchange" + " " + str(mount) + " " + "to ILS:" + " "))
            break
        except ValueError:
                print("Oops!  That was no valid number.  Try again...")
    return (user_guess)


def play3(level):
    total = get_money_interval(level)
    mount = total[0]
    exchange_ils = total[1]
    user_guess = get_guess_from_user(mount)
    max_option = exchange_ils + (5 - level)
    min_option = exchange_ils - (5 - level)
    if min_option <= user_guess <= max_option:
        print("Well done you guessed it right,\n You're a champion")
        return True
    else:
        print("The amount in shekels is " + str(exchange_ils))
        print("Your guess is " + str(user_guess))
        print("Too bad you could not guess the computer number, please try again")
        return False





