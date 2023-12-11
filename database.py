import psycopg2
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


# ==================================== Connecting to table =======================================================


# Replace with actual database credentials
load_dotenv()

database_url = os.getenv("DATABASE_URL")


def connect_db():
    """Establishes a connection to the database."""
    try:
        connection = psycopg2.connect(
            database_url, cursor_factory=psycopg2.extras.DictCursor)
        return connection
    except psycopg2.DatabaseError as e:
        print(f"Database connection failed: {e}")
        raise


# ==================================== creating tables =======================================================


def create_tables(connection):
    """
    Create any necessary tables in this function, you can choose yourself if you want to
    run it at start or not.
    """
    with connect_db() as connection:
        with connection.cursor() as cur:
            create_broker = """
            CREATE TABLE IF NOT EXISTS broker(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) CHECK(email LIKE '%@%') UNIQUE,
            contact_info VARCHAR(20)
            );
            """
            create_category = """
            CREATE TABLE IF NOT EXISTS category(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) UNIQUE NOT NULL,
            );
            """
            create_customer = """
            CREATE TABLE IF NOT EXISTS customer(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) CHECK(email LIKE '%@%') UNIQUE,
            contact_info VARCHAR(20)
            );
            """
            create_listing = """
            CREATE TABLE IF NOT EXISTS listing(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price INT NOT NULL,
            description VARCHAR(255),
            category_id INT REFERENCES category(id),
            broker_id INT REFERENCES category(id)    
            );
            """
            create_listing_customer = """
            CREATE TABLE IF NOT EXISTS listing_customer(
            listing_id INT,
            customer_id INT,
            appointments BOOLEAN,
            PRIMARY KEY(listing_id, customer_id)
            );
            """
            create_customer_favorute_listing = """
            CREATE TABLE IF NOT EXISTS listing_customer(
            listing_id INT,
            customer_id INT,
            favorite_residence BOOLEAN
            PRIMARY KEY(listing_id, customer_id)
            );
            """
            try:
                cur.execute(create_broker)
                cur.execute(create_category)
                cur.execute(create_customer)
                cur.execute(create_listing)
                cur.execute(create_listing_customer)
                cur.execute(create_customer_favorute_listing)
                # extra table för favorit
                connection.commit()
                print("Created table successfully in PostgreSQL")
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False


# ==================================== EXTRA: Check if the table exists =======================================================

# The testing if first table exists name broker. If you want to test another table change 1 to the table name and select the name and see if it exists. Will rewrite this line comment later!
table_name = "broker"


def check_if_exists(table_name):
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute("""
                            SELECT EXISTS(
                            SELECT 1 FROM information_schema.tables
                            WHERE table_catalog = 'hemnet'
                            AND table_schema = 'public'
                            AND table_name = %s
                            );
                            """, (table_name,))
                return cur.fetchone()[0]
            except psycopg2.Error as e:
                print("Error", e)
                return False


print(f"Table {table_name} exists: {check_if_exists(table_name)}")
if check_if_exists(table_name) == False:
    create_tables()
else:
    print("Table already exists")

print(f"Table {table_name} exists: {check_if_exists(table_name)}")


# ==================================== Starting CRUD =======================================================

# ==================================== new: listing CRUD =======================================================


# Create a listing:
def create_listing(name, price, description, category_id, broker_id):
    """Creates a new listing in the database."""
    # Implement the SQL query to insert a new listing
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO listing (name, price, description, category_id, broker_id) VALUES (%s, %s, %s, %s, %s)", (name, price, description, category_id, broker_id))
                connection.commit()
                print("Created listing successfully")
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False


# Get all from listing
def view_listing():
    """Retrieves details of a specific listing along with category and broker information."""
    # Implement the SQL query to retrieve listing details with JOIN
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute("SELECT * FROM listing ORDER BY id ASC")
                print("Got all listing successfully")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


# get listing by id
def view_listing_by_id(id):
    """Retrieves details of a specific listing along with category and broker information."""
    # Implement the SQL query to retrieve listing details with JOIN
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute("SELECT * FROM listing WHERE id = %s", (id,))
                print("Got specific listing by id successfully")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


# Update a listing by id
def update_listing(id, name, price, description, category_id, broker_id):
    """Updates an existing listing."""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute(
                    "UPDATE listing SET name = %s, price = %s, description = %s, category_id = %s, broker_id = %s WHERE id = %s",
                    (name, price, description, category_id, broker_id, id))
                connection.commit()
                print("Updated listing by id successfully")
                return True
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False


