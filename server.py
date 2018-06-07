from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify, url_for)

import os

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

################################################################################

################### VIEW FUNCTIONS RENDERING TEMPLATES #########################

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

    max_weight = (weight * reps * 0.033) + weight

    return str(round(max_weight,2))

@app.route('/calculate-working-weight')
def calculate_working_weight():

    target_max = request.args.get('target-max')
    reps = request.args.get('reps')

    print reps

    target_max = float(target_max)
    reps = float(reps)

    weight = target_max/((reps * 0.033) + 1)



    print(weight)

    return str(round(weight,2))




if __name__ == "__main__":

    app.debug = False

    port = int(os.environ.get('PORT', 5000))

    app.run(port=port, host='0.0.0.0')