# Rachel Pepe - Student ID: 011613072 - C950 Task Two

from UserInterface import display_menu, handle_menu_selection
from LoadingFunctions import load_address_data, load_distance_data, load_package_data
from LoadTrucks import load_truck
from NearestNeighborAlgorithm import deliver_packages
from Truck import Truck
from HashTable import HashTable

# ----------------------------------- Helper Functions ----------------------------------------------------------

# Test to see if correct packages are loaded into trucks
def check_loaded_packages(truck_1, truck_2, truck_3):
    for package in truck_2.loaded_packages:
        print("truck2", {package.package_id})
    print("")
    for package in truck_1.loaded_packages:
        print("truck1", {package.package_id})
    print("")
    for package in truck_3.loaded_packages:
        print("truck3", {package.package_id})
    print("")



# -------------------------------------- Main Code ---------------------------------------------------------------

# Creates instance of a hash table to store package objects imported from csv file
package_hash_table = HashTable()

# load the package CSV file into package_hash_table, creating instances of package objects
load_package_data('PackageCSV.csv', package_hash_table)


# 2D list that holds all the distance data between 2 addresses
distance_data = load_distance_data('DistancesCSV.csv')


# list of all available addresses to be delivered to
address_data = load_address_data('AddressCSV.csv')


# create truck objects for all 3 trucks
truck_1 = Truck(1)
truck_2 = Truck(2)
truck_3 = Truck(3)

# load all 3 trucks
load_truck(truck_1, truck_2, truck_3, package_hash_table)

# Test to see if correct packages are loaded into trucks
# check_loaded_packages(truck_1, truck_2, truck_3)


# deliver packages for each truck
deliver_packages(truck_2, package_hash_table, distance_data, address_data)
deliver_packages(truck_1, package_hash_table, distance_data, address_data)
deliver_packages(truck_3, package_hash_table, distance_data, address_data)
print("")


# display interactive user interface that allows user to view package statuses at specific times, view total
# mileage traveled by all trucks, and details of a specific package

handle_menu_selection([truck_1, truck_2, truck_3], package_hash_table)