import time

from constants.parking_slot_type import ParkingSlotType
from constants.vehicle_category import VehicleCategory
from model.address import Address
from model.vehicle import Vehicle
from service.parking_floor import ParkingFloor, ParkingSlot
from service.parking_lot import ParkingLot

def main():
    name_of_parking_lot = "XYZ Parking Lot"
    address = Address(street="3", block="d", city="Bangalore", state="KA", country="India")

    all_slots = {
        ParkingSlotType.Compact: {
            "C1": ParkingSlot("C1", ParkingSlotType.Compact),
            "C2": ParkingSlot("C2", ParkingSlotType.Compact),
            "C3": ParkingSlot("C3", ParkingSlotType.Compact)
        },
        ParkingSlotType.Large: {
            "L1": ParkingSlot("L1", ParkingSlotType.Large),
            "L2": ParkingSlot("L2", ParkingSlotType.Large),
            "L3": ParkingSlot("L3", ParkingSlotType.Large)
        }
    }

    parking_floor = ParkingFloor("1", all_slots)
    parking_floors = [parking_floor]
    
    parking_lot = ParkingLot(name_of_parking_lot, address, parking_floors)

    vehicle = Vehicle(vehicle_number="KA-01-MA-9999", vehicle_category=VehicleCategory.Hatchback)

    ticket = parking_lot.assign_ticket(vehicle)
    print("Ticket number >>", ticket.ticket_number)

    # Persist the ticket to the database here
    time.sleep(10)  # Simulate waiting time
    price = parking_lot.scan_and_pay(ticket)
    print("Price is >>", price)

if __name__ == "__main__":
    main()
