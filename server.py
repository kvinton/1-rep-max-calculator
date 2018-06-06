from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify, url_for)

from flask_debugtoolbar import DebugToolbarExtension

from sqlalchemy import func, desc

# from model import (connect_to_db, db, User, UserMessage, CustomerService, 
#                    CXMessage, MessageThread)



# from helper_functions import (is_message_urgent, is_thread_urgent, 
#                               create_all_messages_dict, get_unread_message_threads,
#                               get_recent_message_threads, get_urgent_message_threads,
#                               get_threads_by_cx, create_message_thread_dict)


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

    app.debug = True

    app.jinja_env.auto_reload = app.debug

    # connect_to_db(app)

    DebugToolbarExtension(app)

    # app.run()

    app.run(port=5000, threaded=True, host='0.0.0.0')