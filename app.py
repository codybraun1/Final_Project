import os

import pandas as pd
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/mvps.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
Data = Base.classes.mvps


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("data/<actual_season>")
def get_data(actual_season):
    sel = [
        #columns to select
    ]

    results = db.session.query(*sel).filter(Data.ActualSeason == actual_season).all()

    # Create a dictionary entry for each row of information
    actual_data = {}
    for result in results:
        actual_data[] = result[0]

    print(actual_data)
    return jsonify(actual_data)


@app.route("data/<pred_season>")
def get_data(pred_season):
    sel = [
        #columns to select
    ]

    results = db.session.query(*sel).filter(Data.PredSeason == pred_season).all()

    # Create a dictionary entry for each row of information
    pred_data = {}
    for result in results:
        pred_data[] = result[0]

    print(pred_data)
    return jsonify(pred_data)


if __name__ == "__main__":
    app.run()
