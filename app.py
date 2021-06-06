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
    final = session.query(measurement.date, measurement.prcp).all()
    # Close session
    session.close()

    # Create dictionary from empty list  
    date_prcp = []
    for date, prcp in final:
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
    final = session.query(station.station, station.name).all()
    # Close session
    session.close()

    # Create dictionary from empty list  
    stations_list = []
    for station_id, name in final:
        station_dict = {}
        station_dict[station_id] = name

        # Append to empty list
        stations_list.append(station_dict)

    # Jsonify the list
    return jsonify(stations_list)


# Route 4: TOBS
@app.route("/api/v1.0/tobs")
def tobs():
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
    # filter by station with highest number of observatons
    most_obs = most_active[0][0]

    final = session.query(measurement.date, measurement.tobs).\
                filter(measurement.date <= "2017-08-23").\
                filter(measurement.date >= "2016-08-24").\
                filter(measurement.station == most_obs).all()
    session.close()

     # Create dictionary from empty list  
    tobs = []
    for date, tobs in final:
        tobs_dict = {}
        tobs_dict[date] = tobs

        # Append to empty list
        tobs.append(tobs_dict)

    # Jsonify the list
    return jsonify(tobs)


# Route 5: Start Date 
@app.route("/api/v1.0/<start>")
def start_date(start):
    # Begin session to start calling from database
    session = Session(engine)    
    final = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
            filter(measurement.date >= start).all()
    session.close()

    # Create dictionary from empty list  
    final_tobs = []
    for date, min_tobs, max_tobs, avg_tobs in final:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Min"] = min_tobs 
        tobs_dict["Max"] = max_tobs 
        tobs_dict["Avg"] = avg_tobs

        # Append to empty list
        final_tobs.append(tobs_dict)
    
    return jsonify(final_tobs)


# Routh 6: Start Date and End Date 
@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    # Begin session to start calling from database
    session = Session(engine)    
    final = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start).\
        filter(measurement.date <= end).all()
    session.close()

    # Create dictionary from empty list  
    final_tobs = []
    for date, min_tobs, max_tobs, avg_tobs in final:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Min"] = min_tobs 
        tobs_dict["Max"] = max_tobs 
        tobs_dict["Avg"] = avg_tobs

        # Append to empty list
        final_tobs.append(tobs_dict)
    
    return jsonify(final_tobs)
    
if __name__ == "__main__":
    app.run(debug=True)
  