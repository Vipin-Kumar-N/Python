class Robot:
    def __init__(self,name_val1):
        self.name = name_val1
        self.position = [0,0]
        print("My Name is",self.name)

    def eat(self):
        print("I'm Hungry")
    
    def walk(self,x):
        self.position[0] = self.position[0]+x
        print("New Position :",self.position)

class Robot_Dog(Robot):
    def make_noise(self):
        print("Woof..Woof...")

    def eat(self):
        super().eat()
        print("I want Bacon")

robotDog = Robot_Dog('Bud')
robotDog.walk(10)
robotDog.make_noise()
robotDog.eat()