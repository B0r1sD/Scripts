from flask import Flask, render_template,request

app = Flask(__name__)

#decorator (special funct that modifies other funct)

# define a route for /
@app.route("/")

#just return render template of index.html

def index():
    return render_template("index.html")

@app.route("/greet",methods=["POST"])
def greet():
    name = request.args.get("name","world")
    #default world if no arg got
    return render_template("greet.html", namePerson=name)