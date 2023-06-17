README.md

# User Data Management

This repository contains Python programs for managing user data. There are three main programs available:

1. **Random User Data Generator:** `random_user_data_generator.py`
2. **User Data Sorting:** `user_data_sorting.py`
3. **User Data Search:** `user_data_search.py`

## Random User Data Generator

This program fetches random user data from a REST API and writes it to a CSV file named "users.csv". The program sends GET requests to a mock REST API endpoint, such as the Random Data API, available at [https://random-data-api.com/documentation](https://random-data-api.com/documentation). Each request has an interval time of 1 second, ensuring controlled data retrieval. The fetched user data is appended to the "users.csv" file in a comma-separated format.

**Example Dataset in File (with comma separation):**

```
Id,First Name,Last Name,Username,Email,Avatar,Gender,Date of Birth,Address
1,John,Doe,johndoe,johndoe@example.com,avatar1.jpg,Male,1990-01-01,123 Main St
2,Jane,Smith,janesmith,janesmith@example.com,avatar2.jpg,Female,1992-05-15,456 Elm St
```

## User Data Sorting

This program reads user data from the "users.csv" file and creates a new CSV file named "users-sorted.csv" by applying a sorting algorithm. The sorting is based on a chosen field, such as firstName, Name, or Username, depending on the dataset. The program uses a sorting algorithm, implemented with the `sorted()` function, to sort the data. The sorted data is then written to the "users-sorted.csv" file.

**Example Dataset in users-sorted.csv (sorted by firstName):**

```
Id,First Name,Last Name,Username,Email,Avatar,Gender,Date of Birth,Address
3,Alice,Jones,alicejones,alicejones@example.com,avatar3.jpg,Female,1995-03-10,789 Oak St
2,Jane,Smith,janesmith,janesmith@example.com,avatar2.jpg,Female,1992-05-15,456 Elm St
1,John,Doe,johndoe,johndoe@example.com,avatar1.jpg,Male,1990-01-01,123 Main St
```

## User Data Search

This program allows the user to input either an ID or Username of a user and retrieves the details of that user from the "users.csv" file. The program performs a search for the user based on the provided ID or Username and displays the user details if found. It provides a simple and interactive way to search for specific user information.

**Example Output of User Data Search (searching for user with ID 2):**

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

Feel free to explore and utilize these programs for managing user data efficiently.

## Usage

To use any of the programs, follow the instructions below:

1. Clone this repository to your local machine.
2. Install the required dependencies, if any (mentioned in program-specific documentation).
3. Run the desired program using a Python interpreter (e.g., `python random_user_data_generator.py`).
4. Follow the prompts or refer to the program-specific documentation for further instructions.

Enjoy managing your user
