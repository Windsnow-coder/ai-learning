def find_min(nums):
    min=nums[0]
    for x in nums:
        if x <min :
            min=x
    return min

def count_90(nums):
    count=0
    for x in nums:
        if x >= 90:
            count+=1
    return count

def count_scores(nums):
    cnt={}
    for x in nums:
        cnt[x]=cnt.get(x,0)+1
    return cnt

def average(nums):
    total=0
    for x in nums:
        total+=x
    return total/len(nums)

scores = [75, 92, 88, 63, 95, 88, 70]

mn = find_min(scores)
avg = average(scores)
high = count_90(scores)
cnt = count_scores(scores)

print(f"最低分 = {mn}")
print(f"平均分 = {avg:.2f}")
print(f"90分以上人数 = {high}")
print(f"分数统计 = {cnt}")