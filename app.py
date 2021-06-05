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

################################
# Flask set up
app = Flask(__name__)

################################


################################
# Flask Routes 
# Route 1: Home 
@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start-date<br/>"
        f"/api/v1.0/start-date/end-date<br/>"
    )




# Route 2: Precipitation
@app.route("/api/v1.0/precipitation")


'''
# Route 3: Stations
@app.route("/api/v1.0/stations")




# Route 4: Dates and temps observations
@app.route("/api/v1.0/tobs")



# Route 5: Temperatures
@app.route("/api/v1.0/<start")


@app.route("/api/v1.0/<start>/<end")
    

'''