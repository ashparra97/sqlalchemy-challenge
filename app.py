# Flask Challenge

#import flask and sqlalchemy tools
from flask import Flask, jsonify
import sqlalchemy 
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

# import dependencies
import numpy as np 
import pandas as pd 
import datetime as dt

# SQL Alchemy set up
engine = create_engine("sqlite:///hawaii.sqlite")

# Declare a base
base = automap_base()

# Use base to reflect the database tables 
base.prepare(engine, reflect=True)

# Reflect tables into classes and save a reference to those classes
station = base.classes.station
measurement = base.classes.measurement

# Create session
session = Session(engine)




# Flask set up
app = Flask(__name__)

# Route 1: Home 
@app.route("/")
def home(): 
    return render_template("index.html")




# Route 2: Precipitation
@app.route("/api/v1.0/precipitation")



# Route 1: Stations
@app.route("/api/v1.0/stations")




# Route 1: Dates and temps observations
@app.route("/api/v1.0/tobs")



# Route 1: Temperatures
@app.route("/api/v1.0/<start")


@app.route("/api/v1.0/<start>/<end")
    