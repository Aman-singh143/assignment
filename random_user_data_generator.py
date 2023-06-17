# Write a program to GET random data of an user and write it in a File named
# users.csv. Each GET request must have an interval time of 1 second and append the
# information in a comma separated format. You can use any open source mock rest
# api endpoints available on the internet or use Random Data API
# (https://random-data-api.com/documentation). [2 marks]

import requests
import time
import csv
 
def get_random_user():
    """Gets a random user from the Random Data API."""
    url = "https://random-data-api.com/api/v2/users"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def write_user_to_csv(user):
    """Writes a user to a CSV file."""
    with open("users.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        if csvfile.tell() == 0:
            writer.writerow([
                "Id",
                "First Name",
                "Last Name",
                "Username",
                "Email",
                "Avatar",
                "Gender",
                "Date of Birth",
                "Address"
            ])
        writer.writerow([
            user["id"],
            user["first_name"],
            user["last_name"],
            user["username"],
            user["email"],
            user["avatar"],
            user["gender"],
            user["date_of_birth"],
            user["address"]
        ])

# Number of n indicates the number of entry in csv file  
if __name__ == "__main__":
    n = 10  
    for i in range(n):
        user = get_random_user()
        write_user_to_csv(user)
        time.sleep(1)
    print("Entry Done")