# vehicles.py

class Vehicle:
    # CLASS VARIABLES: Shared across all instances
    college_name = "ACE Engineering College"
    total_vehicles = 0

    def __init__(self, vehicle_id, vehicle_type, capacity):
        # INSTANCE VARIABLES: Unique to each individual object
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.capacity = capacity
        Vehicle.total_vehicles += 1

    @classmethod
    def get_total_vehicles(cls):
        """Returns the total number of vehicles registered globally."""
        return cls.total_vehicles

    @staticmethod
    def validate_vehicle_id(vehicle_id):
        """Validates standard vehicle registration format (e.g., AP28Z1234)."""
        if len(vehicle_id) == 9 and vehicle_id[:2] == "AP":
            return True
        return False

    def display_info(self):
        """Base info method to be overridden by child classes."""
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Type: {self.vehicle_type}")
        print(f"Capacity: {self.capacity} seats")


class Bus(Vehicle):
    """Specialized Bus class inheriting from base Vehicle."""
    def __init__(self, vehicle_id, capacity, route_number, has_ac=False):
        super().__init__(vehicle_id, vehicle_type="Bus", capacity=capacity)
        self.route_number = route_number
        self.has_ac = has_ac

    def __str__(self):
        ac_status = "Yes" if self.has_ac else "No"
        return f"Bus [{self.vehicle_id}] | Route: {self.route_number} | Capacity: {self.capacity} | AC: {ac_status}"

    def __repr__(self):
        return f"Bus(vehicle_id='{self.vehicle_id}', route={self.route_number}, capacity={self.capacity})"

    def display_info(self):
        """Polymorphic override of parent display method."""
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Type: Bus")
        print(f"Capacity: {self.capacity} seats")
        print(f"Route Number: {self.route_number}")
        ac_status = "Yes" if self.has_ac else "No"
        print(f"AC: {ac_status}")
        print("-" * 30)


class MiniVan(Vehicle):
    """Specialized Mini-Van class inheriting from base Vehicle."""
    def __init__(self, vehicle_id, capacity, trip_purpose):
        super().__init__(vehicle_id, vehicle_type="MiniVan", capacity=capacity)
        self.trip_purpose = trip_purpose

    def __str__(self):
        return f"MiniVan [{self.vehicle_id}] | Purpose: {self.trip_purpose}"

    def __repr__(self):
        return f"MiniVan(vehicle_id='{self.vehicle_id}', capacity={self.capacity}, purpose='{self.trip_purpose}')"

    def display_info(self):
        """Polymorphic override of parent display method."""
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Type: MiniVan")
        print(f"Capacity: {self.capacity} seats")
        print(f"Trip Purpose: {self.trip_purpose}")
        print("-" * 30)