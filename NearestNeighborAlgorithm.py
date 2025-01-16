from datetime import datetime, timedelta


# ---------------------------------Helper functions -----------------------------------------------------

# Handles package 9 correction
def correct_address_package_9(package, current_time):
    # Defines the correct time as 10:20 am
    correction_time = datetime.strptime("10:20 AM", "%I:%M %p")

    if current_time >= correction_time: # 10:20am in decimal hours
        package.address = "410 S State St"
        package.city = "Salt Lake City"
        package.state = "UT"
        package.zip = '84111'

def calculate_travel_time(distance):
    return timedelta(hours=distance / 18)



# ---------------------------------Nearest Neighbor Algorithm -----------------------------------------------------

# Finds the next closest address to deliver the next package using nearest neighbor approach
def find_nearest_neighbor_from_list(current_address, undelivered_packages, distance_data, address_data):
    # Get the index of the current address
    current_index = address_data.index(current_address)
    nearest_package = None
    shortest_distance = float('inf')

    # Iterate through undelivered packages to find the nearest one
    for package in undelivered_packages:
        package_index = address_data.index(package.address)  # Get the index of the package's address
        distance = distance_data[current_index][package_index]  # Get the distance from current address

        # Check if this package is closer
        if distance < shortest_distance:
            nearest_package = package
            shortest_distance = distance

    return nearest_package, shortest_distance


# Function that uses nearest neighbor approach to deliver packages
def deliver_packages(truck, hash_table, distance_data, address_data):

    current_address = 'Hub' # start at the hub
    undelivered_packages = [pkg for pkg in truck.loaded_packages if pkg.status != 'Delivered']
    truck.total_distance = 0

    # sets start times of trucks
    if truck.truck_id == 2:
        # truck 2 leaves the hub at 9:05
        truck.current_time = datetime.strptime("9:05 AM", "%I:%M %p")
        truck.start_time = truck.current_time
    elif truck.truck_id == 3:
        # truck 3 leaves the hub at 10:20 once the driver of truck 1 returns and he gets the correct
        # address for package 9
        truck.current_time = datetime.strptime("10:30 AM", "%I:%M %p")
        truck.start_time = truck.current_time


    # while there are still undelivered packages
    while undelivered_packages:
        # correct address for Package #9 at 10:20
        for package in undelivered_packages:
            if package.package_id == 9:
                correct_address_package_9(package, truck.current_time)

        # Find the nearest neighbor based on the list of undelivered packages
        nearest_package, shortest_distance = find_nearest_neighbor_from_list(current_address, undelivered_packages, distance_data, address_data)
        nearest_address = nearest_package.address
        # Print for testing
        # print(f"The closest next address is at {nearest_address}, which is {shortest_distance} miles away from the current address.")

        # Calculate travel time to the next location
        travel_time = calculate_travel_time(shortest_distance)

        # Update the truck's state and deliver the package
        truck.current_address = nearest_address
        truck.current_time += travel_time
        truck.total_distance += shortest_distance

        # Deliver all packages at the current location
        for package in undelivered_packages[:]:
            if package.address == nearest_address:
                # Skip Package #9 until after 10:20 AM
                if package.package_id == 9 and truck.current_time < datetime.strptime("10:20 AM", "%I:%M %p"):
                    continue
                package.status = 'Delivered'
                package.delivery_time = truck.current_time  # Set delivery time
                package.delivered_by = truck.truck_id
                truck.delivered_packages.append(package)
                undelivered_packages.remove(package)  # Remove the package from the undelivered list
                # Print for testing
                # print(f'Truck {truck.truck_id} delivered package {package.package_id} to {package.address} at {truck.current_time} '
                      # f'and has driven {truck.total_distance:.2f} total miles.')

        # Update for next iteration
        current_address = nearest_address


    # Return truck 1 to the hub after deliveries are done, that driver will then switch to truck 3
    # and leave the hub once he gets the correct address for package 9 at 10:20
    if truck.truck_id == 1:
        hub_index = address_data.index('Hub')
        final_distance_to_hub = distance_data[address_data.index(truck.current_address)][hub_index]
        truck.total_distance += final_distance_to_hub
        truck.current_address = 'Hub'

    # Print for testing
    # print(f"Truck {truck.truck_id} returned to the Hub. Total miles driven: {truck.total_distance:.2f}")
