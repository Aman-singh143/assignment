import csv

def search_user_by_id(users, search_id):
    """Searches for a user by ID and returns the user details."""
    for user in users:
        if user["Id"] == search_id:
            return user
    return None

def search_user_by_username(users, search_username):
    """Searches for a user by Username and returns the user details."""
    for user in users:
        if user["Username"] == search_username:
            return user
    return None

def main():
    # Read the CSV file and store the user data
    users = []
    with open("users.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(row)

    # Prompt the user for ID or Username input
    search_input = input("Enter the ID or Username of the user: ")

    # Search for the user by ID
    user = search_user_by_id(users, search_input)

    # If user is not found by ID, search by Username
    if user is None:
        user = search_user_by_username(users, search_input)

    # Display the user details if found, otherwise show an error message
    if user:
        print("User Found:")
        for key, value in user.items():
            print(f"{key}: {value}")
    else:
        print("User not found.")

if __name__ == "__main__":
    main()
