

# loads all 3 trucks
def load_truck(truck1, truck2, truck3, hash_table):
    # Get all packages from the hash table that are not delivered yet
    packages_to_load = [pkg for _, pkg in hash_table.items() if pkg.status != 'Delivered']

    for package in packages_to_load[:]:  # Iterate over a copy to modify the original list
        if truck2 and package.package_id in [3, 18, 36, 38, 6, 25, 28, 32, 26]:
            truck2.loaded_packages.append(package)
            package.status = 'In Transit'
            packages_to_load.remove(package)
        elif truck1 and package.package_id in [14, 15, 19, 16, 13, 20, 1, 29, 30, 31, 34, 37, 40, 2, 4, 5, 7]:
            truck1.loaded_packages.append(package)
            package.status = 'In Transit'
            packages_to_load.remove(package)
        elif truck3:
            truck3.loaded_packages.append(package)
            package.status = 'In Transit'
            packages_to_load.remove(package)

    return truck1, truck2, truck3