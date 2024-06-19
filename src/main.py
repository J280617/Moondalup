from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

# Create a car park object with the location Moondalup, capacity 100, and log_file "moondalup.txt"
car_park = CarPark(location="Moondalup", capacity=100, log_file="moondalup.txt")
car_park.write_config()

# Create an entry sensor object with id 1, is_active True, and car_park car_park
entry_sensor = EntrySensor(id=1, is_active=True, car_park=car_park)
for _ in range(10):
    entry_sensor.trigger(car_park)

# Create an exit sensor object with id 2, is_active True, and car_park car_park
exit_sensor = ExitSensor(id=2, is_active=True, car_park=car_park)
for _ in range(2):
        exit_sensor.trigger(car_park)

# Create a display object with id 1, message "Welcome to the car park.", is_on True, and car_park car_park
display = Display(id=1, message="Welcome to the car park.", is_on=True, car_park=car_park)

available_bays = car_park.available_bays

entry_sensor = EntrySensor(id=1, is_active=True, car_park=car_park)
exit_sensor = ExitSensor(id=2, is_active=True,car_park=car_park)

if __name__ == "__main__":
    print(car_park)
    print(entry_sensor)
    print(exit_sensor)
    print(f"Current number of available bays: {available_bays}")
    print(f"Display ID: {display.id}")
    print(f"Message: {display.message}")
    print(f"Is On: {display.is_on}")
    print(f"Car Park: {car_park.location}")

