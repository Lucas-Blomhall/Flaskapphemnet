<<<<<<< Updated upstream
=======
import requests


# ==================================== listing calls =======================================================


# create listing
def create_listing():
    movie_data = {
        "name": "testhouse",
        "price": 10000000,
        "description": "Science Fiction",
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
        "name": "testhouse",
        "price": 10000000,
        "description": "Science Fiction",
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


def main():
    """Displays a menu for user interaction."""

    menu_options = {
        "1": create_listing,
        "2": get_listing
    }

    while True:
        print("\nCRUD Operations Menu:")
        print("1. create_listing")
        print("2. get_listing")
        print("3. get_listing_by_id")
        print("4. update_listing_by_id")
        print("5. delete_listing_by_id")

        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == "7":  # does not work yet
            break
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
        elif choice in menu_options:
            menu_options[choice]()
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()
>>>>>>> Stashed changes
