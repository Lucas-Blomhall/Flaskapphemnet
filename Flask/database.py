import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

"""
This file is responsible for making database queries

- Try to return results with cursor.fetchall() or cursor.fetchone() when possible
- Make sure you always give the user response if something went right or wrong, sometimes 
you might need to use the RETURNING keyword to garantuee that something went right / wrong
e.g when making DELETE or UPDATE queries
- You will need to decide which parameters each function should receive. All functions 
start with a connection parameter.
"""

# Replace with actual database credentials
load_dotenv()
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

# Optional, add these to psycopg.connect() if you need to
DATABASE_PORT = os.getenv("DATABASE_PORT")  # default is normally 5432
DATABASE_USER = os.getenv("DATABASE_USER")  # default is normally postgres


# postgresql://postgres:Vanligt123!@localhost/carappdb


def connect_db():
    """Establishes a connection to the database."""
    try:
        connection = psycopg2.connect(
            host="localhost", post="5432", database="hemnet", user="postgres", password="Vanligt123!")
        return connection
    # connection = psycopg2.connect(
    #         dbname=DATABASE_NAME, password=DATABASE_PASSWORD, user="postgres")
    #     return connection
    except psycopg2.DatabaseError as e:
        print(f"Database connection failed: {e}")
        raise


async def create_tables(connection):
    """
    Create any necessary tables in this function, you can choose yourself if you want to
    run it at start or not.
    """
    pass


def create_listing(connection):
    """Creates a new listing in the database."""
    # Implement the SQL query to insert a new listing
    pass


def delete_listing(connection):
    """Deletes a listing from the database."""
    pass


def view_listing(connection):
    car = db.query(SQLCar).filter(SQLCar.id == car_id).first()
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    db.delete(car)
    db.commit()
    return {"message": "Car deleted successfully"}
    # Implement the SQL query to retrieve listing details with JOIN
    pass


def create_category(connection):
    """Creates a new category in the database."""
    pass


def update_category(connection):
    """Updates an existing category."""
    pass


def create_broker(connection):
    """Creates a new broker in the database."""
    pass


def update_broker(connection):
    """Updates an existing broker."""
    pass


def create_customer(connection):
    """Creates a new customer in the database."""
    pass


def delete_customer(connection):
    """Deletes a customer from the database."""
    pass


def create_appointment(connection):
    """Creates a new viewing appointment."""
    pass


def remove_appointment(connection):
    """Removes an appointment."""
    pass


def update_appointment(connection):
    """
    Updates an appointment
    """
    pass


def view_appointments_for_customer(connection):
    """Retrieves all appointments for a specific customer."""
    pass


def favorite_listing(connection):
    """You can choose freely how to implement it"""
    pass


def unfavorite_listing(connection):
    """You can choose freely how to implement it"""
    pass
