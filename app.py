########## Denna fil gäller endast för VG-nivå ##########

from flask import Flask, jsonify, request
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


# Hej / Hello Tobias
# Vi har ändrat några namn på funktionerna eftersom det finns samma namn i database.py och app.py. Det blir lättare att läsa och hänga med.
# Har gjort lines med comments för att man ska kunna hänga med enklare. Lets go!

# ====================================== Welcome endpoint ================================================

@app.route('/', methods=['GET'])
def get_todos():
    return jsonify({'message': "welcome to hemnet!"})


# ====================================== FORMATS for read ================================================

# Vi kör en foreach loop där vi kollar igenom alla värdena för  att kunna formatera värderna
# listing
def format_listing(listings):
    return [{
        'id': listing['id'],
        'name': listing['name'],
        'price': listing['price'],
        'description': listing['description'],
        'category_id': listing['category_id'],
        'broker_id': listing['broker_id']
    } for listing in listings]


# category
def format_category(categorys):
    return [{
        'id': category['id'],
        'name': category['name']
    } for category in categorys]


# customer
def format_customer(customers):
    return [{
        'id': customer['id'],
        'name': customer['name'],
        'email': customer['email'],
        'contact_info': customer['contact_info']
    } for customer in customers]


# broker
def format_broker(brokers):
    return [{
        'id': broker['id'],
        'name': broker['name'],
        'email': broker['email'],
        'contact_info': broker['contact_info']
    } for broker in brokers]


# listing_customer
def format_listing_customer(listing_customers):
    return [{
        'listing_id': listing_customer['listing_id'],
        'customer_id': listing_customer['customer_id'],
        'appointments': listing_customer['appointments']
    } for listing_customer in listing_customers]


# customer_favorute_listing
def format_customer_favorute_listing(customer_favorute_listings):
    return [{
        'listing_id': customer_favorute_listing['listing_id'],
        'customer_id': customer_favorute_listing['customer_id'],
        'favorite_residence': customer_favorute_listing['favorite_residence']
    } for customer_favorute_listing in customer_favorute_listings]


# =========================================== CRUD operation START =================================================

# =========================================== listing crud =================================================

# Create listing
@app.route('/listing', methods=['POST'])
def add_listing_route():
    """
    Endpoint to add a new listing
    """
    data = request.get_json()
    name = data['name']
    price = data['price']
    description = data['description']
    category_id = data['category_id']
    broker_id = data['broker_id']
    database.create_listing(name, price, description, category_id, broker_id)
    return jsonify({'message': "created listing successfully"}), 201


# Read listing
@app.route('/listing', methods=['GET'])
def get_all_listings_route():
    """
    Should return a list of X number of listings based on a LIMIT
    """
    listings = database.view_listing()
    new_listing = format_listing(listings)
    return jsonify(new_listing), 200


# Read listing by id
@app.route('/listing/<int:id>', methods=['GET'])
def listing_detail_route(id):
    """
    Endpoint to return a specific listing
    """
    selected_listing = database.view_listing_by_id(id)
    new_listing = format_listing(selected_listing)
    return jsonify(new_listing), 200


# Update listing
@app.route('/listing/<int:id>', methods=['PUT'])
def update_listing_route(id):
    """
    Endpoint to update an existing listing
    """
    data = request.get_json()  # Hämtar data från Postman
    name = data['name']
    price = data['price']
    description = data['description']
    category_id = data['category_id']
    broker_id = data['broker_id']

    success = database.update_listing(
        id, name, price, description, category_id, broker_id)

    if success == True:
        return jsonify({'message': "Updated listing successfully"}), 200
    else:
        return jsonify({'message': "Failed to update listing"}), 400


# Delete listing
@app.route('/listing/<id>', methods=['DELETE'])
def remove_listing_route(id):
    """
    Endpoint to remove a listing
    """
    database.delete_listing(id)
    return jsonify({'message': "deleted listing successfully"}), 200


# =========================================== Category crud =================================================

# Create category
@app.route('/category', methods=['POST'])
def add_category_route():
    """
    Endpoint to add a new category
    Get category details from customer and call db.create_category
    """
    data = request.get_json()
    name = data['name']
    database.create_category(name)
    return jsonify({'message': "created listing successfully"}), 201


# Read category
@app.route('/category', methods=['GET'])
def get_all_category_route():
    """
    Should return a list of X number of category based on a LIMIT
    """
    selected_category = database.view_category()
    new_category = format_category(selected_category)
    return jsonify(new_category), 200


# Read category by id error uncomment later
@app.route('/category/<int:id>', methods=['GET'])
def category_detail_route(id):
    """
    Endpoint to return a specific listing
    """
    selected_category = database.view_category_by_id(id)
    new_category = format_category(selected_category)
    return jsonify(new_category), 200


