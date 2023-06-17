import csv

def read_csv(filename):
    """Reads a CSV file and returns the data as a list of dictionaries."""
    data = []
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def write_csv(data, filename):
    """Writes data to a CSV file."""
    with open(filename, "w", newline="") as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def sort_users(data, field):
    """Sorts the user data based on the specified field."""
    sorted_data = sorted(data, key=lambda x: x[field])
    return sorted_data

if __name__ == "__main__":
    # Read the original CSV file
    users_data = read_csv("users.csv")

    # Sort the user data based on the "First Name" field
    sorted_data = sort_users(users_data, "First Name")

    # Write the sorted data to a new CSV file
    write_csv(sorted_data, "users-sorted.csv")

    print("Sorting completed. Sorted data is stored in 'users-sorted.csv'.")
