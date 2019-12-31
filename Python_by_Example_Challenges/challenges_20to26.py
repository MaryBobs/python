###020
##name = input("Please enter your first name: ")
##print(len(name))
##
###021
##firstName = input("Please enter your first name: ")
##surname = input("Please enter your surname: ")
##fullName = firstName + " " + surname
##length = len(fullName)
##print(fullName, length)
##
###022
##firstname = input("Enter your first name(lowercase): ")
##surname = input("Enter your surname(lowercase): ")
##firstname = firstname.title()
##surname = surname.title()
##name = firstname + " " + surname
##print(name)
##
###023
##rhyme = input("Please enter the first line of a nursery rhyme: ")
##length = len(rhyme)
##print("that is", length, "characters long")
##start = int(input("Enter a starting number: "))
##end = int(input("Enter a ending number: "))
##print(rhyme[start:end])
##
###024
##word = input("Please enter a random word: ").upper()
##print(word)
##
###025
##firstname = input("Please enter your first name: ")
##if len(firstname) < 5:
##    surname = input("Please enter your surname: ")
##    name = firstname + surname
##    print(name.upper())
##else:
##    print(firstname.lower())
    
#025
word = input("Please enter a random word: ")
letter = word[0].lower()
length = len(word)
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    newword = word + "way"
else:
    newword = word[1:length] + letter + "ay"
print(newword.lower())
