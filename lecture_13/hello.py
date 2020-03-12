print("welcome to coding block")
from flask import Flask

app = Flask("hello")

@app.route("/")
def sayhi():
    return("I say hi")

app.run()