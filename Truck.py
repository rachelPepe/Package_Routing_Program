from datetime import datetime

# Truck class to store information about each truck
class Truck:
    def __init__(self, truck_id):
        self.truck_id = truck_id
        self.speed = 18  # Speed in miles per hour
        self.capacity = 16  # Package capacity
        self.current_address = 'Hub'
        self.current_time = datetime.strptime("08:00 AM", "%I:%M %p")
        self.start_time = datetime.strptime("08:00 AM", "%I:%M %p") # tracks the time the truck leaves the Hub to start deliveries
        self.total_distance = 0
        self.loaded_packages =[]
        self.delivered_packages = []  # List of delivered packages
