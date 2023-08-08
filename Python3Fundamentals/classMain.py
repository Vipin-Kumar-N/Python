class Robot_Dog:
    def __init__(self,name_val1,breed_val1):
        self.name = name_val1
        self.breed = breed_val1
    def barking(self):
        print("Woof..Woof..")


myDog = Robot_Dog('Spot','Chihuaha')
print(myDog.breed)
print(myDog.name)
myDog.barking()