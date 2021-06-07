from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    try:
        return "Hey there!"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(port=80)
