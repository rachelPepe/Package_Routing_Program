from datetime import datetime, timedelta

# Displays options to user
def display_menu():
    print("\nDelivery System Menu")
    print("1. View the delivery status of all packages at a specific time")
    print("2. View total mileage traveled by all trucks")
    print("3. View details of a specific package")
    print("4. Exit")
    print("-" * 40)

# Displays the user interface and responds to given input
def handle_menu_selection(trucks, package_hash_table):
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            time_input = input("Enter the time to check status (e.g., 8:35 AM): ")
            try:
                time_to_check = datetime.strptime(time_input, "%I:%M %p")
                view_package_status(trucks, package_hash_table, time_to_check)
            except ValueError:
                print("Invalid time format. Please try again.")
        elif choice == 2:
            total_mileage = sum(truck.total_distance for truck in trucks)
            print(f"\nTotal mileage traveled by all trucks: {total_mileage:.2f} miles\n")
        elif choice == 3:
            try:
                package_id = int(input("Enter the package ID: "))
                package_hash_table.lookup_package_by_id(package_id)
            except ValueError:
                print("Invalid input. Please enter a valid package ID.")
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 4.")



# Displays the status of all packages at a given time without modifying their actual status.
def view_package_status(trucks, hash_table, time_to_check):
    print(f"\nPackage status at {time_to_check.strftime('%I:%M %p')}:\n")

    for package_id, package in hash_table.items():
        status = get_package_status(package, trucks, time_to_check)
        print(f"Package {package_id}: {status} "
              f"{'(Delivered at ' + package.delivery_time.strftime('%I:%M %p') + ')' if status == 'Delivered' else ''}")

    # Total mileage
    total_mileage = sum(truck.total_distance for truck in trucks)
    print(f"\nTotal mileage traveled by all trucks: {total_mileage:.2f} miles\n")



# Determines the status of a package dynamically based on the time and returns a string indicating the package status
def get_package_status(package, trucks, time_to_check=None):
    if time_to_check is None:
        time_to_check = datetime.now()

    if package.delivery_time and package.delivery_time <= time_to_check:
        return "Delivered"
    elif any(package in truck.loaded_packages for truck in trucks) and package.delivery_time is None:
        return "In Transit"
    else:
        return "At Hub"