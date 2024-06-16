class CarPark:
    def __init__(self, location = "Unknown", capacity=0, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []  # uses the first value if not None, otherwise uses the second value
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."
