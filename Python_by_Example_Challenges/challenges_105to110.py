###105
##file = open("Numbers.txt","w")
##file.write("1, ")
##file.write("2, ")
##file.write("3, ")
##file.write("4, ")
##file.write("5, ")
##file.close()
##
###106
##file = open("Names.txt","w")
##file.write("Mary\n")
##file.write("Ed\n")
##file.write("Jeff\n")
##file.write("Ann\n")
##file.write("Joe\n")
##file.close()
##
###107
##file = open("Names.txt","r")
##print(file.read())
##file.close()
##
###108
##file = open("Names.txt","a")
##newname = input("Enter a name to add: ")
##file.write(newname + "\n")
##file.close()
##
##file = open("Names.txt","r")
##print(file.read())
##file.close()

#109
print("1) Create a new file")
print("2) Display the file")
print("3) Add a new item to the file")
choice = int(input("Make a selection 1, 2 or 3: "))
if choice == 1:
    subject = input("Enter a school subject: ")
    file = open("Subject.txt","w")
    file.write(subject + "\n")
    file.close()
elif choice == 2:
    file = open("Subject.txt","r")
    print(file.read())
    file.close()
elif choice == 3:
    subject = input("Enter a subject: ")
    file = open("Subject.txt","a")
    file.write(subject + "\n")
    file.close()
    file = open("Subject.txt","r")
    print(file.read())
    file.close()
else:
    print("Error")
    
             
