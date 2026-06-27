# fare.py

from abc import ABC, abstractmethod

class FareCalculator(ABC):
    def __init__(self, student_id, distance_km):
        self.student_id = student_id
        self.distance_km = distance_km

    @abstractmethod
    def calculate_fare(self):
        pass

    @abstractmethod
    def display_fare_summary(self):
        pass

    def apply_discount(self, amount, discount_percent):
        discounted_total = amount - (amount * (discount_percent / 100))
        return discounted_total


class RouteFare(FareCalculator):
    def __init__(self, student_id, distance_km, pass_type):
        super().__init__(student_id, distance_km)
        self.pass_type = pass_type

    def calculate_fare(self):
        if self.pass_type.lower() == "monthly":
            return self.distance_km * 2.5
        elif self.pass_type.lower() == "semester":
            return self.distance_km * 12.0
        return 0.0

    def display_fare_summary(self):
        """Renders standard transport pass calculations invoice details."""
        base_fare = self.calculate_fare()
        
        # FIXED: Semester gets 10% discount, Monthly gets NO discount
        if self.pass_type.lower() == "semester":
            discount = 10
            final_fare = self.apply_discount(base_fare, discount)
        else:
            discount = 0
            final_fare = base_fare
        
        print("\n=== Route Fare Summary ===")
        print(f"Student ID: {self.student_id}")
        print(f"Distance: {self.distance_km} km")
        print(f"Pass Type: {self.pass_type}")
        print(f"Base Fare: Rs. {base_fare:.2f}")
        if discount > 0:
            print(f"Discount Applied: {discount}%")
            print(f"Final Amount: Rs. {final_fare:.2f}")
        else:
            print(f"Final Amount: Rs. {final_fare:.2f}")
        print("-" * 30)


class SpecialTripFare(FareCalculator):
    def __init__(self, student_id, distance_km, num_students):
        super().__init__(student_id, distance_km)
        self.num_students = num_students

    def calculate_fare(self):
        total_fare = self.distance_km * 5 * self.num_students
        return {
            "total_fare": total_fare,
            "per_student": total_fare / self.num_students if self.num_students > 0 else 0
        }

    def display_fare_summary(self):
        """Renders ad-hoc unique journey invoice records."""
        fare_details = self.calculate_fare()
        total = fare_details["total_fare"]
        per_student = fare_details["per_student"]
        
        print("\n=== Special Trip Fare Summary ===")
        print(f"Student ID: {self.student_id}")
        print(f"Distance: {self.distance_km} km")
        print(f"Number of Students: {self.num_students}")
        print(f"Total Fare: Rs. {total:.2f}")
        print(f"Per Student: Rs. {per_student:.2f}")
        
        # Apply 5% discount for groups larger than 20
        if self.num_students > 20:
            discounted = self.apply_discount(total, 5)
            print(f"Group Discount Applied: 5%")
            print(f"Final Total: Rs. {discounted:.2f}")
        else:
            print(f"Final Total: Rs. {total:.2f}")
        print("-" * 30)