# Update category
@app.route('/category/<int:id>', methods=['PUT'])
def update_category_route(id):
    """
    Endpoint to update a category
    Get updated category details from customer and call db.update_category
    """
    data = request.get_json()  # Hämtar data från Postman
    name = data['name']

    success = database.update_category(
        id, name)

    if success == True:
        return jsonify({'message': "Updated listing successfully"}), 200
    else:
        return jsonify({'message': "Failed to update listing"}), 400


# Delete category
@app.route('/category/<int:id>', methods=['DELETE'])
def remove_category_route(id):
    """
    Endpoint to remove a category
    """
    if database.delete_category(id):
        return jsonify({'message': "Deleted category successfully"}), 200
    else:
        return jsonify({'message': "Category not found or deletion failed"}), 404


# =========================================== Broker crud =================================================

# Create broker
@app.route('/broker', methods=['POST'])
def add_broker_route():
    """
    Endpoint to add a new broker
    Get broker details from broker and call db.create_broker
    """
    data = request.get_json()
    name = data['name']
    email = data['email']
    contact_info = data['contact_info']
    database.create_broker(name, email, contact_info)
    return jsonify({'message': "created listing successfully"}), 201


# Read all from broker
@app.route('/broker', methods=['GET'])
def get_all_broker_route():
    """
    Should return a list of X number of broker based on a LIMIT
    """
    selected_broker = database.view_broker()
    new_broker = format_broker(selected_broker)
    return jsonify(new_broker), 200


# Read broker by id
@app.route('/broker/<int:id>', methods=['GET'])
def broker_detail_route(id):
    """
    Endpoint to return a specific broker
    """
    selected_broker = database.view_broker_by_id(id)
    new_broker = format_broker(selected_broker)
    return jsonify(new_broker), 200


# This did not work!
# Update broker
@app.route('/broker/<int:id>', methods=['PUT'])
def update_broker_route(id):
    """
    Endpoint to update an existing broker
    """
    data = request.get_json()  # Hämtar data från Postman
    name = data['name']
    email = data['email']
    contact_info = data['contact_info']

    success = database.update_broker(
        id, name, email, contact_info)

    if success == True:
        return jsonify({'message': "Updated broker successfully"}), 200
    else:
        return jsonify({'message': "Failed to update broker"}), 400


# Delete broker by id
@app.route('/broker/<int:id>', methods=['DELETE'])
def remove_broker_route(id):
    """
    Endpoint to remove a category
    """
    if database.delete_broker(id):
        return jsonify({'message': "Deleted broker successfully"}), 200
    else:
        return jsonify({'message': "Broker not found or deletion failed"}), 404


# =========================================== Customer crud =================================================

# Create customer
@app.route('/customer', methods=['POST'])
def add_customer_route():
    """
    Endpoint to add a new customer
    Get customer details from customer and call db.create_customer
    """
    data = request.get_json()
    name = data['name']
    email = data['email']
    contact_info = data['contact_info']
    database.create_customer(name, email, contact_info)
    return jsonify({'message': "created customer successfully"}), 201


# Read all from customer
@app.route('/customer', methods=['GET'])
def get_all_customer_route():
    """
    Endpoint to list all customer
    """
    customers = database.view_customer()
    new_customer = format_customer(customers)
    return jsonify(new_customer), 200


# Read customer by id
@app.route('/customer/<int:id>', methods=['GET'])
def customer_detail_route(id):
    """
    Endpoint to return a specific customer
    """
    selected_customer = database.view_customer_by_id(id)
    new_customer = format_customer(selected_customer)
    return jsonify(new_customer), 200


# Update customer
@app.route('/customer/<int:id>', methods=['PUT'])
def update_customer_route(id):
    """
    Endpoint to update an existing customer
    """
    data = request.get_json()  # Hämtar data från Postman
    name = data['name']
    email = data['email']
    contact_info = data['contact_info']

    success = database.update_customer(
        id, name, email, contact_info)

    if success == True:
        return jsonify({'message': "Updated customer successfully"}), 200
    else:
        return jsonify({'message': "Failed to update customer"}), 400


# Delete customer by id
@app.route('/customer/<int:id>', methods=['DELETE'])
def remove_customer_route(id):
    """
    Endpoint to remove a customer
    """
    if database.delete_customer(id):
        return jsonify({'message': "Deleted customer successfully"}), 200
    else:
        return jsonify({'message': "Customer not found or deletion failed"}), 404


# =============================== listing_customer crud ===================================


# Create listing_customer
@app.route('/listing_customer', methods=['POST'])
def add_listing_customer_route():
    """
    Endpoint to add a new listing_customer
    Get listing_customer details from listing_customer and call db.listing_customer
    """
    data = request.get_json()
    listing_id = data['listing_id']
    customer_id = data['customer_id']
    appointments = data['appointments']
    database.create_appointment(listing_id, customer_id, appointments)
    return jsonify({'message': "created listing_customer successfully"}), 201


