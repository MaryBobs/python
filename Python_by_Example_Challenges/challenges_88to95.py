#088
from array import *
nums = array ('i',[])
for x in range(0,5):
    num = int(input("Enter a number: "))
    nums.append(num)
nums = sorted(nums)
nums.reverse()
print(nums)
