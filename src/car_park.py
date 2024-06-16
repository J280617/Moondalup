from sensor import Sensor
from display import Display
class CarPark:
    def __init__(self, location = "Unknown", capacity=0, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []  # uses the first value if not None, otherwise uses the second value
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate_number):
        self.plates.append(plate_number)
        self.update_displays()

    def remove_car(self, plate_number):
        if plate_number in self.plates:
            self.plates.remove(plate_number)
            self.update_displays()
        else:
            print(f"Plate number {plate_number} is not found in the car park.")

    def update_displays(self):
        data = {
            "available_bays": self.available_bays,
            "temperature": 25
        }
        for display in self.displays:
            display.update(data)


    @property
    def available_bays(self):
        available = self.capacity - len(self.plates)
        return max(available, 0)  # Ensure available bays is not negative

