# Flask Challenge

#import modules
from flask import Flask, jsonify 


# Flask set up
app = Flask(__name__)

# Route 1: Home 
@app.route("/")
def home(): 
    return home

# Route 2: Precipitation
@app.route("/api/v1.0/precipitation")



# Route 1: Stations
@app.route("/api/v1.0/stations")




# Route 1: Dates and temps observations
@app.route("/api/v1.0/tobs")



# Route 1: Temperatures
@app.route("/api/v1.0/<start")


@app.route("/api/v1.0/<start>/<end")
    