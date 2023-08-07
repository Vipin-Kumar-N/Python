import random
ch = ['r','s','p']
score = 0
while True:
    computer_choice = random.choice(ch)
    user_choice = input("Enter choice r,p,s: ")
    if user_choice in ch:
        if computer_choice == user_choice:
            print("TIE")
        elif computer_choice == 'p' and user_choice =='s' or computer_choice == 'r' and user_choice =='p' or computer_choice == 'p' and user_choice =='r':
            score += 1
            print("User WIN")
        else:
            print("Computer WIN")
            score -=1
    else:
        if score > 0:
            print("User WINS by : "+str(score))
        elif score < 0:
            print("Computer WINS by : "+str(abs(score)))
        else:
            print("TIE")
        print("Exited")
        break