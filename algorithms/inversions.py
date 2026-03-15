
def invertion(nums):
    x=0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i<j and nums[i]>nums[j]:
                x=x+1
    return x
            
        
list_of_nums=[2,3,8,6,1]
print(invertion(list_of_nums))
