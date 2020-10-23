from server import *


@app.route("/")
def home():
    return "Send a post request to the /H or go to /H url and it will give further instructions ! "
