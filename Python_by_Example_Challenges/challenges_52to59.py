###052
##import random
##num = random.randint(1,100)
##print(num)
##
###053
##import random
##fruit = random.choice(["apple","pear","peach","banana","mango"])
##print(fruit)
##
###054
##import random
##coin = random.choice(["h","t"])
##guess = input("Choose heads or tails: (h/t) ")
##if guess == coin:
##    print("You win")
##else:
##    print("Bad luck")
##if coin == "h":
##    print("The computer chose heads")
##else:
##    print("The computer chose tails")
##
###055
##import random
##num = random.randint(1,5)
##guess = int(input("Can you guess the number, between 1 and 5? "))
##if guess == num:
##    print("Well done")
##else:
##    if guess > num:
##        print("Too high")
##    else:
##        print("Too low")
##    guess = int(input("Guess again: "))
##    if guess == num:
##        print("Correct")
##    else:
##        print("You lose")
##print("Computer picked",num)
##
###056
##import random
##num = random.randint(1,10)
##guess = int(input("Guess a number between 1 and 10: "))
##while guess != num:
##    guess = int(input("Guess again: "))
##print("Correct, the computer's number was", num)
##
###057
##import random
##num = random.randint(1,10)
##correct = False
##while correct == False:
##    guess = int(input("Guess a number: "))
##    if guess < num:
##        print("Too low")
##    elif guess > num:
##        print("Too high")
##    else:
##        correct = True
##
###058
##import random
##score = 0
##for i in range(0,5):
##    num1 = random.randint(1,100)
##    num2 = random.randint(1,100)
##    answer = num1 + num2
##    print("What is: ", num1, "+", num2, "= ")
##    question = int(input("Answer: "))
##    if question == answer:
##        score = score + 1
##print("Your score was", score, "out of 5")

#059
import random
colour = random.choice(["red","blue","green","purple","pink"])
print("Choose a colour from red, blue, green, purple or pink: " )
tryagain = True
while tryagain == True:
    choice = input("Enter your colour: ").lower()
    if colour == choice:
        print("Well done", colour, "is correct!")
        tryagain = False
    else:
        if colour == "red":
            print("Bet you are RED with anger you go that wrong, try again: ")
        elif colour == "blue":
            print("You are probably feeling BLUE that you got that wrong, try again: ")
        elif colour == "green":
            print("Bet you are GREEN with envy that you couldn't get that right, try again: ")
        elif colour == "purple":
             print("Bet you are PURPLE with fury you were wrong, try again: ")
        elif colour == "pink":
            print("Bet you are a bit PINK at getting that wrong, try again: ")

    
