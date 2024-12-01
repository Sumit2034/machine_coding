from datetime import datetime
from email.headerregistry import Address
from time import time
from typing import List, Dict, Optional

from constants.parking_slot_type import ParkingSlotType
from model.ticket import Ticket
from model.vehicle import Vehicle
from service.parking_floor import ParkingFloor, ParkingSlot

class ParkingLot:
    _instance = None  # Private class variable for singleton instance

    def __new__(cls, name_of_parking_lot: str, address: Address, parking_floors: List[ParkingFloor]):
        if cls._instance is None:
            cls._instance = super(ParkingLot, cls).__new__(cls)
            cls._instance.name_of_parking_lot = name_of_parking_lot
            cls._instance.address = address
            cls._instance.parking_floors = parking_floors
        return cls._instance

    def add_floors(self, name: str, park_slots: Dict[ParkingSlotType, Dict[str, ParkingSlot]]):
        parking_floor = ParkingFloor(name, park_slots)
        self.parking_floors.append(parking_floor)

    def remove_floors(self, parking_floor: 'ParkingFloor'):
        self.parking_floors.remove(parking_floor)

    def assign_ticket(self, vehicle: Vehicle) -> Optional[Ticket]:
        parking_slot = self.get_parking_slot_for_vehicle_and_park(vehicle)
        if parking_slot is None:
            return None
        parking_ticket = self.create_ticket_for_slot(parking_slot, vehicle)
        # Persist ticket to database (implementation not shown)
        return parking_ticket

    def scan_and_pay(self, ticket: Ticket) -> float:
        end_time = time() * 1000  # You can use time.time() * 1000 for milliseconds
        ticket.parking_slot.remove_vehicle(ticket.vehicle)
        duration = (end_time - ticket.start_time) // 1000  # Duration in seconds
        price = ticket.parking_slot.parking_slot_type.get_price_for_parking(duration)
        # Persist record to database (implementation not shown)
        return price

    def create_ticket_for_slot(self, parking_slot: ParkingSlot, vehicle: Vehicle) -> Ticket:
        return Ticket.create_ticket(vehicle, parking_slot)

    def get_parking_slot_for_vehicle_and_park(self, vehicle: Vehicle) -> Optional[ParkingSlot]:
        for floor in self.parking_floors:
            parking_slot = floor.get_relevant_slot_for_vehicle_and_park(vehicle)
            if parking_slot is not None:
                return parking_slot
        return None
