class Car:
#    The instance_attr is only accessible from the scope of an object. The class attribute (class_attr) is accessible as both a property of the class and as a property of objects, as it’s shared between all of them.
    def __init__(self,starting_top_speed=100) :
        self.top_speed=starting_top_speed
        self.warnings=[]
    def __repr__(self):
        print('class printing')
        return 'Top speed: {} and Warnings: {}'.format(self.top_speed, len(self.warnings))

    def drive(self):
        print("I am driving but certainly not faster then {}". format(self.top_speed))
car1 = Car()

car1.drive()
Car.top_speed=200
car1.warnings.append('new warning') # instance attribute will share only to this instance
# print whole object of class Car with help of __dict__ .This method will turn out the instance attributes as a dictionary
# print(car1.__dict__)
print(car1)
car2 =Car(200)
car2.drive()
print(car2.warnings)
car3 =Car(250)
car3.drive()
print(car3.warnings)