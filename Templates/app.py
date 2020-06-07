import os

from flask import Flask, render_template, redirect, request, url_for, send_from_directory

# from flask_pymongo import PyMongo
from flask_pymongo import pymongo


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
def home():
    # Find one record of data from the mongo database
    # Project2 = list(db.Project2.find())

    # Return the homepage
    return render_template('index.html')

# Route to render TEC.html template using data from Mongo
@app.route("/TEC.html")
def TEC2():
    # Find one record of data from the mongo database
    TEC = list(db.TEC.find())


    # Return template and data
    return render_template('TEC.html', TEC = TEC)

# Route to render TEP.html template using data from Mongo
@app.route("/TEP.html")
def TEP():
    # Find one record of data from the mongo database
    TEP = list(db.TEP.find())
    print(TEP)


    # Return template and data
    return render_template('TEP.html', TEP = TEP)

# # Route to render EBOT.html template using data from Mongo
@app.route("/EBOT.html")
def EBOT():
    # Find one record of data from the mongo database
    EBOT = list(db.EBOT.find())


    # Return template and data
    return render_template('EBOT.html', EBOT = EBOT)

# # Route to render EIG.html template using data from Mongo
@app.route("/EIG.html")
def EIG():
    # Find one record of data from the mongo database
    EIG = list(db.EIG.find())


    # Return template and data
    return render_template('EIG.html', EIG = EIG)

# # Route to render CC.html template using data from Mongo
# @app.route("/CC.html")
# def CC():
    # Find one record of data from the mongo database
    # coordinates = mongo.db.coordinates.find({})


    # Return template and data
    # return render_template('CC.html', coordinates = coordinates)

if __name__ == "__main__":
    app.run(debug=True)