# Delete a listing
def delete_listing(id):
    """Deletes a listing from the database."""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute(
                    "DELETE FROM listing WHERE id = %s", (id,))
                connection.commit()
                print("Deleted listing successfully")
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False


# ==================================== end new: category CRUD =======================================================


# Create Category
def create_category(name):
    """Creates a new category in the database."""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO category (name) VALUES (%s)", (name,))
                connection.commit()
                print("Created category successfully")
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False


# Read all from category:
def view_category():
    """Retrieves details of a specific category along with category and broker information."""
    # Implement the SQL query to retrieve listing details with JOIN
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute("SELECT * FROM category ORDER BY id ASC")
                print("Got all data from category successfully")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


# Read a category by id
def view_category_by_id(id):
    """Retrieves details of a specific category along with category and broker information."""
    # Implement the SQL query to retrieve category details with JOIN
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute("SELECT * FROM category WHERE id = %s", (id,))
                print("Got specific category by id successfully")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


# Update a category by id
def update_category(id, name):
    """Updates an existing category."""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute(
                    "UPDATE category SET name = %s WHERE id = %s", (name, id))
                connection.commit()
                print("Updated category by id successfully")
                return True
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False


# Delete a category by id
def delete_category(id):
    """Deletes a category from the database."""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute("DELETE FROM category WHERE id = %s", (id,))
                affected_rows = cur.rowcount  # Get the number of affected rows
                connection.commit()
                print("Deleted category successfully")
                return affected_rows > 0  # Return True if any rows were deleted
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False

            # BONUS we add so that we can delete the parent id for child ids


# ==================================== end new: broker CRUD =======================================================


# Create a broker
def create_broker(name, email, contact_info):
    """Creates a new broker in the database."""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO broker (name, email, contact_info) VALUES (%s, %s, %s)", (name, email, contact_info))
                connection.commit()
                print("Created broker successfully")
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False


# Read all from broker
def view_broker():
    """Retrieves details of a specific broker along with category and broker information."""
    # Implement the SQL query to retrieve broker details with JOIN
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute("SELECT * FROM broker ORDER BY id ASC")
                print("Got all broker successfully")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


# Read broker by id
def view_broker_by_id(id):
    """Retrieves details of a specific listing along with category and broker information."""
    # Implement the SQL query to retrieve broker details with JOIN
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute("SELECT * FROM broker WHERE id = %s", (id,))
                print("Got specific broker by id successfully")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


# Update a broker by id
def update_broker(id, name, email, contact_info):
    """Updates an existing broker."""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute(
                    "UPDATE broker SET name = %s, email = %s, contact_info = %s WHERE id = %s", (name, email, contact_info, id))
                connection.commit()
                print("Updated broker by id successfully")
                return True
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False


# Delete broker by id
def delete_broker(id):
    """Deletes a broker from the database."""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute("DELETE FROM broker WHERE id = %s", (id,))
                affected_rows = cur.rowcount  # Get the number of affected rows
                connection.commit()
                print("Deleted broker successfully")
                return affected_rows > 0  # Return True if any rows were deleted
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False


# ==================================== end new: customer CRUD =======================================================


# Create a customer
def create_customer(name, email, contact_info):
    """Creates a new customer in the database."""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO customer (name, email, contact_info) VALUES (%s, %s, %s)", (name, email, contact_info))
                connection.commit()
                print("Created customer successfully")
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False


# Read customer
def view_customer():
    """Retrieves details of a specific listing along with category and broker information."""
    # Implement the SQL query to retrieve listing details with JOIN
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute("SELECT * FROM customer ORDER BY id ASC")
                print("Got all listing successfully")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


# Read customer by id
def view_customer_by_id(id):
    """Retrieves details of a specific customer along with customer and customer information."""
    # Implement the SQL query to retrieve customer details with JOIN
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute("SELECT * FROM customer WHERE id = %s", (id,))
                print("Got specific customer by id successfully")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


# Update a customer by id
def update_customer(id, name, email, contact_info):
    """Updates an existing customer."""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute(
                    "UPDATE customer SET name = %s, email = %s, contact_info = %s WHERE id = %s", (name, email, contact_info, id))
                connection.commit()
                print("Updated customer by id successfully")
                return True
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False


