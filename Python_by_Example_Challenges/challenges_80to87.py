###080
##name = input("Enter your first name: ")
##print("Your first name is:",len(name),"characters long")
##surname = input("Enter your surname: ")
##print("Your surname is",len(surname),"characters long")
##fullname = name + " " + surname
##print("Your name:",fullname,"is",len(fullname),"characters long")
##
###081
##subject = input("Enter your favourite school subject: ")
##for letter in subject:
##    print(letter,end="-")
##
###082
##poem = ("I've nearly reached breaking point, she snapped")
##print(poem)
##start = int(input("A number between 0 and 10: "))
##end = int(input("A number between 20 and 30: "))
##print(poem[start:end])
##
###083
##word = input("Type a word in uppercase: ")
##while word.isupper() == False:
##    word = input("Try again: ")
##else:
##    print("Thank you")
##
###084
##postcode = input("Enter your postcode: ")
##print(postcode[0:2].upper())
##
###085
##name = input("Enter your name: ").lower()
##count = 0
##for i in name:
##    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
##        count = count + 1
##print("There are",count,"vowels in your name")
##
###086
##password = input("Enter your new password: ")
##passwordcheck = input("Enter it again: ")
##if password == passwordcheck:
##    print("Thank you")
##elif password.upper() == passwordcheck.upper():
##    print("They must be in the same case")
##else:
##    print("Incorrect")

#087
word = input("Enter a word: ")
word = word[::-1]
for i in word:
    print(i)
