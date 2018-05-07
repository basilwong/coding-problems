totalTup = ()
elements = int(input())
nums = input().split()

for i in range(0,elements):
    tempTup = (int(nums[i]),)
    totalTup = totalTup + tempTup

print (hash(totalTup))
# print (totalTup)

print(nums)

for i in range(0,8):
