from flask import Flask, request
import operations

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

app.config['SECRET_KEY'] = "skey000"

# Welcome 
@app.route("/welcome")
def welcome():
    return "Welcome!"

@app.route("/welcome/home")
def welhome():
    return "Welcome home!"

@app.route("/welcome/back")
def welback():
    return "Welcome back!"

# Calc Part 1:
@app.route("/add")
def do_add():
    """Add a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.add(a, b)

    return str(result)

@app.route("/mul")
def do_mul():
    """Multiply a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.mult(a, b)

    return str(result)

@app.route("/sub")
def do_sub():
    """Subtract parameter b from parameter a."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.sub(a, b)

    return str(result)

@app.route("/div")
def do_div():
    """Divide parameter a by parameter b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.div(a, b)

    return str(result)

# Calc Part 2:
operators = {
    "add": operations.add,
    "sub": operations.sub,
    "mul": operations.mult,
    "div": operations.div,
    }

@app.route("/math/<func>")
def do_math(func):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[func](a, b)

    return str(result)
 