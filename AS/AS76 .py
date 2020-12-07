nums = input("what are your 5 numbers?:").split()
maxdifference = 1000000
for i in range(len(nums)):
    for l in range(len(nums)-1):
        pos1 = abs(int(nums[i]) - int(nums[l+1]))
        if pos1 == 0:
            pass
        elif pos1 < maxdifference:
            maxdifference = pos1

print(maxdifference)
