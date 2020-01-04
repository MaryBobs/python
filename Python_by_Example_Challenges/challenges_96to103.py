###096
##list = [[2,5,7],[3,7,4],[1,6,9],[4,2,0]]
##
###097
##list = [[2,5,7],[3,7,4],[1,6,9],[4,2,0]]
##row = int(input("Choose a number between 0 and 3: "))
##column = int(input("Choose a number between 0 and 2: "))
##print(list[row][column])
##
###098
##list = [[2,5,7],[3,7,4],[1,6,9],[4,2,0]]
##row = int(input("Which row would you like, 0, 1 2 or 3: "))
##print(list[row])
##new = int(input("Enter a new value: "))
##list[row].append(new)
##print(list[row])
##
###099
##list = [[2,5,7],[3,7,4],[1,6,9],[4,2,0]]
##row = int(input("Which row would you like, 0, 1 2 or 3: "))
##print(list[row])
##col = int(input("Which column would you like, 0, 1 or 2: "))
##print(list[row][col])
##change = input("Do you want to amend the value? (y/n) ")
##if change == "y":
##    new = int(input("Enter the new value: "))
##    list[row][col] = new
##print(list[row])
##
###100
##sales = {"John":{"N":3056,"S":8463,"E":8441,"W":2694},
##         "Tom":{"N":4832,"S":6786,"E":4737,"W":3612},
##         "Anne":{"N":5239,"S":4802,"E":5820,"W":1859},
##         "Fiona":{"N":3904,"S":3645,"E":8821,"W":2451}}
##print(sales)
##
###101
##sales = {"John":{"N":3056,"S":8463,"E":8441,"W":2694},
##         "Tom":{"N":4832,"S":6786,"E":4737,"W":3612},
##         "Anne":{"N":5239,"S":4802,"E":5820,"W":1859},
##         "Fiona":{"N":3904,"S":3645,"E":8821,"W":2451}}
##print(sales)
##name = input("Which name do you wnat to change: ").capitalize()
##region = input("And which region: ").upper()
##print(sales[name][region])
##newsales = int(input("What is the new sales figure: "))
##sales[name][region] = newsales
##print(sales[name])
##
###102
##shoes = {}
##for i in range(0,4):
##    name = input("Enter name: ")
##    age = (input("Enter age: "))
##    shoesize = int(input("Enter shoe size: "))
##    shoes[name] = {"Age":age,"Shoe size":shoesize}
##details = input("Whose details do you want to see: ")
##print(shoes[details])
##
###103
##shoes = {}
##for i in range(0,4):
##    name = input("Enter name: ")
##    age = (input("Enter age: "))
##    shoesize = int(input("Enter shoe size: "))
##    shoes[name] = {"Age":age,"Shoe size":shoesize}
##for name in shoes:
##    print((name),shoes[name]["Age"])

#104
shoes = {}
for i in range(0,4):
    name = input("Enter name: ")
    age = (input("Enter age: "))
    shoesize = int(input("Enter shoe size: "))
    shoes[name] = {"Age":age,"Shoe size":shoesize}
delete = input("Whose details do you want to delete? ")
del shoes[delete]
for name in shoes:
    print((name),shoes[name]["Age"],shoes[name]["Shoe size"])
              
               



        
