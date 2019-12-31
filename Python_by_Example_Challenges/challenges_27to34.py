###027
##num = float(input("Please enter a number with decimal places: "))
##print(num * 2)
##
###028
##num = float(input("Please enter a number with decimal places: "))
##answer = num * 2
##print(round(answer,2))
##
###029
##import math
##num = int(input("Please enter a number over 500: "))
##answer = math.sqrt(num)
##print(round(answer,2))
##
###030
##import math
##print(round(math.pi,5))
##
###031
##import math
##radius = int(input("To find the area of a circle please enter the radius: "))
##area = math.pi*(radius**2)
##print("The area of the circle is",area)
##
###032
##import math
##radius = int(input("Enter radius: "))
##depth = int(input("Enter depth: "))
##area = math.pi*(radius**2)
##volume = area * depth
##print("The cylinder volume is:", round(volume,3))
##
###033
##num1 = int(input("Enter a number: "))
##num2 = int(input("Enter another number: "))
##ans1 = num1 // num2
##ans2 = num1 % num2
##print(num1,"divided by",num2,"is",ans1,"with",ans2,"remaining")

#034
print("""1) Square
2) Triangle
            """)
num = int(input("Enter a number: "))
if num == 1:
    side = int(input("Enter length of one side: "))
    area = side * side
    print("Area is:", area)
elif num == 2:
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: "))
    area = (base*height)/2
    print("Area is:", area)
else:
    print("Error message")
               
