import Utils
from flask import Flask

app = Flask(__name__)

def readline():
    f = open("Scores.txt", "r")
    score = int(f.readline())
    f.close()
    return str(score)



def set_html(score):
    html = f"""<html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1 id="description">The score is <span id="score">{score}</span></h1>
        </body>
    </html>"""
    return html

def set_html_error():
    html = f"""<html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1 id="description" >Error <span id="score" style="color:red">{Utils.BAD_RETURN_CODE}</span></h1>
            </body>
    </html>"""
    return html

@app.errorhandler(Exception)
def server_error(erorr):
    app.logger.exception(erorr)
    return set_html_error(), int(Utils.BAD_RETURN_CODE)

@app.route("/")
def call_to_flask():
    score = readline()
    return set_html(score)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8777)



