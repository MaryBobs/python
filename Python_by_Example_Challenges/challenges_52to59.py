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

#055
import random
num = random.randint(1,5)
guess = int(input("Can you guess the number, between 1 and 5? "))
if guess == num:
    print("Well done")
else:
    if guess > num:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Guess again: "))
    if guess == num:
        print("Correct")
    else:
        print("You lose")
print("Computer picked",num)
            
