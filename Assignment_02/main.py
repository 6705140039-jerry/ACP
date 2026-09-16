from rental import Vehicle, Renter, ElectricCar, Motorbike

# CampusWheels demonstration

# Create vehicles and a renter
car = Vehicle("Toyota", "Yaris", "1AB234")
electric_car = ElectricCar("Tesla", "Model 3", "EV1234", 75)
motorbike = Motorbike("Honda", "Click", "MB5678", 125)

renter = Renter("Alice", 12345)

print("Initial vehicles:")
print(car)
print(electric_car)
print(motorbike)

# Rent and return a vehicle
car.rent()
renter.rented.append(car)

print("\nAfter renting the car:")
print(car)
print("Renter's rented vehicles:", renter.rented)

car.return_vehicle()
renter.rented.remove(car)

print("\nAfter returning the car:")
print(car)
print("Renter's rented vehicles:", renter.rented)

# ValueError tests
print("\nInvalid renter tests:")

try:
    Renter("", 12345)
except ValueError as e:
    print("Bad name caught:", e)

try:
    Renter("Bob", 0)
except ValueError as e:
    print("Bad licence caught:", e)

try:
    renter.name = ""
except ValueError as e:
    print("Bad name update caught:", e)

try:
    renter.license_no = -10
except ValueError as e:
    print("Bad licence update caught:", e)

# Inheritance and polymorphism
print("\nMixed Vehicle list:")
vehicles = [car, electric_car, motorbike]

for vehicle in vehicles:
    print(vehicle)
