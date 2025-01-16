# Hash table to store package objects with their package ids as keys
class HashTable:
    def __init__(self, initial_capacity = 40):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # updates or adds new key value pair into the hash table
    def insert(self, key, value):
        bucket_index = hash(key) % len(self.table)
        bucket_list = self.table[bucket_index]

        # update key if it already exists in bucket_list
        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = value
                return True

        # add key and value pair to end of bucket_list
        key_value = [key, value]
        bucket_list.append(key_value)
        return True

    # searches for package object by key, if found, prints out vital package information
    def lookup_package_by_id(self, key):
        bucket_index = hash(key) % len(self.table)
        bucket_list = self.table[bucket_index]

        # searches for key in the bucket_list
        for key_value in bucket_list:
            package = key_value[1]
            if package.delivery_deadline:
                deadline = package.delivery_deadline.strftime('%I:%M %p')
            else:
                deadline = "N/A"
            if key_value[0] == key:
                print(f"Package with ID:{package.package_id} was found"
                      f"\nDelivery address: {package.address}, {package.city}, {package.zip}"
                      f"\nDelivery deadline: {deadline}, Package weight: {package.weight} KILOS"
                      f"\nCurrent delivery status: {package.status}"
                      f'\nSpecial instructions: {package.notes}', end='')
                if package.status == 'Delivered':
                    print(f"\nDelivered at {package.delivery_time.strftime('%I:%M %p')} by truck {package.delivered_by}")
                elif package.status == 'In Transit':
                    print(f"\nPackage is in Transit to {package.address}")
                else:
                    print("\nPackage is still at Hub")
            else:
                print(f"Package with ID:{package.package_id} was not found")
        print("")

    # iterates over all items in the hash table, returns key-value pairs
    def items(self):
        for bucket in self.table:
            for pair in bucket:
                yield pair[0], pair[1]


    # iterates through the table and prints each packages details
    def print_table(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Bucket {i}:")
                for pair in bucket:
                    package = pair[1]
                    print(f"PackageID {package.package_id}: {package.address}, {package.city}, {package.zip}"
                          f"\nDelivery deadline: {package.delivery_deadline}, Package weight: {package.weight},"
                          f"\nWas delivered at: {package.delivery_time} by: {package.delivered_by}"
                          f"\nCurrent status: {package.status}")


    # removes item from hash table by key
    def remove(self, key):
        bucket_index = hash(key) % len(self.table)
        bucket_list = self.table[bucket_index]

        # if present, remove item with matching key from bucket_list
        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])
                return
