#controller
#view: jinja, html

import os

from flask import Flask, render_template,request
from flask_mail import Mail, Message



app = Flask(__name__)

mail = Mail(app)

#decorator (special funct that modifies other funct)

# define a route for /
@app.route("/")

#app.config["MAIL_DEFAULT_SENDER"] = os.environ["MAIL_DEFAULT_SENDER"]
#app.config["MAIL_DEFAULT_SENDER"] = 

def index():

    msg = Message("Hello",
              recipients=["boris.depoortere69@gmail.com"])
    msg.body = "testing"
    msg.html = "<b>testing</b>"
    mail.send(msg)

#just return render template of index.html

def index():
    return render_template("index.html")

@app.route("/greet",methods=["POST"])
def greet():
    name = request.args.get("name","world")
    #default world if no arg got
    return render_template("greet.html", namePerson=name)