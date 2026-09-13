def find_max(nums):
    mx=nums[0]
    for x in nums:
        if x >= mx:
            mx=x
    return mx

def count_even(nums):
    count=0
    for x in nums:
        if x%2==0:
            count+=1
    return count

def average(nums):
    average=nums[0]
    total=0
    for x in nums:
        total+=x
    average=total/len(nums)
    return average

nums=[3,7,2,9,4]
result=find_max(nums)
count=count_even(nums)
a=average(nums)
print(result,count,a)









#nums=[1,2,3,2,4]
#s=set()
#judge=False
#for x in nums:
#    if x in s:
#        judge=True
#        break
#    else:
#        s.add(x)
#if judge:
#    print("有重复元素")
#else:
#    print("无重复元素")










#num=[1,2,2,3,3,3,4]
#cnt={}
#for x in num:
#    cnt[x]=cnt.get(x,0)+1
#print(cnt)