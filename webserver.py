from flask import Flask
from threading import Thread
import os

const port = process.env.PORT || 4000 

app = Flask(__name__)

@app.route("/")
def home():
    return "Discord bot ok"


def run():
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

