from flask import *
from flask_restful import *
from pymongo import *

app = Flask(__name__)
app.debug = True
app.secret_key = "RANUGA D 2008"
api = Api(app)
cluster = MongoClient(
    "mongodb+srv://Ranuga:Ranuga@cluster0.u7gva.mongodb.net/<dbname>?retryWrites=true&w=majority"
)
from server.rest_api import *
from server.routes import *