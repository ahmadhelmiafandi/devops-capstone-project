from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)

# Security Headers with Talisman
talisman = Talisman(app, content_security_policy=None)

@app.route("/")
def hello():
    return "Hello, World!"
