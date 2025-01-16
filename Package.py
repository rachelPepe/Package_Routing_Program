# Package class to store the details of each package
class Package:
    def __init__(self, package_id, address, city, state, zip, delivery_deadline , weight, notes, status="At Hub"):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.notes = notes
        self.status = status  #'At Hub', 'In Transit', or 'Delivered'
        self.delivery_time = None  # To track delivery time
        self.delivered_by = None  # To track which truck delivered the package

    def update_status(self, new_status):
        self.status = new_status

    def update_delivery_info(self, delivery_time, truck_id):
        self.delivery_time = delivery_time
        self.delivered_by = truck_id

