import unittest
from display import Display
from car_park import CarPark
class TestDisplay(unittest.TestCase):

    def setUp(self):
        self.car_park = CarPark(location="123 Example Street", capacity=100)

        self.display = Display(id=1, message="Welcome to the car park", is_on=True, car_park=self.car_park)
        #print(f"DEBUG: Display object created with car_park: {self.display.car_park}")
    # ... inside the TestDisplay class
    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.car_park, CarPark)

        # ... inside the TestDisplay class
    def test_update(self):
        self.display.update({"message": "Goodbye"})#,"is_on": False, "unknown_attribute": "value"})
        #self.assertEqual(self.display.message, "Goodbye")

if __name__ == '__main__':
    unittest.main()