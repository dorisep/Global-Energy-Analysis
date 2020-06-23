import os

from flask import Flask, render_template, redirect, request, url_for, send_from_directory

# from flask_pymongo import PyMongo
import pymongo


# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
# app.config['MONGO_DBNAME'] = 'Global_Energy_Analysis'
# mongo = PyMongo(app, uri="mongodb://localhost:27017/Global_Energy_Analysis")

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.Global_Energy_Analysis
# collection = db.produce

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    # Find one record of data from the mongo database
    TEC = list(db.TEC_Mod.find())
    TEP = list(db.TEP_Mod.find())
    EBOT = list(db.EBOT_Mod.find())
    EIG = list(db.EIG_Mod.find())
    # Return the homepage
    return render_template('index.html', TEC=TEC, TEP=TEP, EIG=EIG, EBOT=EBOT)

# Route to render TEC.html template using data from Mongo
@app.route("/TEC.html")
def TEC():
    # Find one record of data from the mongo database
    TEC = list(db.TEC_Mod.find())

    # Return template and data
    return render_template('TEC.html', TEC = TEC)

# Route to render TEP.html template using data from Mongo
@app.route("/TEP.html")
def TEP():
    # Find one record of data from the mongo database
    TEP = list(db.TEP_Mod.find())

    # Return template and data
    return render_template('TEP.html', TEP = TEP)

# # Route to render EBOT.html template using data from Mongo
@app.route("/EBOT.html")
def EBOT():
    # Find one record of data from the mongo database
    EBOT = list(db.EBOT_Mod.find())
    # Return template and data
    return render_template('EBOT.html', EBOT = EBOT)

# # Route to render EIG.html template using data from Mongo
@app.route("/EIG.html")
def EIG():
    # Find one record of data from the mongo database
    EIG = list(db.EIG_Mod.find())
    print(EIG)
    # Return template and data
    return render_template('EIG.html', EIG = EIG)


if __name__ == "__main__":
    app.run(debug=True)

