import unittest
from domain.car import Car

class TestCar(unittest.TestCase):
    


    def test_create(self):
        car=Car("C1",2007,780)
        
        self.assertEqual(car.get_fuel(),"C1")
        self.assertEqual(car.get_year(),2007)
        self.assertEqual(car.get_price(),780)
        
        
    def test_set(self):
        car=Car()
        
        car.set_fuel("C1")
        car.set_price(780)
        car.set_year(2007)
        
        self.assertEqual(car.get_fuel(),"C1")
        self.assertEqual(car.get_year(),2007)
        self.assertEqual(car.get_price(),780)
        

if __name__=="__main__":
    unittest.main()