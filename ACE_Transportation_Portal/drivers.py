# drivers.py

class Driver:
    def __init__(self, driver_id, name, license_number, contact):
        self.driver_id = driver_id
        self.name = name
        self._license_number = None
        self._contact = None
        self.license_number = license_number
        self.contact = contact

    # PROPERTY: license_number - GETTER
    @property
    def license_number(self):
        return self._license_number

    # PROPERTY: license_number - SETTER
    @license_number.setter
    def license_number(self, value):
        if len(value) == 16:
            self._license_number = value
        else:
            raise ValueError("License number must be exactly 16 characters!")

    # PROPERTY: contact - GETTER
    @property
    def contact(self):
        return self._contact

    # PROPERTY: contact - SETTER
    @contact.setter
    def contact(self, value):
        if value.isdigit() and len(value) == 10:
            self._contact = value
        else:
            raise ValueError("Contact number must be exactly 10 digits!")

    # PROPERTY: contact - DELETER
    @contact.deleter
    def contact(self):
        print(f"✗ Deleting contact number: {self._contact}")
        del self._contact
        print("✓ Contact number deleted successfully!")

    def display_info(self):
        """Renders formal profile details."""
        print("\n=== Driver Information ===")
        print(f"Driver ID: {self.driver_id}")
        print(f"Name: {self.name}")
        print(f"License Number: {self._license_number if self._license_number else 'Not set'}")
        print(f"Contact: {self._contact if hasattr(self, '_contact') else 'Not set'}")
        print("-" * 30)