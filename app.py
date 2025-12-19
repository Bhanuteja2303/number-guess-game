from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Generate random number once
number = random.randint(1, 10)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        guess = int(request.form["guess"])

        if guess < number:
            message = "Too low!"
        elif guess > number:
            message = "Too high!"
        else:
            message = "Correct! You guessed the number 🎉"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
