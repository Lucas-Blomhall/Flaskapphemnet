import requests


# ==================================== listing calls =======================================================


# create listing
def create_listing():
    movie_data = {
        "name": "createdhouse",
        "price": 40000000,
        "description": "createdhouse",
        "category_id": 1,
        "broker_id": 1
    }
    # Replace with your API URL
    response = requests.post("http://127.0.0.1:8080/listing", json=movie_data)
    if response.status_code == 201:
        print("Listing added successfully.")
    else:
        print("Failed to add movie.")


# get listing
def get_listing():
    # Replace with your API URL
    response = requests.get("http://127.0.0.1:8080/listing")
    if response.status_code == 200:
        print(response.text)
        # listings = response.json()
        # print("listings:", listings)
    else:
        print(f"Error: {response.status_code} Failed to retrieve listings.")


# get listing by id
def get_listing_by_id():
    # Replace with your API URL
    id = input("what id do you want to search for?")
    response = requests.get(f"http://127.0.0.1:8080/listing/{id}")
    if response.status_code == 200:
        print(response.text)
        # listings = response.json()
        # print("listings:", listings)
    else:
        print(f"Error: {response.status_code} Failed to retrieve listings.")


# update listing by id
def update_listing_by_id():
    listing_data = {
        "name": "hejhej",
        "price": 10000000,
        "description": "hejhej",
        "category_id": 1,
        "broker_id": 1
    }
    # Replace with your API URL
    id = input("what id do you want to search for?")
    response = requests.put(
        f"http://127.0.0.1:8080/listing/{id}", json=listing_data)
    if response.status_code == 200:
        print("Listing updated successfully.")
    else:
        print("Failed to add movie.")


# delete listing by id
def delete_listing_by_id():
    # Replace with your API URL
    id = input("what id do you want to search for?")
    response = requests.delete(f"http://127.0.0.1:8080/listing/{id}")
    if response.status_code == 200:
        print("Listing deleted successfully.")
        # listings = response.json()
        # print("listings:", listings)
    else:
        print(f"Error: {response.status_code} Failed to retrieve listings.")


# ==================================== Category calls =======================================================


# create category
def create_category():
    name = input("What name do you want in your category?")
    movie_data = {
        "name": name
    }
    # Replace with your API URL
    response = requests.post("http://127.0.0.1:8080/category", json=movie_data)
    if response.status_code == 201:
        print("Category added successfully.")
    else:
        print("Failed to add category.")


# get category
def get_category():
    # Replace with your API URL
    response = requests.get("http://127.0.0.1:8080/category")
    if response.status_code == 200:
        print(response.text)
        # categorys = response.json()
        # print("listings:", categorys)
    else:
        print(f"Error: {response.status_code} Failed to retrieve categorys.")


# get category by id
def get_category_by_id():
    # Replace with your API URL
    id = input("what id do you want to search for?")
    response = requests.get(f"http://127.0.0.1:8080/category/{id}")
    if response.status_code == 200:
        print(response.text)
        # categorys = response.json()
        # print("categorys:", categorys)
    else:
        print(f"Error: {response.status_code} Failed to retrieve categorys.")


# update category by id
def update_category_by_id():
    category_data = {
        "name": "hejhej",
        "price": 10000000,
        "description": "hejhej",
        "category_id": 1,
        "broker_id": 1
    }
    # Replace with your API URL
    id = input("what id do you want to search for?")
    response = requests.put(
        f"http://127.0.0.1:8080/category/{id}", json=category_data)
    if response.status_code == 200:
        print("Category updated successfully.")
    else:
        print("Failed to add movie.")


# delete category by id
def delete_category_by_id():
    # Replace with your API URL
    id = input("what id do you want to search for?")
    response = requests.delete(f"http://127.0.0.1:8080/category/{id}")
    if response.status_code == 200:
        print("Category deleted successfully.")
        # categorys = response.json()
        # print("categorys:", categorys)
    else:
        print(f"Error: {response.status_code} Failed to retrieve categorys.")


# ==================================== Broker calls =======================================================


# create broker
def create_broker():
    name = input("What name do you want in your broker?")
    email = input("What email do you want in your broker?")
    contact_info = input("What contact_info do you want in your broker?")
    broker_data = {
        "name": name,
        "email": email,
        "contact_info": contact_info
    }
    # Replace with your API URL
    response = requests.post("http://127.0.0.1:8080/broker", json=broker_data)
    if response.status_code == 201:
        print("Broker added successfully.")
    else:
        print("Failed to add broker.")


