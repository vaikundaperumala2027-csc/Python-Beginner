class Vehicle:
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
    def open_boot(self):
        print("Car boot opened")
class Bus(Vehicle):
    def carry_passengers(self):
        print("Bus is carrying passengers")
car = Car()
bus = Bus()
car.start()              
car.open_boot()
bus.start()
bus.carry_passengers()