from Package import Package
from datetime import datetime
import csv

# function that loads package data into a hash table in key value pairs with the package ID as the key and
# the package object as the value
def load_package_data(package_csv, hash_table):
    with open(package_csv, mode='r') as file:
        reader = csv.reader(file)
        next(reader) # skips header
        for row in reader:
            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            delivery_deadline = row[5]
            if delivery_deadline == 'EOD':  # Handle 'End of Day' case
                delivery_deadline = None
            else:
                delivery_deadline = datetime.strptime(delivery_deadline, "%I:%M %p")
            weight = float(row[6])
            notes = row[7]

            package = Package(package_id, address, city, state, zip_code, delivery_deadline,
                              weight, notes)
            hash_table.insert(package_id, package)


# function to load distance between two addresses from distanceCSV and populate 2-dimensional distance_data list
def load_distance_data(distance_csv):
    distance_data = []
    with open(distance_csv, mode='r') as file:
        reader = csv.reader(file)
        next(reader) # skips header
        for row in reader:
            # convert each row into a list of distances (float)
            distance_data.append([float(distance) for distance in row[1:]])
    return distance_data


# function to load addresses from addressCSV and store them in the address_data list
def load_address_data(address_csv):
    address_data = []
    with open(address_csv, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            address_data.append(row[0])
    return address_data
