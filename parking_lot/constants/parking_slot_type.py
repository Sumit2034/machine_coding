from enum import Enum

class ParkingSlotType(Enum):
    TwoWheeler = "TwoWheeler"
    Compact = "Compact"
    Medium = "Medium"
    Large = "Large"

    def get_price_for_parking(self, duration: float) -> float:
        """Method to calculate the price for parking based on slot type."""
        if self == ParkingSlotType.TwoWheeler:
            return duration * 0.05
        elif self == ParkingSlotType.Compact:
            return duration * 0.075
        elif self == ParkingSlotType.Medium:
            return duration * 0.09
        elif self == ParkingSlotType.Large:
            return duration * 0.10
        else:
            raise ValueError("Invalid Parking Slot Type")
