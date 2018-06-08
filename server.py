from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify, url_for)

import os

import math 

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

################################################################################

################### VIEW FUNCTIONS RENDERING TEMPLATES #########################

def calculate_1_rep_max(weight, reps):

    return (weight * reps * 0.033) + weight

def calculate_working_weight(target_max, reps):

    return target_max/((reps * 0.033) + 1)


def myround(x, prec=2, base=2.5):
  return round(base * round(float(x)/base),prec)


def roundup(x):
    return int(math.ceil(x / 2.5)) * 2.5


@app.route('/')
def index():
    """Homepage."""

    return render_template('index.html')

@app.route('/calculate-rep-max')
def calculate_rep_max():

    weight = request.args.get('weight')
    reps = request.args.get('reps')

    weight = float(weight)
    reps = float(reps)

    max_weight = calculate_1_rep_max(weight, reps)

    return str(round(max_weight,2))

@app.route('/calculate-working-weight')
def calculate_weight():

    target_max = request.args.get('target-max')
    reps = request.args.get('reps')

    print reps

    target_max = float(target_max)
    reps = float(reps)

    weight = calculate_working_weight(target_max, reps)

    print(weight)

    return str(round(weight,2))

@app.route("/off-season")
def render_off_season():

    return render_template('offseason.html')

@app.route('/calculate-next-rep-max')
def calculate_next_max():

    weight = request.args.get('weight')
    reps = request.args.get('reps')
    week = request.args.get('week')

    print week

    weight = float(weight)
    reps = float(reps)
    week = int(week)

    max_weight = calculate_1_rep_max(weight, reps)

    rep_scheme = [8, 5, 8, 5, 3, 5, 3, 2]

    rep_scheme = rep_scheme[week:]

    upcoming_weights = []

    for reps in rep_scheme:

        max_weight = max_weight + 1

        new_weight = calculate_working_weight(max_weight, reps)

        if new_weight % 2.5 != 0:
            new_weight = roundup(new_weight)
            max_weight = calculate_1_rep_max(new_weight, reps)
            print max_weight


        upcoming_weights.append((round(new_weight,2), reps, round(max_weight,2)))

    
    my_dict = {'weights': upcoming_weights}

    return jsonify(my_dict)







if __name__ == "__main__":

    app.debug = True

    port = int(os.environ.get('PORT', 5000))

    app.run(port=port, host='0.0.0.0')