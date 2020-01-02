###069
##countries = ("Scotland","Ireland","Iceland","Italy","Spain")
##print(countries)
##choice = input("Choose one of the countries: ").capitalize()
##print("That is in postion", countries.index(choice))
##
###070
##countries = ("Scotland","Ireland","Iceland","Italy","Spain")
##print(countries)
##choice = input("Choose one of the countries: ").capitalize()
##print("That is in postion", countries.index(choice))
##num = int(input("Please enter a number from 0 to 4: "))
##print("That is:",countries[num])
##
###071
##sports = ["running","football"]
##sports.append(input("What is your favourite sport? "))
##sports.sort()
##print(sports)
##
###072
##subjects = ["maths","science","geography","history","drama","sports"]
##print(subjects)
##subjects.remove(input("Which of these subjects is your least favorite? "))
##print(subjects)
##
###073
##foods = {}
##foods[1] = input("Enter your favourite food? ")
##foods[2] = input("and another: ")
##foods[3] = input("and another: ")
##foods[4] = input("one more: ")
##print(foods)
##item = int(input("Which food do you want to remove? "))
##del foods[item]
##print(sorted(foods.values()))
##
###074
##colours = ["red","orange","yellow","green","blue","indigo","violet","emerald","teal","mustard"]
##start = int(input("Pick a number between 0 and 4: "))
##end = int(input("Pick a number between 5 and 9: "))
##print(colours[start:end])
##
###075
##numbers_list = [123,456,789,101]
##for i in numbers_list:
##    print(i)
##number = int(input("Please enter a three digit number: "))
##if number in numbers_list:
##    print(numbers_list.index(number))
##else:
##    print("Not in list")
##
###076
##guests = []
##print("Which three guests would you like to invite, enter their names: ")
##guests.append(input("Guest 1: "))
##guests.append(input("Guest 2: "))
##guests.append(input("Guest 3: "))
##addguest = True
##while addguest == True:
##    guest = input("Would you like to invite more guests? (y/n) ")
##    if guest == "y":
##        guests.append(input("Next guest: "))
##    elif guest == 'n':
##        addguest = False
##print("You have",len(guests),"guests coming to your party")
##
###077
##guest1 = input("Enter the name of the first guest to invite: ")
##guest2 = input("Enter another name: ")
##guest3 = input("and another: ")
##guests = [guest1, guest2, guest3]
##addguest = input("Do you want to invite another guest? (y/n)")
##while addguest == "y":
##    newguest = guests.append(input("Enter another name: "))
##    addguest = input("Do you want to invite another guest? (y/n)")
##print("Your guest list is:",guests)
##choice = input("Please enter one of your guests names: ")
##print(choice,"is guest position",guests.index(choice))
##print("Do you still want to invite", choice,"to your party?")
##invite = input("(y/n) ")
##if invite == "n":
##    guests.remove(choice)
##    print("Your guest list is now:", guests)
##else:
##    print("Your list is still:", guests)
##
###078
##shows = ["Eastenders","Emmerdale","Coronation Street","Hollyoaks"]
##for i in shows:
##    print(i)
##newshow = input("Please enter another TV show: ")
##position = int(input("What postion do you want it to be in: "))
##shows.insert(position,newshow)
##print(shows)

#079
nums = []
for i in range(0,3):
    num = nums.append(int(input("Please enter a number: ")))
    print(nums)
question = input("Are you sure you want to save that last number? (y/n) ")
if question == "n":
    nums.remove(2)
    print(nums)
else:
    print(nums)
                   

               
                             