# Read all from listing_customer
@app.route('/listing_customer', methods=['GET'])
def get_all_listing_customer_route():
    """
    Endpoint to list all listing_customer
    """
    listing_customers = database.view_listing_customer()
    new_listing_customers = format_listing_customer(listing_customers)
    return jsonify(new_listing_customers), 200


# Read listing_customer by customer_id
@app.route('/listing_customer/<int:customer_id>', methods=['GET'])
def listing_customer_detail_route(customer_id):
    """
    Endpoint to return all appointments from listing_customer for a specific customer
    """
    selected_listing_customer = database.view_listing_customer_by_id(
        customer_id)
    new_listing_customer = format_listing_customer(selected_listing_customer)
    return jsonify(new_listing_customer), 200


# Update listing_customer
@app.route('/listing_customer/<int:customer_id>/<int:listing_id>', methods=['PUT'])
def update_listing_customer_route(customer_id, listing_id):
    """
    Endpoint to update an existing customer
    """
    data = request.get_json()  # Hämtar data från Postman
    appointments = data['appointments']

    success = database.update_listing_customer(
        appointments, listing_id, customer_id)

    if success == True:
        return jsonify({'message': "Updated listing_customer successfully"}), 200
    else:
        return jsonify({'message': "Failed to update listing_customer"}), 400


# Delete listing_customer by id
@app.route('/listing_customer/<int:customer_id>/<int:listing_id>', methods=['DELETE'])
def remove_listing_customer_route(customer_id, listing_id):
    """
    Endpoint to remove a customer
    """
    if database.remove_listing_customer(customer_id, listing_id):
        return jsonify({'message': "Deleted customer successfully"}), 200
    else:
        return jsonify({'message': "Customer not found or deletion failed"}), 404


# =============================== customer_favorute_listing crud ===================================


# Create customer_favorute_listing
@app.route('/customer_favorute_listing', methods=['POST'])
def add_customer_favorute_listing_route():
    """
    Endpoint to add a new customer_favorute_listing
    Get customer_favorute_listing details from customer_favorute_listing and call db.customer_favorute_listing
    """

    data = request.get_json()
    listing_id = data['listing_id']
    customer_id = data['customer_id']
    favorite_residence = data['favorite_residence']
    database.create_customer_favorute_listing(
        listing_id, customer_id, favorite_residence)
    return jsonify({'message': "created customer_favorute_listing successfully"}), 201


# Read all from customer_favorute_listing
@app.route('/customer_favorute_listing', methods=['GET'])
def get_all_customer_favorute_listing_route():
    """
    Endpoint to list all customer_favorute_listing
    """
    customer_favorute_listings = database.view_customer_favorute_listing()
    new_customer_favorute_listings = format_customer_favorute_listing(
        customer_favorute_listings)
    return jsonify(new_customer_favorute_listings), 200


# Read customer_favorute_listing by customer_id
@app.route('/customer_favorute_listing/<int:customer_id>', methods=['GET'])
def customer_favorute_listing_detail_route(customer_id):
    """
    Endpoint to return all appointments from listing_customer for a specific customer
    """
    selected_customer_favorute_listing = database.view_customer_favorute_listing_by_id(
        customer_id)
    new_customer_favorute_listing = format_customer_favorute_listing(
        selected_customer_favorute_listing)
    return jsonify(new_customer_favorute_listing), 200


# Update customer_favorute_listing
@app.route('/customer_favorute_listing/<int:customer_id>/<int:listing_id>', methods=['PUT'])
def update_customer_favorute_listing_route(customer_id, listing_id):
    """
    Endpoint to update an existing customer_favorute_listing
    """
    data = request.get_json()  # Hämtar data från Postman
    favorite_residence = data['favorite_residence']

    success = database.update_customer_favorute_listing(
        favorite_residence, listing_id, customer_id)

    if success == True:
        return jsonify({'message': "Updated customer_favorute_listing successfully"}), 200
    else:
        return jsonify({'message': "Failed to update customer_favorute_listing"}), 400


# Delete customer_favorute_listing by id
@app.route('/customer_favorute_listing/<int:customer_id>/<int:listing_id>', methods=['DELETE'])
def remove_customer_favorute_listing_route(customer_id, listing_id):
    """
    Endpoint to remove a customer
    """
    if database.remove_customer_favorute_listing(customer_id, listing_id):
        return jsonify({'message': "Deleted customer_favorute_listing successfully"}), 200
    else:
        return jsonify({'message': "customer_favorute_listing not found or deletion failed"}), 404


# =============================== END ===================================

# app.run(debug=True) default way
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # bättre sätt
