"""Import flask and random libraries."""
from flask import Flask, request, render_template
from random import sample

app = Flask(__name__)


def sort_letters(message):
    """Sort the characters of a string in alphabetical order."""
    return "".join(sorted(list(message)))


@app.route("/")
def homepage():
    """Homepage with handy links for your convenience."""
    return render_template("home.html")


@app.route("/froyo")
def choose_froyo():
    """Show a form to collect the user's Fro-Yo order."""
    return render_template("froyo_form.html")


@app.route("/froyo_results")
def show_froyo_results():
    """Show the user what they ordered from the previous page."""
    context = {
        "users_froyo_flavor": request.args.get("flavor"),
        "users_froyo_toppings": request.args.get("toppings"),
    }
    return render_template("froyo_results.html", **context)


@app.route("/favorites")
def favorites():
    """Show the user a form to pick their favorite color, animal, and city."""
    return render_template("favorites_form.html")


@app.route("/favorites_results")
def favorites_results():
    """Show the user a nice message using their form results."""
    context = {
        "color": request.args.get("color"),
        "animal": request.args.get("animal"),
        "city": request.args.get("city"),
    }
    return render_template("favorites_results.html", **context)


@app.route("/secret_message")
def secret_message():
    """Show the user a form to collect a secret message.

    Send the result via the POST method to keep it a secret.
    """
    return render_template("secret_message.html")


@app.route("/message_results", methods=["POST"])
def message_results():
    """Show the user their message, with the letters in sorted order."""
    message = sort_letters(request.form.get("message"))
    return render_template("message_results.html", message=message)


@app.route("/calculator")
def calculator():
    """Show the user a form to enter 2 numbers and an operation."""
    return render_template("calculator_form.html")


@app.route("/calculator_results")
def calculator_results():
    """Show the user the result of their calculation."""
    operation = request.args.get("operation")
    operand_one = int(request.args.get("operand1"))
    operand_two = int(request.args.get("operand2"))

    if operation == "add":
        result = operand_one + operand_two
    elif operation == "subtract":
        result = operand_one - operand_two
    elif operation == "multiply":
        result = operand_one * operand_two
    elif operation == "divide":
        result = operand_one / operand_two

    context = {
        "operation": operation,
        "operand_one": operand_one,
        "operand_two": operand_two,
        "result": result,
    }

    return render_template("calculator_results.html", **context)


list_of_compliments = [
    "awesome",
    "beatific",
    "blithesome",
    "conscientious",
    "coruscant",
    "erudite",
    "exquisite",
    "fabulous",
    "fantastic",
    "gorgeous",
    "indubitable",
    "ineffable",
    "magnificent",
    "outstanding",
    "propitioius",
    "remarkable",
    "spectacular",
    "splendiferous",
    "stupendous",
    "super",
    "upbeat",
    "wondrous",
    "zoetic",
]


@app.route("/compliments")
def compliments():
    """Show the user a form to get compliments."""
    return render_template("compliments_form.html")


@app.route("/compliments_results")
def compliments_results():
    """Show the user some compliments."""
    num_compliments = request.args.get("num_compliments")
    chosen_compliments = sample(list_of_compliments, int(num_compliments))
    context = {
        "name": request.args.get("users_name"),
        "wants_compliments": request.args.get("wants_compliments"),
        "chosen_compliments": chosen_compliments,
    }

    return render_template("compliments_results.html", **context)


if __name__ == "__main__":
    app.run()
