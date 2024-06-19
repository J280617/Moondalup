import json
#from sensor import Sensor
#from display import Display
from pathlib import Path
from datetime import datetime # we'll use this to timestamp entries
class CarPark:
    def __init__(self, location = "Unknown", capacity=0, plates=None, sensors=None, displays=None, log_file=Path("log.txt"), config_file="config.json"):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []  # uses the first value if not None, otherwise uses the second value
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the file if it doesn't exist:
        self.log_file.touch(exist_ok=True)
        self.config_file = config_file

    def write_config(self, file_path="config.json"):
        with open(file_path, "w") as f:  # TODO: use self.config_file; use Path; add optional parm to __init__
            json.dump({
                "location": self.location,
                "capacity": self.capacity,
                "log_file": str(self.log_file)
            }, f)

    print("Writing to:", Path.cwd().absolute())
    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])

    # in CarPark class
    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()  # Update any display that shows the current state
            self._log_car_activity(plate, "exited")
        else:
            print(f"Plate number {plate} is not found in the car park.")

    def update_displays(self):
        data = {
            "available_bays": self.available_bays,
            "temperature": 25
        }
        for display in self.displays:
            display.update(data)

    def is_plate_in_use(self, plate):
        return plate in self.plates

    @property
    def available_bays(self):
        #available = self.capacity - len(self.plates)
        occupied_bays = len(self.plates)
        available = self.capacity - occupied_bays
        return max(available,0)  # Ensure available bays is not negative