# get broker
def get_broker():
    # Replace with your API URL
    response = requests.get("http://127.0.0.1:8080/broker")
    if response.status_code == 200:
        print(response.text)
        # brokers = response.json()
        # print("brokers:", brokers)
    else:
        print(f"Error: {response.status_code} Failed to retrieve brokers.")


# get broker by id
def get_broker_by_id():
    # Replace with your API URL
    id = input("what id do you want to search for?")
    response = requests.get(f"http://127.0.0.1:8080/broker/{id}")
    if response.status_code == 200:
        print(response.text)
        # brokers = response.json()
        # print("brokers:", brokers)
    else:
        print(f"Error: {response.status_code} Failed to retrieve brokers.")


# update broker by id
def update_broker_by_id():
    name = input("What name do you want in your broker?")
    email = input("What email do you want in your broker?")
    contact_info = input("What contact_info do you want in your broker?")
    broker_data = {
        "name": name,
        "email": email,
        "contact_info": contact_info
    }
    # Replace with your API URL
    id = input("what id do you want to search for?")
    response = requests.put(
        f"http://127.0.0.1:8080/broker/{id}", json=broker_data)
    if response.status_code == 200:
        print("Broker updated successfully.")
    else:
        print("Failed to add broker.")


# delete broker by id
def delete_broker_by_id():
    # Replace with your API URL
    id = input("what id do you want to search for?")
    response = requests.delete(f"http://127.0.0.1:8080/broker/{id}")
    if response.status_code == 200:
        print("Broker deleted successfully.")
        # brokers = response.json()
        # print("brokers:", brokers)
    else:
        print(f"Error: {response.status_code} Failed to retrieve brokers.")


# ==================================== Customer calls =======================================================


# create customer
def create_customer():
    name = input("What name do you want in your customer?")
    email = input("What email do you want in your customer?")
    contact_info = input("What contact_info do you want in your customer?")
    customer_data = {
        "name": name,
        "email": email,
        "contact_info": contact_info
    }
    # Replace with your API URL
    response = requests.post(
        "http://127.0.0.1:8080/customer", json=customer_data)
    if response.status_code == 201:
        print("Customer added successfully.")
    else:
        print("Failed to add customer.")


# get customer
def get_customer():
    # Replace with your API URL
    response = requests.get("http://127.0.0.1:8080/customer")
    if response.status_code == 200:
        print(response.text)
        # customers = response.json()
        # print("customers:", customers)
    else:
        print(f"Error: {response.status_code} Failed to retrieve customers.")


# get customer by id
def get_customer_by_id():
    # Replace with your API URL
    id = input("what id do you want to search for?")
    response = requests.get(f"http://127.0.0.1:8080/customer/{id}")
    if response.status_code == 200:
        print(response.text)
        # customers = response.json()
        # print("customers:", customers)
    else:
        print(f"Error: {response.status_code} Failed to retrieve customers.")


# update customers by id
def update_customer_by_id():
    name = input("What name do you want in your customer?")
    email = input("What email do you want in your customer?")
    contact_info = input("What contact_info do you want in your customer?")
    customer_data = {
        "name": name,
        "email": email,
        "contact_info": contact_info
    }
    # Replace with your API URL
    id = input("what id do you want to search for?")
    response = requests.put(
        f"http://127.0.0.1:8080/customer/{id}", json=customer_data)
    if response.status_code == 200:
        print("Customer updated successfully.")
    else:
        print("Failed to add customer.")


# delete customer by id
def delete_customer_by_id():
    # Replace with your API URL
    id = input("what id do you want to search for?")
    response = requests.delete(f"http://127.0.0.1:8080/customer/{id}")
    if response.status_code == 200:
        print("Customer deleted successfully.")
        # customers = response.json()
        # print("customers:", customers)
    else:
        print(f"Error: {response.status_code} Failed to retrieve customers.")


# ==================================== listing_customer calls =======================================================


# create listing_customer
def create_listing_customer():
    listing_id = input("What listing_id do you want in your listing_customer?")
    customer_id = input(
        "What customer_id do you want in your listing_customer?")
    appointments = input(
        "What appointments do you want in your listing_customer?")
    listing_customer_data = {
        "listing_id": listing_id,
        "customer_id": customer_id,
        "appointments": appointments
    }
    # Replace with your API URL
    response = requests.post(
        "http://127.0.0.1:8080/listing_customer", json=listing_customer_data)
    if response.status_code == 201:
        print("Listing_customer added successfully.")
    else:
        print("Failed to add listing_customer.")


