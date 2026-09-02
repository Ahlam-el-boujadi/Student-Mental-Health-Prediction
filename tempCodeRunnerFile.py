from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "Student Depression Prediction"

if __name__ == "__main__":
    app.run(debug=True)