# Delete a customer by id
def delete_customer(id):
    """Deletes a customer from the database."""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute("DELETE FROM customer WHERE id = %s", (id,))
                affected_rows = cur.rowcount  # Get the number of affected rows
                connection.commit()
                print("Deleted customer successfully")
                return affected_rows > 0  # Return True if any rows were deleted
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False


# ================================= END ================================================


# ================================= STARTING crud for 2 JUNCTION TABLES ================================================


# ================================= listing_customer crud ================================================


# Create listing_customer
def create_appointment(listing_id, customer_id, appointment):
    """Creates a new viewing appointment."""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO listing_customer (listing_id, customer_id, appointment) VALUES (%s, %s)", (
                        listing_id, customer_id, appointment)
                )
                connection.commit()
                print("Created an appointment in listing_customer successfully")
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False


# Read listing_customer
def view_listing_customer():
    """Retrieves details of a specific listing along with category and broker information."""
    # Implement the SQL query to retrieve listing details with JOIN
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                # (extra) ORDER BY id ASC
                cur.execute("SELECT * FROM listing_customer")
                print("Got all listing_customer successfully")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


# Read listing_customer by id
def view_listing_customer_by_id(customer_id):
    """Retrieves all appointments from listing_customer for a specific customer."""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute(
                    "SELECT * FROM listing_customer WHERE customer_id = %s", (customer_id,))
                print("Update an appointment from listing_customer")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


# Update listing_customer
def update_listing_customer(appointments, listing_id, customer_id):
    """Updates an listing_customer"""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute(
                    "Update listing_customer SET appointments = %s WHERE listing_id = %s AND customer_id = %s", (appointments, listing_id, customer_id))
                print("Update an appointment from listing_customer")
                # Den kollar om någon rad blev påverkad av våran query. Om det blev det så returnerar det True!
                return cur.rowcount > 0
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False


# Delete listing_customer
def remove_listing_customer(customer_id, listing_id):
    """Removes an appointment."""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute(
                    "DELETE FROM listing_customer WHERE listing_id = %s AND customer_id = %s", (listing_id, customer_id))
                print("Deleted an appointment from listing_customer")
                return cur.rowcount > 0  # Return True if any rows were deleted
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False


# ================================= nend new: customer_favorute_listing crud ================================================


# Create customer_favorute_listing
def create_customer_favorute_listing(listing_id, customer_id, favorite_residence):
    """Creates a new customer_favorute_listing."""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO customer_favorute_listing (listing_id, customer_id, favorite_residence) VALUES (%s, %s, %s)", (
                        listing_id, customer_id, favorite_residence)
                )
                connection.commit()
                print(
                    "Created an favorite_residence in customer_favorute_listing successfully")
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False


# Read customer_favorute_listing
def view_customer_favorute_listing():
    """Retrieves details of a specific listing along with category and broker information."""
    # Implement the SQL query to retrieve listing details with JOIN
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                # (extra) ORDER BY id ASC
                cur.execute("SELECT * FROM customer_favorute_listing")
                print("Got all customer_favorute_listing successfully")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


# Read customer_favorute_listing by id
def view_customer_favorute_listing_by_id(customer_id):
    """Retrieves all appointments from customer_favorute_listing for a specific customer."""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute(
                    "SELECT * FROM customer_favorute_listing WHERE customer_id = %s", (customer_id,))
                print("Update an appointment from customer_favorute_listing")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


# Update customer_favorute_listing
def update_customer_favorute_listing(favorite_residence, listing_id, customer_id):
    """Updates an customer_favorute_listing"""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute(
                    "Update customer_favorute_listing SET favorite_residence = %s WHERE listing_id = %s AND customer_id = %s", (favorite_residence, listing_id, customer_id))
                print("Update an appointment from customer_favorute_listing")
                # Den kollar om någon rad blev påverkad av våran query. Om det blev det så returnerar det True!
                return cur.rowcount > 0
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False


# Delete customer_favorute_listing
def remove_customer_favorute_listing(customer_id, listing_id):
    """Removes an appointment."""
    with connect_db() as connection:
        with connection.cursor() as cur:
            try:
                cur.execute(
                    "DELETE FROM customer_favorute_listing WHERE listing_id = %s AND customer_id = %s", (listing_id, customer_id))
                print("Deleted an appointment from customer_favorute_listing")
                return cur.rowcount > 0  # Return True if any rows were deleted
            except psycopg2.Error as e:
                print("Error: ", e)
                connection.rollback()
                return False

# ================================= END ================================================
