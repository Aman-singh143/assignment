README.md

# User Data Management

This repository contains Python programs for managing user data. There are three main programs available:

1. **Random User Data Generator:** `random_user_data_generator.py`
2. **User Data Sorting:** `user_data_sorting.py`
3. **User Data Search:** `user_data_search.py`

## Random User Data Generator

This program fetches random user data from a REST API and writes it to a CSV file named "users.csv". The program sends GET requests to a mock REST API endpoint (e.g., Random Data API) at a 1-second interval. The retrieved user data is appended to the CSV file in a comma-separated format.

To run the program:

```shell
python random_user_data_generator.py
```

## User Data Sorting

This program reads user data from the "users.csv" file and creates a new CSV file named "users-sorted.csv" by applying a sorting algorithm on a chosen field. The sorting field can be firstName, Name, or Username, based on the dataset. The program uses the `sorted()` function to sort the data and writes the sorted data to the output file.

To run the program:

```shell
python user_data_sorting.py
```

## User Data Search

This program allows the user to input either an ID or Username of a user and retrieves the details of that user from the "users.csv" file. The program searches for the user by ID and Username and displays the user details if found. It provides a user-friendly interface for searching user data.

To run the program:

```shell
python user_data_search.py
```

Please note that all programs assume the presence of a "users.csv" file in the same directory, which contains the user data.

Feel free to explore and utilize these programs for managing user data efficiently.

