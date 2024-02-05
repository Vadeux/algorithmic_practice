class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.type_place_map = {
            1: big,
            2: medium,
            3: small
        }

    def add_car(self, car_type: int) -> bool:
        if self.type_place_map[car_type] >= 1:
            self.type_place_map[car_type] -= 1
            return True
        return False


parking = ParkingSystem(1, 1, 0)
assert parking.add_car(1) is True  # return true because there is 1 available slot for a big car
assert parking.add_car(2) is True  # return true because there is 1 available slot for a big car
assert parking.add_car(3) is False  # return false because there is no available slot for a small car
assert parking.add_car(1) is False  # return false because there is no available slot for a big car. It is already occupied.