# get listing_customer
def get_listing_customer():
    # Replace with your API URL
    response = requests.get("http://127.0.0.1:8080/listing_customer")
    if response.status_code == 200:
        print(response.text)
        # listing_customer = response.json()
        # print("listing_customer:", listing_customer)
    else:
        print(
            f"Error: {response.status_code} Failed to retrieve listing_customer.")


# get listing_customer by id
def get_listing_customer_by_id():
    # Replace with your API URL
    customer_id = input("what customer_id do you want to search for?")
    response = requests.get(
        f"http://127.0.0.1:8080/listing_customer/{customer_id}")
    if response.status_code == 200:
        print(response.text)
        # listing_customer = response.json()
        # print("listing_customer:", listing_customer)
    else:
        print(
            f"Error: {response.status_code} Failed to retrieve listing_customer.")


# update listing_customer by id
def update_listing_customer_by_id():
    name = input("What name do you want in your listing_customer?")
    email = input("What email do you want in your listing_customer?")
    contact_info = input(
        "What contact_info do you want in your listing_customer?")
    listing_customer_data = {
        "name": name,
        "email": email,
        "contact_info": contact_info
    }
    # Replace with your API URL
    customer_id = input("what customer_id do you want to search for?")
    response = requests.put(
        f"http://127.0.0.1:8080/customer/{customer_id}", json=listing_customer_data)
    if response.status_code == 200:
        print("Listing_customer updated successfully.")
    else:
        print("Failed to add listing_customer.")


# delete listing_customer by id
def delete_listing_customer_by_id():
    # Replace with your API URL
    customer_id = input("what customer_id do you want to search for?")
    listing_id = input("what listing_id do you want to search for?")
    response = requests.delete(
        f"http://127.0.0.1:8080/listing_customer/{customer_id}/{listing_id}")
    if response.status_code == 200:
        print("Listing_customer deleted successfully.")
        # listing_customers = response.json()
        # print("listing_customers:", listing_customers)
    else:
        print(
            f"Error: {response.status_code} Failed to retrieve listing_customer.")


# ==================================== customer_favorute_listing calls =======================================================


# create customer_favorute_listing
def create_customer_favorute_listing():
    listing_id = input(
        "What listing_id do you want in your customer_favorute_listing?")
    customer_id = input(
        "What customer_id do you want in your customer_favorute_listing?")
    favorite_residence = input(
        "What favorite_residence do you want in your customer_favorute_listing?")
    customer_favorute_listing_data = {
        "listing_id": listing_id,
        "customer_id": customer_id,
        "favorite_residence": favorite_residence
    }
    # Replace with your API URL
    response = requests.post(
        "http://127.0.0.1:8080/customer_favorute_listing", json=customer_favorute_listing_data)
    if response.status_code == 201:
        print("customer_favorute_listing added successfully.")
    else:
        print("Failed to add customer_favorute_listing.")


# get customer_favorute_listing
def get_customer_favorute_listing():
    # Replace with your API URL
    response = requests.get("http://127.0.0.1:8080/customer_favorute_listing")
    if response.status_code == 200:
        print(response.text)
        # listing_customer = response.json()
        # print("listing_customer:", listing_customer)
    else:
        print(
            f"Error: {response.status_code} Failed to retrieve customer_favorute_listing.")


# get customer_favorute_listing by id
def get_customer_favorute_listing_by_id():
    # Replace with your API URL
    customer_id = input("what customer_id do you want to search for?")
    response = requests.get(
        f"http://127.0.0.1:8080/customer_favorute_listing/{customer_id}")
    if response.status_code == 200:
        print(response.text)
        # listing_customer = response.json()
        # print("listing_customer:", listing_customer)
    else:
        print(
            f"Error: {response.status_code} Failed to retrieve customer_favorute_listing.")


# update customer_favorute_listing by id
def update_customer_favorute_listing_by_id():
    listing_id = input(
        "What listing_id do you want in your customer_favorute_listing?")
    customer_id = input(
        "What customer_id do you want in your customer_favorute_listing?")
    favorite_residence = input(
        "What favorite_residence do you want in your customer_favorute_listing?")
    customer_favorute_listing_data = {
        "listing_id": listing_id,
        "customer_id": customer_id,
        "favorite_residence": favorite_residence
    }
    # Replace with your API URL
    customer_id = input("what customer_id do you want to search for?")
    listing_id = input("what listing_id do you want to search for?")
    response = requests.put(
        f"http://127.0.0.1:8080/customer_favorute_listing/{customer_id}/{listing_id}", json=customer_favorute_listing_data)
    if response.status_code == 200:
        print("customer_favorute_listing updated successfully.")
    else:
        print("Failed to add customer_favorute_listing.")


