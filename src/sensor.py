from car_park import CarPark
from abc import ABC, abstractmethod
import random
class Sensor(ABC):
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        status = "(Active)" if self.is_active else "(Inactive)"
        return f"Sensor {self.id} {status}"

    def trigger(self):
        if self.is_active and self.car_park:
            if isinstance(self.car_park, CarPark):
                if self.id == 1:  # Entry sensor
                    self.car_park.add_car("NewPlateNumber")
                elif self.id == 2:  # Exit sensor
                    self.car_park.remove_car("ExistingPlateNumber")
                else:
                    raise ValueError("Invalid sensor ID")
            else:
                raise TypeError("car_park must be an instance of CarPark")
        else:
            print(f"Sensor {self.id} is inactive or not properly configured")

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")
    def trigger(self, plate):
        if self.is_active:
            self.car_park.add_car(plate)
            self.car_park._log_car_activity(plate, "entered")

class ExitSensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")

    def trigger(self, plate):
        if self.is_active:
            self.car_park.remove_car(plate)
            self.car_park._log_car_activity(plate, "exited")

    def _scan_plate(self):
        return random.choice(self.car_park.plates)
