class Car:
    # instance_attr is an instance attribute defined inside the constructor.
    # class_attr is a class attribute defined outside the constructor.
    top_speed=100
    warnings=[]

    def drive(self):
        print("I am driving but certainly not faster then {}". format(self.top_speed))
car1 = Car()

car1.drive()
Car.top_speed=200
car1.warnings.append('new warning') # class attribute will share this to all instances
# car1.top_speed=200
car2 =Car()
car2.drive()
print(car2.top_speed)
print(car2.warnings)
car3 =Car()
car3.drive()
print(car3.top_speed)

print(car3.warnings)