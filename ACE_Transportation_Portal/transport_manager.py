# transport_manager.py

from vehicles import Bus, MiniVan
from drivers import Driver

class TransportManager:
    def __init__(self, manager_name):
        self.manager_name = manager_name
        # COMPOSITION: Storing multiple component class arrays internally
        self.buses = []
        self.mini_vans = []
        self.drivers = []

    def add_bus(self, bus_obj):
        if isinstance(bus_obj, Bus):
            self.buses.append(bus_obj)
            print(f"✓ Bus '{bus_obj.vehicle_id}' added successfully!")
            return True
        else:
            print("✗ Error: Object is not a Bus instance!")
            return False

    def add_minivan(self, van_obj):
        if isinstance(van_obj, MiniVan):
            self.mini_vans.append(van_obj)
            print(f"✓ MiniVan '{van_obj.vehicle_id}' added successfully!")
            return True
        else:
            print("✗ Error: Object is not a MiniVan instance!")
            return False

    def add_driver(self, driver_obj):
        if isinstance(driver_obj, Driver):
            self.drivers.append(driver_obj)
            print(f"✓ Driver '{driver_obj.name}' added successfully!")
            return True
        else:
            print("✗ Error: Object is not a Driver instance!")
            return False

    def display_all_vehicles(self):
        all_vehicles = self.buses + self.mini_vans
        if not all_vehicles:
            print("\nNo vehicles currently registered in the system.")
            return

        print(f"\n=== ACE College Vehicle Fleet - Total: {len(all_vehicles)} ===")
        for vehicle in all_vehicles:
            vehicle.display_info()  # POLYMORPHISM in action!

    def display_all_drivers(self):
        if not self.drivers:
            print("\nNo active drivers found on roster maps.")
            return
        print("\n=== All Registered Drivers ===")
        for driver in self.drivers:
            driver.display_info()

    def search_vehicle(self, vehicle_id):
        all_vehicles = self.buses + self.mini_vans
        for vehicle in all_vehicles:
            if vehicle.vehicle_id.lower() == vehicle_id.lower():
                print(f"\n✓ Vehicle found!")
                vehicle.display_info()
                return vehicle
        print(f"\n✗ Vehicle with ID '{vehicle_id}' not found.")
        return None

    def display_dashboard(self):
        print("\n" + "=" * 50)
        print("          TRANSPORT DASHBOARD")
        print("=" * 50)
        print(f"Manager: {self.manager_name}")
        print(f"Total Buses: {len(self.buses)}")
        print(f"Total MiniVans: {len(self.mini_vans)}")
        print(f"Total Drivers: {len(self.drivers)}")
        print(f"Total Vehicles: {len(self.buses) + len(self.mini_vans)}")
        print("=" * 50)