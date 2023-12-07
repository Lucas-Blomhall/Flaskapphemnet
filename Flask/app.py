########## Denna fil gäller endast för VG-nivå ##########


# Crud delen med routes här


from flask import Flask, request
from dotenv import load_dotenv
import os
import psycopg2
import database

app = Flask(__name__)
load_dotenv()
con = database.connect_db()

"""
- Add a variable called FLASK_DEBUG=True to your .env-file to turn on debug-mode
- Run the flask-application using "flask run"

ADD ENDPOINTS FOR FLASK HERE
Make sure to do the following:
- use @app.route with the appropriate HTTP-verb
- Use correct STATUS CODES, e.g 200, 400, 401 etc. when returning a result to the user
This means you need some error handling that determine what should be returned to the user
Read more: https://www.geeksforgeeks.org/10-most-common-http-status-codes/
- Use correct URL paths the resource, e.g some endpoints should be located at the exact same URL, 
but will have different HTTP-verbs.

Whenever possible, you should reuse the functions in the database class which
you used in the G-part. Otherwise, create new database functions in database.py.
You probably do not need any new tables - an API is all about interacting with your existing data
Feel free to add more endpoints if you want.
"""


# # does not work
# @app.route('/')
# def check():
#     return 'Hello world'

@app.route("/employees", methods=["GET"])
def view_listing():
    db = database.connect_db()
    return db.all()


def add_listing():
     
    """
    Endpoint to add a new listing
    """


def remove_listing():
    """
    Endpoint to remove a listing
    """
    pass


def listing_detail():
    """
    Endpoint to return a specific listing
    """
    pass


def get_all_listings():
    """
    Should return a list of X number of listings based on a LIMIT
    """
    pass


def add_category():
    """
    Endpoint to add a new category
    Get category details from customer and call db.create_category
    """
    pass


def update_category():
    """
    Endpoint to update a category
    Get updated category details from customer and call db.update_category
    """
    pass


def add_broker():
    """
    Endpoint to add a new broker
    Get broker details from customer and call db.create_broker
    """
    pass


def modify_broker():
    """
    Endpoint to modify a broker
    Get updated broker details from customer and call db.update_broker
    """
    pass


def add_customer():
    """
    Endpoint to add a new customer
    Get customer details from customer and call db.create_customer
    """
    pass


def remove_customer():
    """
    Endpoint to remove a customer
    Get customer ID from customer and call db.delete_customer
    """
    pass


def get_all_customers():
    """
    Endpoint to list all customer
    """


def schedule_appointment():
    """
    Endpoint to schedule a viewing appointment
    Get appointment details from customer and call db.create_appointment
    """
    pass


def update_appointment():
    """
    Endpoint to update an existing appointment
    Get appointment details from customer and call db.update_appointment
    """
    pass


def cancel_appointment():
    """
    Endpoint to cancel an appointment
    Get appointment ID from customer and call db.remove_appointment
    """
    pass


def list_customer_appointments():
    """
    Endpoint that returns appointments for a specific customer
    Get customer ID from customer and call db.view_appointments_for_customer
    """
    pass


def favorite_listing():
    """
    Endpoint to let a customer favorite a specific listing
    Should ideally only need a title, it's your choice how to implement it
    """
    pass


def unfavorite_listing():
    """
    Endpoint to let a customer unfavorite a specific listing
    Should ideally only need a title, but it's your choice how to implement it
    """
    pass
