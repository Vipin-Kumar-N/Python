import random
roll = random.randint(1,6)
guess = int(input("Guess the number : "))
if guess == roll:
    print("Correct!! "+str(roll))
else:
    print("Wrong!!! "+str(roll))