<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    # parking_lot.py
class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def enter_vehicle(self, vehicle_number):
        """Handle entry of a new vehicle"""
        if len(self.stack) >= self.capacity:
            print(f"🚫 Parking Full! Cannot allow vehicle {vehicle_number}.")
        else:
            self.stack.append(vehicle_number)
            print(f"✅ Vehicle {vehicle_number} parked successfully.")

    def exit_vehicle(self):
        """Handle exit of the most recently parked vehicle"""
        if not self.stack:
            print("🚗 No vehicles in parking lot!")
        else:
            vehicle = self.stack.pop()
            print(f"⬅️ Vehicle {vehicle} has exited the parking lot.")

    def display(self):
        """Show current parking status"""
        if not self.stack:
            print("🅿️ Parking lot is empty.")
        else:
            print("\nCurrent Vehicles (Top = Last In):")
            for v in reversed(self.stack):
                print(f"   - {v}")
            print()


def main():
    print("=== 🚗 Welcome to the Stack-Based Parking System ===\n")
    capacity = int(input("Enter parking lot capacity: "))
    parking_lot = ParkingLot(capacity)

    while True:
        print("\n--- MENU ---")
        print("1. Enter Vehicle")
        print("2. Exit Vehicle")
        print("3. Display Parking Lot")
        print("4. Exit Program")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            vehicle_number = input("Enter vehicle number: ").upper()
            parking_lot.enter_vehicle(vehicle_number)

        elif choice == '2':
            parking_lot.exit_vehicle()

        elif choice == '3':
            parking_lot.display()

        elif choice == '4':
            print("👋 Exiting system... Have a great day!")
            break

        else:
            print("❌ Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()

</body>
</html>