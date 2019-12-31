###045
##total = 0
##while total <= 50:
##    num = int(input("Enter a number: "))
##    total = total + num
##    print("The total is:",total)
##
###046
##num = 0
##while num <= 5:
##    num = int(input("Enter a number: "))
##print("The last number you entered was:", num)
##    
###047
##num1 = int(input("Enter a number: "))
##total = num1
##question = "y"
##while question == "y":
##    num2 = int(input("Enter another number: "))
##    total = total + num2
##    question = input("Do you want to enter another number? (y/n) ")
##print("The total is: ",total)
##
###048
##count = 0
##inviteGuest = "y"
##while inviteGuest == "y":
##    name = input("Enter the name of your guest: ")
##    print(name,"has now been invited")
##    count = count + 1
##    inviteGuest = input("Do you want to invite another guest? (y/n) ")
##print("There are",count,"guests")
##
###049
##compnum = 50
##count = 1
##num1 = int(input("Can you guess the number I am thinking of? "))
##while num1 != compnum:
##    if num1 < compnum:
##        print("Too low")
##    else:
##        print("Too high")
##    count = count + 1
##    num1 = int(input("Enter a number: "))
##print("Well done, you took",count,"attempts")
##
###050
##num1 = int(input("Please enter a number: "))
##while num1 < 10 or num1 > 20:
##    if num1 < 10:
##        print("Too low")
##    else:
##        print("Too high")
##    num1 = int(input("Please try again: "))
##print("Thank you")

#051
num = 10
while num > 0:
    print("There are",num,"green bottles hanging on the wall")
    print("and if 1 green bottle should accidentally fall")
    num = num -1
    guess = int(input("How many green bottles will be hanging on the wall? "))
    if guess == num:
        ("There will be",num,"green bottles hanging on the wall")
    else:
        while guess != num:
            guess = int(input("No, try again: "))
print("There are no more green bottles hanging on the wall") 
        
        
