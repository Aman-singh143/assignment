README.md

# User Data Management

This repository contains Python programs for managing user data. There are three main programs available:

1. **Random User Data Generator:** `random_user_data_generator.py`
2. **User Data Sorting:** `user_data_sorting.py`
3. **User Data Search:** `user_data_search.py`

## Random User Data Generator

This program retrieves random user data from the Random Data API and writes it to a CSV file named "users.csv". The program makes a GET request to the API, receives a random user's data in JSON format, and appends it to the CSV file.Each request has an interval time of 1 second, ensuring controlled data retrieval. The fetched user data is appended to the "users.csv" file in a comma-separated format.

**Program Components**

get_random_user() function: This function sends a GET request to the chosen API endpoint and fetches a random user's data in JSON format. It handles the API response, verifies the status code for a successful request, and returns the user data as a JSON object.

write_user_to_csv() function: This function takes the user data as input and writes it to the "users.csv" file. It opens the file in append mode and uses the csv.writer module to write the user's data as a new row in the CSV file. If the file is empty, it first writes the header row with the field names.

Main program: The main program controls the overall execution. It defines the number of times to retrieve random user data, indicated by the value of n. In each iteration, it calls the get_random_user() function to fetch user data, then calls the write_user_to_csv() function to append the data to the CSV file. After each iteration, it pauses for 1 second using time.sleep(1) to maintain the interval between requests.

**Example Dataset in File (with comma separation):**

```
Id,First Name,Last Name,Username,Email,Avatar,Gender,Date of Birth,Address
6421,Launa,Kunze,launa.kunze,launa.kunze@email.com,https://robohash.org/magnieosvoluptatem.png?size=300x300&set=set1,Agender,1968-03-08,"{'city': 'Lake Lavonaton', 'street_name': 'Stiedemann Parkway', 'street_address': '130 Schmeler Canyon', 'zip_code': '22331', 'state': 'Idaho', 'country': 'United States', 'coordinates': {'lat': 73.5922582917818, 'lng': 82.7581102588598}}"
3213,Emerson,Ledner,emerson.ledner,emerson.ledner@email.com,https://robohash.org/deseruntipsamrepellendus.png?size=300x300&set=set1,Genderqueer,1991-07-11,"{'city': 'Omarstad', 'street_name': 'Feeney Village', 'street_address': '133 Lora Way', 'zip_code': '08381', 'state': 'Connecticut', 'country': 'United States', 'coordinates': {'lat': 53.20538678576344, 'lng': 103.99128426947215}}"
8737,Terry,Crooks,terry.crooks,terry.crooks@email.com,https://robohash.org/quasiundeest.png?size=300x300&set=set1,Non-binary,1970-03-10,"{'city': 'Fredericfort', 'street_name': 'Bobby Turnpike', 'street_address': '58368 Leopoldo Ways', 'zip_code': '57202', 'state': 'California', 'country': 'United States', 'coordinates': {'lat': 65.48471518027168, 'lng': -123.05085065248218}}"

```

## User Data Sorting

This program reads user data from the "users.csv" file and creates a new CSV file named "users-sorted.csv" by applying a sorting algorithm. The sorting is based on a chosen field, such as firstName, Name, or Username, depending on the dataset. The program uses a sorting algorithm, implemented with the `sorted()` function, to sort the data. The sorted data is then written to the "users-sorted.csv" file.

**Code Overview**

The code consists of three main functions:

read_from_csv(): This function takes a filename as input and reads the data from the CSV file. It opens the file in read mode and uses the csv.reader to iterate over the rows. Each row is appended to a list called data. Finally, the function returns the data list containing the user data.

write_to_csv(): This function takes a filename and data as input and writes the data to a CSV file. It opens the file in write mode and uses the csv.writer to write the data to the file. It uses the writerows() method to write multiple rows at once.

main(): This function is the entry point of the program. It first calls the read_from_csv() function to read the user data from the "users.csv" file. It then applies the sorting algorithm on the user data based on the chosen field. In this code, the sorting is done based on the first name field (index 0) using the sorted() function and a lambda function as the key. The sorted data is stored in the sorted_data variable.

Next, the code inserts the header row from the original data into the sorted data at the beginning. This ensures that the header row is preserved in the sorted output.

Finally, the write_to_csv() function is called to write the sorted data to the "users-sorted.csv" file.

**Example Dataset in users-sorted.csv (sorted by firstName):**

```
Id,First Name,Last Name,Username,Email,Avatar,Gender,Date of Birth,Address
3,Alice,Jones,alicejones,alicejones@example.com,avatar3.jpg,Female,1995-03-10,789 Oak St
2,Jane,Smith,janesmith,janesmith@example.com,avatar2.jpg,Female,1992-05-15,456 Elm St
1,John,Doe,johndoe,johndoe@example.com,avatar1.jpg,Male,1990-01-01,123 Main St
```

## User Data Search

This program allows the user to input either an ID or Username of a user and retrieves the details of that user from the "users.csv" file. The program performs a search for the user based on the provided ID or Username and displays the user details if found. It provides a simple and interactive way to search for specific user information.


**Code overview**

The code consists of three main functions:

search_user_by_id(): This function takes a list of users and a search ID as input. It iterates through the list of users and checks if the ID matches the search ID. If a match is found, it returns the user details. If no match is found, it returns None.

search_user_by_username(): This function takes a list of users and a search username as input. It iterates through the list of users and checks if the username matches the search username. If a match is found, it returns the user details. If no match is found, it returns None.

main(): This function is the entry point of the program. It reads the user data from the "users.csv" file and stores it in a list called users. It prompts the user to enter an ID or Username to search for. It then calls the search_user_by_id() function to search for the user by ID. If a match is found, it displays the user details. If no match is found, it calls the search_user_by_username() function to search for the user by Username. Again, if a match is found, it displays the user details. If no match is found, it shows an error message.


```
Enter the ID or Username of the user: 2
User Found:
Id: 2
First Name: Jane
Last Name: Smith
Username: janesmith
Email: janesmith@example.com
Avatar: avatar2.jpg
Gender: Female
Date of Birth: 1992-05-15
Address: 456 Elm St
```


## Usage

To use any of the programs, follow the instructions below:

1. Clone this repository to your local machine.
2. Install the required dependencies, if any (mentioned in program-specific documentation).
3. Run the desired program using a Python interpreter (e.g., `python random_user_data_generator.py`).
4. Follow the prompts or refer to the program-specific documentation for further instructions.

