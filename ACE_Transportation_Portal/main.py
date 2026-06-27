# main.py

from transport_manager import TransportManager
from vehicles import Bus, MiniVan, Vehicle
from drivers import Driver
from fare import RouteFare, SpecialTripFare


def display_main_menu():
    print("\n" + "=" * 55)
    print("  ACE Engineering College Transportation Portal")
    print("=" * 55)
    print("  1. Add New Bus")
    print("  2. Add New MiniVan")
    print("  3. Add New Driver")
    print("  4. Display All Vehicles")
    print("  5. Display All Drivers")
    print("  6. Calculate Route Fare")
    print("  7. Calculate Special Trip Fare")
    print("  8. Search Vehicle by ID")
    print("  9. Display Dashboard Summary")
    print("  0. Exit Portal")
    print("=" * 55)


def main():
    manager = TransportManager("Mr. Ramesh")
    
    # Pre-populate with sample data
    print("\n📦 Loading sample data...")
    try:
        bus1 = Bus("AP2821234", 50, 3, True)
        bus2 = Bus("AP2825678", 45, 1, False)
        van1 = MiniVan("TN05AB789", 12, "Industrial Visit")
        driver1 = Driver("D001", "Mr. Suresh", "AP12345678901234", "9876543210")
        
        manager.add_bus(bus1)
        manager.add_bus(bus2)
        manager.add_minivan(van1)
        manager.add_driver(driver1)
        print("✓ Sample data loaded successfully!")
    except Exception as e:
        print(f"✗ Error loading sample data: {e}")

    while True:
        display_main_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\n[ADD BUS]")
            try:
                v_id = input("Enter Vehicle ID (e.g. AP28Z1234): ").strip()
                if not Vehicle.validate_vehicle_id(v_id):
                    print("✗ Invalid Vehicle ID! Must start with 'AP' and be 9 characters.")
                    continue
                capacity = int(input("Enter Seating Capacity: "))
                route_num = int(input("Enter Assigned Route Number: "))
                ac_choice = input("Is it an AC Bus? (y/n): ").strip().lower()
                has_ac = True if ac_choice == 'y' else False
                
                new_bus = Bus(v_id, capacity, route_num, has_ac)
                manager.add_bus(new_bus)
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif choice == "2":
            print("\n[ADD MINIVAN]")
            try:
                v_id = input("Enter Vehicle ID: ").strip()
                capacity = int(input("Enter Seating Capacity: "))
                purpose = input("Enter Purpose (e.g., Industrial Visit): ").strip()
                
                new_van = MiniVan(v_id, capacity, purpose)
                manager.add_minivan(new_van)
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif choice == "3":
            print("\n[ADD DRIVER]")
            try:
                d_id = input("Enter Driver Staff ID: ").strip()
                name = input("Enter Driver Name: ").strip()
                lic = input("Enter 16-character License Plate ID: ").strip()
                phone = input("Enter 10-digit Contact Phone Number: ").strip()
                
                new_driver = Driver(d_id, name, lic, phone)
                manager.add_driver(new_driver)
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif choice == "4":
            print("\n[DISPLAY ALL VEHICLES]")
            manager.display_all_vehicles()

        elif choice == "5":
            print("\n[DISPLAY ALL DRIVERS]")
            manager.display_all_drivers()

        elif choice == "6":
            print("\n[ROUTE FARE CALCULATOR]")
            try:
                s_id = input("Student ID: ").strip()
                distance = float(input("Distance (km): "))
                p_type = input("Pass Type (Monthly/Semester): ").strip()
                
                if p_type.lower() not in ["monthly", "semester"]:
                    print("✗ Pass type must be 'Monthly' or 'Semester'")
                    continue
                
                invoice = RouteFare(s_id, distance, p_type)
                invoice.display_fare_summary()
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif choice == "7":
            print("\n[SPECIAL TRIP FARE CALCULATOR]")
            try:
                s_id = input("Coordinator Student ID: ").strip()
                distance = float(input("Total Route Distance (km): "))
                count = int(input("Number of Travelling Students: "))
                
                invoice = SpecialTripFare(s_id, distance, count)
                invoice.display_fare_summary()
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif choice == "8":
            print("\n[SEARCH VEHICLE]")
            search_id = input("Enter Vehicle ID to look up: ").strip()
            manager.search_vehicle(search_id)

        elif choice == "9":
            print("\n[DASHBOARD SUMMARY]")
            manager.display_dashboard()

        elif choice == "0":
            print("\n Thank you for using ACE Transportation Portal!")
            print(" Goodbye!\n")
            break

        else:
            print("✗ Invalid Choice. Please try options 0-9.")


if __name__ == "__main__":
    main()