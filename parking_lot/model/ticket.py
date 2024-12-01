from dataclasses import dataclass, field
from time import time
from typing import Optional

from model.vehicle import Vehicle
from service.parking_floor import ParkingSlot

@dataclass
class Ticket:
    ticket_number: str
    start_time: float
    end_time: Optional[float] = None
    vehicle: Vehicle = field(default=None)
    parking_slot: ParkingSlot = field(default=None)

    @staticmethod
    def create_ticket(vehicle: Vehicle, parking_slot: ParkingSlot) -> 'Ticket':
        current_time = time()  # Get current time in seconds (similar to System.currentTimeMillis() in Java)
        ticket_number = f"{vehicle.vehicle_number}{int(current_time)}"
        return Ticket(
            ticket_number=ticket_number,
            start_time=current_time,
            vehicle=vehicle,
            parking_slot=parking_slot
        )
