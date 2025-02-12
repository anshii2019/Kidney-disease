from flask import Flask
# from anshika import create_col
app = Flask(__name__)


#@app.route("/ansh")
@app.route("/anshika")
def name():
    return "hey this is anshika"

if __name__ == "__main__":
    app.run(debug=True)
