import database as db
import psycopg2

"""
This file is responsible to interact with the user

- You should use input() ONLY in this file and not in database.py
- You should use print() ONLY in this file and not in database.py
- You should error handle here, e.g using try except to catch various errors
- This file is responsible for showing the menu to the user
"""

def add_listing():
    """
    Function to add a new listing
    Get customer input for listing details and call db.create_listing
    """

def remove_listing():
    """
    Function to remove a listing
    Get listing ID from customer and call db.delete_listing
    """
    pass

def display_listing():
    """
    Function to display a listing
    Get listing ID from customer and call db.view_listing
    Make sure to include information about the broker, listing and customer
    """
    pass

def add_category():
    """
    Function to add a new category
    Get category details from customer and call db.create_category
    """
    pass

def update_category():
    """
    Function to update a category
    Get updated category details from customer and call db.update_category
    """
    pass

def add_broker():
    """
    Function to add a new broker
    Get broker details from customer and call db.create_broker
    """
    pass

def modify_broker():
    """
    Function to modify a broker
    Get updated broker details from customer and call db.update_broker
    """
    pass

def add_customer():
    """
    Function to add a new customer
    Get customer details from customer and call db.create_customer
    """
    pass

def remove_customer():
    """
    Function to remove a customer
    Get customer ID from customer and call db.delete_customer
    """
    pass

def schedule_appointment():
    """
    Function to schedule a viewing appointment
    Get appointment details from customer and call db.create_appointment
    """
    pass

def update_appointment():
    """
    Function to update an existing appointment
    Get appointment details from customer and call db.update_appointment
    """
    pass

def cancel_appointment():
    """
    Function to cancel an appointment
    Get appointment ID from customer and call db.remove_appointment
    """
    pass

def view_customer_appointments():
    """
    Function to view appointments for a specific customer
    Get customer ID from customer and call db.view_appointments_for_customer
    """
    pass

def favorite_listing():
    """
    Function to let a customer favorite a specific listing
    Should ideally only need a title, it's your choice how to implement it
    """
    pass
    
def unfavorite_listing():
    """
    Function to let a customer unfavorite a specific listing
    Should ideally only need a title, but it's your choice how to implement it
    """
    pass

# Main execution logic
def main():
    """
    Here, you can add a menu system or command line arguments to call above functions
    """
    pass

if __name__ == '__main__':
    db.connect_db()
    db.create_tables()
    main()
