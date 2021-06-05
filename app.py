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
# Route 1: Home/All measurements
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
def precipitation():
    # Begin session to start calling from database
    session = Session(engine)
    # Query all mesurements for dates and precipitation
    measurements = session.query(measurement.date, measurement.prcp).all()
    # Close session
    session.close()

    # Create dictionary from empty list  
    date_prcp = []
    for date, prcp in measurements:
        dict = {}
        dict[date] = prcp

        # Append to empty list
        date_prcp.append(dict)

    # Jsonify the list
    return jsonify(date_prcp)

# Route 3: Stations
@app.route("/api/v1.0/stations")
def stations():
    # Begin session to start calling from database
    session = Session(engine)
    # Query all mesurements for dates and precipitation
    stations = session.query(station.station, station.name).all()
    # Close session
    session.close()

    # Create dictionary from empty list  
    stations_list = []
    for station_id, name in stations:
        station_dict = {}
        station_dict[station_id] = name

        # Append to empty list
        stations_list.append(station_dict)

    # Jsonify the list
    return jsonify(stations_list)


# Route 4: Dates and temps observations
@app.route("/api/v1.0/tobs")
    # Begin session to start calling from database
    session = Session(engine)

    # Most recent date in data set
    most_recent = session.query(measurement.date).\
        order_by(measurement.date.desc()).first()

    # Calculate the date one year from the last date in data set.
    one_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Design a query to find the most active stations (i.e. what stations have the most rows?)
    # List the stations and the counts in descending order.
    most_rows = session.query(measurement.station, func.count(measurement.station)).\
        group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()





Query the dates and temperature observations of 
the most active station for the last year of data.


Return a JSON list of temperature observations (TOBS) 
for the previous year.
'''
# Route 5: Temperatures
@app.route("/api/v1.0/<start")


@app.route("/api/v1.0/<start>/<end")
    

'''