class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
    
    def description(self):
        print("Make of the car is " + self.make + " and the model is " + self.model + " and the year of release is " + str(self.year)) 


    def display_mileage(self):
        print("The mileage of the car is " + str(self.mileage))

    def add_mileage(self, new_mileage):
        self.mileage = self.mileage + new_mileage

jabreel_car = Car("ferrari","testarini", 2022) 

jabreel_car.description()
jabreel_car.add_mileage(20000)
jabreel_car.display_mileage()





        