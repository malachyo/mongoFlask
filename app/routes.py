import os
from app import app
from flask import render_template, request, redirect

username = "period8"

from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'test'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:UpobVeCKfQUWohRm@cluster0-at8av.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')
# two urls to lead to homebage
def index():
    collection = mongo.db.events
    events = list(collection.find({}))
    # make a list of all found events
    return render_template('index.html', events = events)

@app.route('/input')

def input():
    return render_template('input.html')


@app.route('/add')

def add():
    test = mongo.db.test
    # connect to database
    test.insert({'name': 'last day of school'})
    # insert data
    return "Added to database."


@app.route('/results', methods = ["Get", "Post"])
def results():
    userdata = dict(request.form)
    print(userdata)
    event_name = userdata['event_name']
    print(event_name)
    event_date = userdata['event_date']
    print(event_date)
    event_type = userdata['event_type']
    print(event_type)
    # connecting to  mongo cluster and collection and database events



    events = mongo.db.events
    events.insert({"name": event_name, "date": event_date, "type": event_type})
    # inserting details of the event to database as a dictionary {“name”: event_name, “date”: event_date, “type”: event_type}

    return redirect('/index')
    # bring user back to homepage
