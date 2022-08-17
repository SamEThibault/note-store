from flask import Flask, render_template
import os
from pymongo import MongoClient
import pymongo
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# connect to the MongoDB cloud db using the .env URI
client = MongoClient(os.getenv("CONNECTION_STRING"))
db = client["note-store"]
users_collection = db["users"]
codenotes_collection = db["code-notes"]
writtennotes_collection = db["written-notes"]

# example of inserting a document into the users collection
# users_collection.insert_one(
#     {
#         "_id": "U1IT00001",
#         "item_name": "Blender",
#         "max_discount": "10%",
#         "batch_number": "RR450020FRG",
#         "price": 340,
#         "category": "kitchen appliance",
#     }
# )


@app.route("/")
def index():
    return render_template(
        "index.html", title="Note Store - Home", url=os.getenv("URL")
    )


@app.route("/CMPE327")
def CMPE327():
    return render_template(
        "CMPE327.html",
        title="Note Store - CMPE 327",
        url=os.getenv("URL"),
        name="CMPE 327 - Software Quality Assurance",
    )
