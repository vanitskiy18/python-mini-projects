def merge(left_list,right_list):
    sorted_list=[]
    left_list_index=right_list_index=0
    left_list_length,right_list_length=len(left_list),len(right_list)
    for _ in range(left_list_length+right_list_length):
        if left_list_index<left_list_length and right_list_index<right_list_length:
            if left_list[left_list_index]<=right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index+=1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index+=1
        elif left_list_index==left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index+=1
        elif right_list_index==right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index+=1
        return sorted_list
def merge_sort(nums):
    if len(nums)<=1:
        return nums
    mid=len(nums)//2
    #left_list=merge_sort(nums[:mid])
    #right_list=merge_sort(nums[mid:])
    left_half=merge_sort(nums[:mid])
    right_half=merge_sort(nums[mid:])
    final_list=[]
    while len(left_half)>0 and len(right_half)>0:
        if left_half[0]>=right_half[0]:
            final_list.append(left_half[0])
            left_half=left_half[1:]
        else:
            final_list.append(right_half[0])
            right_half=right_half[1:]
    final_list+=left_half
    final_list+=right_half
    return final_list
        
list_of_nums=[8,3,7,1,10,55]
print(merge_sort(list_of_nums))
