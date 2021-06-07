from flask import Flask

app = Flask(__name__)


@app.route('/')
def display_Score():
    f = open("Scores.txt", "r")
    score = int(f.readline())
    f.close()
    try:
        return 'Your score is : ' + str(score)
    except Exception as e:
        return str(e)


def display():
    print("Thanks for playing the word of game :)\n"
           "What next:")
    display = {1: "Pick a new game.",
               2: "Look at your Score",
               3: "Don't want to play "}
    for i in display:
        print(i, display[i])


def call_to_flask():
    app.run(port=80)
