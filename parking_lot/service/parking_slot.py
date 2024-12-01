

from constants.parking_slot_type import ParkingSlotType
from model.vehicle import Vehicle


class ParkingSlot:
    def __init__(self, name: str, parking_slot_type: ParkingSlotType, is_available: bool = True):
        self.name = name
        self.is_available = is_available
        self.vehicle = None  # Initially, there is no vehicle parked
        self.parking_slot_type = parking_slot_type

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.is_available = False

    def remove_vehicle(self, vehicle: Vehicle):
        if self.vehicle == vehicle:  # Check if the vehicle is the one parked
            self.vehicle = None
            self.is_available = True

    def __repr__(self):
        return f"ParkingSlot(name={self.name}, is_available={self.is_available}, vehicle={self.vehicle}, parking_slot_type={self.parking_slot_type})"
