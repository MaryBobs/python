###035
##name = input("Enter your name: ")
##for i in range(0,3):
##    print(name)
##
###036
##name = input("Enter your name: ")
##num = int(input("Enter a number: "))
##for i in range(0,num):
##    print(name)
##
###037
##name = input("Enter your name: ")
##for i in name:
##    print(i)
##
###038
##name = input("Enter your name: ")
##num = int(input("Enter a number: "))
##for x in range(0,num):
##    for i in name:
##        print(i)
##
###039
##num = int(input("Enter a number between 1 and 12: "))
##for i in range(1,13):
##    answer = i * num
##    print(i,"times",num,"=",answer)
##
###040
##num = int(input("Enter a number below 50: "))
##for i in range(50,num-1,-1):
##    print(i)
##
###041
##name = input("Enter your name: ")
##num = int(input("Enter a number: "))
##if num < 10:
##    for i in range(0,num):
##        print(name)
##else:
##    for i in range(0,3):
##        print("Too high!")
##
###042
##total = 0
##for i in range(0,5):
##    num = int(input("Enter a number: "))
##    answer = input("Do you want to include this number? (y/n) ")
##    if answer == "y":
##        total = total + num
##print(total)
##
###043
##direction = input("Do you want to count up or down? (u/d)")
##if direction == "u":
##    num = int(input("Enter a top number: "))
##    for i in range(1,num+1):
##        print(i)
##elif direction == "d":
##    num = int(input("Enter a number below 20: "))
##    for i in range(20,num-1,-1):
##        print(i)
##else:
##    print("I don't understand")

#044
guests = int(input("How many people do you want to invite to the party? "))
if guests < 10:
    for i in range(0,guests):
        name = input("Enter the guest name: ")
        print(name,"has been invited")
else:
    print("Too many people")
             
        
    
