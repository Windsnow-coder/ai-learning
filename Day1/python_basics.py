nums=[3,7,2,9,4,9]
mx=nums[0]
pos=0
for i in range(len(nums)):
    if(nums[i]>mx):
        mx=nums[i]
        pos=i
print(mx)
print(pos)