# delete customer_favorute_listing by id
def delete_customer_favorute_listing_by_id():
    # Replace with your API URL
    customer_id = input("what customer_id do you want to search for?")
    listing_id = input("what listing_id do you want to search for?")
    response = requests.delete(
        f"http://127.0.0.1:8080/customer_favorute_listing/{customer_id}/{listing_id}")
    if response.status_code == 200:
        print("customer_favorute_listing deleted successfully.")
        # listing_customers = response.json()
        # print("listing_customers:", listing_customers)
    else:
        print(
            f"Error: {response.status_code} Failed to retrieve customer_favorute_listing.")


# ==================================== END calls =======================================================


def main():
    """Displays a menu for user interaction."""

    menu_options = {
        "1": create_listing,
        "2": get_listing
    }

    while True:
        print("\nCRUD Operations Menu:")
        print(" ====== Listing calls ====== ")
        print("1. create_listing")
        print("2. get_listing")
        print("3. get_listing_by_id")
        print("4. update_listing_by_id")
        print("5. delete_listing_by_id")
        print(" ====== Category calls ====== ")
        print("6. create_category")
        print("7. get_category")
        print("8. get_category_by_id")
        print("9. update_category_by_id")
        print("10. delete_category_by_id")
        print(" ====== Broker calls ====== ")
        print("11. create_broker")
        print("12. get_broker")
        print("13. get_broker_by_id")
        print("14. update_broker_by_id")
        print("15. delete_broker_by_id")
        print(" ====== Customer calls ====== ")
        print("16. create_customer")
        print("17. get_customer")
        print("18. get_customer_by_id")
        print("19. update_customer_by_id")
        print("20. delete_customer_by_id")
        print(" ====== Listing_customer calls ====== ")
        print("21. create_listing_customer")
        print("22. get_listing_customer")
        print("23. get_listing_customer_by_id")
        print("24. update_listing_customer_by_id")
        print("25. delete_listing_customer_by_id")
        print(" ====== Customer_favorute_listing calls ====== ")
        print("26. create_customer_favorute_listing")
        print("27. get_customer_favorute_listing")
        print("28. get_customer_favorute_listing_by_id")
        print("29. update_customer_favorute_listing_by_id")
        print("30. delete_customer_favorute_listing_by_id")

        print("100. Exit")

        choice = input("Enter your choice: ")
        if choice == "100":  # does not work yet
            break

# ==================================== Listing calls =======================================================

        elif choice == "1":
            create_listing()
        elif choice == "2":
            get_listing()
        elif choice == "3":
            get_listing_by_id()
        elif choice == "4":
            update_listing_by_id()
        elif choice == "5":
            delete_listing_by_id()

# ==================================== Category calls =======================================================

        elif choice == "6":
            create_category()
        elif choice == "7":
            get_category()
        elif choice == "8":
            get_category_by_id()
        elif choice == "9":
            update_category_by_id()
        elif choice == "10":
            delete_category_by_id()


# ==================================== Broker calls =======================================================

        elif choice == "11":
            create_broker()
        elif choice == "12":
            get_broker()
        elif choice == "13":
            get_broker_by_id()
        elif choice == "14":
            update_broker_by_id()
        elif choice == "15":
            delete_broker_by_id()


# ==================================== Customer calls =======================================================

        elif choice == "16":
            create_customer()
        elif choice == "17":
            get_customer()
        elif choice == "18":
            get_customer_by_id()
        elif choice == "19":
            update_customer_by_id()
        elif choice == "20":
            delete_customer_by_id()

# ==================================== listing_customer calls =======================================================

        elif choice == "21":
            create_listing_customer()
        elif choice == "22":
            get_listing_customer()
        elif choice == "23":
            get_listing_customer_by_id()
        elif choice == "24":
            update_listing_customer_by_id()
        elif choice == "25":
            delete_listing_customer_by_id()

# ==================================== customer_favorute_listing calls =======================================================

        elif choice == "26":
            create_customer_favorute_listing()
        elif choice == "27":
            get_customer_favorute_listing()
        elif choice == "28":
            get_customer_favorute_listing_by_id()
        elif choice == "29":
            update_customer_favorute_listing_by_id()
        elif choice == "30":
            delete_customer_favorute_listing_by_id()

# ==================================== END =======================================================

# ==================================== Extra old code: =======================================================

        # elif choice in menu_options:
        #     menu_options[choice]()

# ==================================== END =======================================================

        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()
