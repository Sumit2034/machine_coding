from typing import Dict, Optional

from constants.parking_slot_type import ParkingSlotType
from constants.vehicle_category import VehicleCategory
from model.vehicle import Vehicle
from service.parking_slot import ParkingSlot


class ParkingFloor:
    def __init__(self, name: str, parking_slots: Dict[ParkingSlotType, Dict[str, ParkingSlot]]):
        self.name = name
        self.parking_slots = parking_slots

    def get_relevant_slot_for_vehicle_and_park(self, vehicle: Vehicle) -> Optional[ParkingSlot]:
        vehicle_category = vehicle.vehicle_category
        parking_slot_type = self.pick_correct_slot(vehicle_category)
        
        if parking_slot_type not in self.parking_slots:
            return None
        
        relevant_parking_slots = self.parking_slots[parking_slot_type]
        slot = None
        
        for key, parking_slot in relevant_parking_slots.items():
            if parking_slot.is_available:
                slot = parking_slot
                slot.add_vehicle(vehicle)
                break

        return slot

    @staticmethod
    def pick_correct_slot(vehicle_category: VehicleCategory) -> ParkingSlotType:
        if vehicle_category == VehicleCategory.TwoWheeler:
            return ParkingSlotType.TwoWheeler
        elif vehicle_category in {VehicleCategory.Hatchback, VehicleCategory.Sedan}:
            return ParkingSlotType.Compact
        elif vehicle_category == VehicleCategory.SUV:
            return ParkingSlotType.Medium
        elif vehicle_category == VehicleCategory.Bus:
            return ParkingSlotType.Large
        
        return None
