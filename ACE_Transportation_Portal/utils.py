# utils.py
# Helper Utilities

def print_banner(title):
    """Print a formatted banner"""
    print("\n" + "=" * 55)
    print(f" {title} ")
    print("=" * 55)

def validate_phone(number):
    """Check if phone number is valid (10 digits)"""
    if len(number) == 10 and number.isdigit():
        return True
    return False

def validate_license(license_num):
    """Check if license number is valid (16 characters)"""
    if len(license_num) == 16:
        return True
    return False

def format_currency(amount):
    """Format amount as currency"""
    return f"Rs. {amount:.2f}"

def get_yes_no(prompt):
    """Get yes/no input from user"""
    while True:
        response = input(prompt + " (yes/no): ").strip().lower()
        if response == "yes" or response == "y":
            return True
        elif response == "no" or response == "n":
            return False
        print("Please enter 'yes' or 'no'")