from constants.vehicle_category import VehicleCategory


class Vehicle:
    def __init__(self, vehicle_number: str, vehicle_category: VehicleCategory):
        self.vehicle_number = vehicle_number
        self.vehicle_category = vehicle_category
