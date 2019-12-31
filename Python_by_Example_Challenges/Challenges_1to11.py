###001
##firstName = input("Enter your first name: ")
##print("Hello", firstName)
##
###002
##firstName = input("Enter your first name: ")
##surname = input("Thank you, now enter your surname: ")
##print("Hello", firstName, surname)
##
###003
##print("What do you call a bear with no teeth?\nA gummy bear!")
##
###004
##num1 = int(input("Please enter a number: "))
##num2 = int(input("Please enter another number: "))
##answer = num1 + num2
##print("The answer is", answer)
##
###005
##num1 = int(input("Please enter your first number: "))
##num2 = int(input("Please enter your second number: "))
##num3 = int(input("Please enter your third number: "))
##answer = (num1 + num2) * num3
##print("The answer is", answer)
##
###006
##num1 = int(input("How many slices of pizza did you have to start with? "))
##num2 = int(input("How many slices have you eaten? "))
##answer = num1 - num2
##print("You have", answer, "yummy slices left!")
##
#007
##name = input("What is your name? ")
##age = int(input("What is your age? "))
##birthdayAge = age + 1
##print(name, "next birthday you will be", birthdayAge)
##
###008
##totalBill = int(input("What is the total price of the bill? "))
##diners = int(input("How many diners are there? "))
##amountToPay = totalBill/diners
##print("Each person must pay £",amountToPay)
##
###009
##days = int(input("Enter a random number of days: "))
##hours = days * 24
##minutes = hours * 60
##seconds = minutes * 60
##print("In", days, "days there are", hours, "hours,",minutes,"minutes and",seconds,"seconds!")
##
###010
##kilos = int(input("Please enter a weight in kilograms: "))
##pounds = kilos * 2.204
##print("That is",pounds,"pounds")

#011
bigNum = int(input("Please enter a number over 100: "))
smallNum = int(input("Please enter a number under 10: "))
answer = bigNum//smallNum
print(smallNum, "goes into", bigNum, answer, "times")
