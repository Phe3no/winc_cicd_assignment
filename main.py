# Import what we need from flask
from flask import Flask, render_template, request

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested


@app.route('/')
def index():
    return render_template("public/index.html")


@app.route('/calculations', methods=("GET", "POST"))
def calculations():
    number_1 = None
    number_2 = None
    add_nums = None
    substract_nums = None
    multiply_nums = None
    divide_nums = None
    remainder_nums = None
    if request.method == "POST":
        number_1 = int(request.form["number_1"])
        number_2 = int(request.form["number_2"])
        error = None

        from static.python.calculations import add, substract, multiply, divide, remainder
        # call the functions with the numbers as arguments
        add_nums = add(number_1, number_2)
        substract_nums = substract(number_1, number_2)
        multiply_nums = multiply(number_1, number_2)
        divide_nums = divide(number_1, number_2)
        remainder_nums = remainder(number_1, number_2)

    return render_template("public/calculations.html", number_1=number_1, number_2=number_2, add_nums=add_nums, substract_nums=substract_nums, multiply_nums=multiply_nums, divide_nums=divide_nums, remainder_nums=remainder_nums)


if __name__ == "__main__":
    app.run()
