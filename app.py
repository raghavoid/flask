from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello World."

@app.route("/add/<int:number1>/<int:number2>")
def add(number1 , number2):
    return f"{number1} + {number2} = {number1 + number2}."

@app.route("/handle_url")
def handle_params():
    greeting = request.args['greeting']
    name = request.args.get('name')
    return f"{greeting}, {name}"
# /handle_url?name=Mike&greeting=Hello      prints Hello, Mike on screen

@app.route("/hello", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return 'You made a GET request.'
    elif request.method == 'POST':
        return 'You made a POST request.'
    else:
        return 'You will never see this message.'

@app.route("/html")
def html():
    mylist = [10,20,30,40,50]
    some_text = "Hello World"
    return render_template("test.html", mylist=mylist,some_text=some_text)

@app.template_filter("reverse_string")
def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    app.run(debug=True)