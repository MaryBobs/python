###088
##from array import *
##nums = array ('i',[])
##for x in range(0,5):
##    num = int(input("Enter a number: "))
##    nums.append(num)
##nums = sorted(nums)
##nums.reverse()
##print(nums)
##
###089
##from array import *
##import random
##nums = array ("i",[])
##for i in range(0,5):
##    num = random.randint(0,100)
##    nums.append(num)
##for i in nums:
##    print(i)
##
###090
##from array import *
##nums = array ('i',[])
##while len(nums) < 5:
##    num = int(input("Enter a number: "))
##    if num >= 10 and num <= 20:
##        nums.append(num)
##    else:
##        print("Outside range")
##print("Thank you")
##for i in nums:
##    print(i)
##
###091
##from array import *
##nums = array ("i",[2,5,2,8,6])
##print(nums)
##choice = int(input("Choose a number from the array: "))
##print("That appears",nums.count(choice),"times")
##
###092
##from array import *
##import random
##
##nums1 = array ('i',[])
##for i in range(0,3):
##    num = int(input("Enter a number: "))
##    nums1.append(num)
##
##nums2 = array ("i",[])
##for i in range(0,5):
##    num = random.randint(0,100)
##    nums2.append(num)
##
##nums1.extend(nums2)
##nums = sorted(nums1)
##for i in nums:
##    print(i)
##
###093
##from array import *
##
##nums1 = array ('i',[])
##for i in range(0,5):
##    num = int(input("Enter a number: "))
##    nums1.append(num)
##nums1 = sorted(nums1)
##for i in nums1:
##    print(i)
##choice = int(input("Choose one of the numbers: "))
##nums1.remove(choice)
##nums2 = array ('i',[])
##nums2.append(choice)
##print(nums1)
##print(nums2)
##
###094
##from array import *
##nums = array ("i",[2,9,5,3,8])
##for i in nums:
##    print(i)
##choice = int(input("Select a number: "))
##correct = False
##while correct == False:
##    if choice in nums:
##        print("Yes, that is at position", nums.index(choice))
##        correct = True
##    else:
##        choice = int(input("Try again: "))

#095
from array import *
import math
nums = array ("f",[10.56,50.67,30.89,90.89,20.21])
num = int(input("Enter a number between 2 and 5: "))
correct = False
while correct == False:
    if num <= 5 and num >= 2:
      for i in nums:
        ans = i / num
        print(round(ans,2))
        correct = True
    else:
        num = int(input("Try again: "))
              
