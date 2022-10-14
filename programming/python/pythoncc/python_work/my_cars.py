from car import Car
from electric_car import ElectricCar

my_bettle = Car("volkswager", 'beetle', 2019)
print(my_bettle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2022)
print(my_tesla.get_descriptive_name())