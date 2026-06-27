# routes.py

# 1. LIST: Bus stops for Route 1 (Ordered, mutable)
route_1_stops = ["College Gate", "ATC Cross", "Nayapur"]

# 2. TUPLE: Fixed GPS Coordinates of a primary depot stop (Immutable)
stop_coordinates = (17.4939, 78.3996)

# 3. SET: Registered Student Pass IDs (Unique values only, no duplicates)
registered_pass_ids = {"ACE001", "ACE002", "ACE003"}

# 4. DICTIONARY: Core Bus Fleet Metadata (Key-Value pairs)
bus_fleet = {
    "bus_no": "AP28Z1234",
    "capacity": 50,
    "driver": "Suresh Kumar"
}

def display_route_stops(route_stops):
    """Prints all stops for a given route sequence."""
    print("Route Stops Sequence:")
    count = 1
    for stop in route_stops:
        print(f"  Stop {count}: {stop}")
        count = count + 1

def add_stop_route(route_stops, new_stop):
    """Adds a new stop to an existing route list."""
    route_stops.append(new_stop)
    print(f"Added stop: '{new_stop}' successfully.")

def register_student_pass(pass_set, student_id):
    """Registers a new student pass ID safely checking for duplicates."""
    if student_id in pass_set:
        print(f"Error: Pass ID {student_id} is already registered!")
    else:
        pass_set.add(student_id)
        print(f"Pass ID {student_id} registered successfully.")

def display_bus_details(bus_dict):
    """Displays key-value data of a bus profile."""
    print("--- Bus Specifications ---")
    for key, value in bus_dict.items():
        print(f"{key.replace('_', ' ').title()}: {value}")