
def heapify(nums,heap_size,root_index):
    largest=root_index
    left_child=(2*root_index)+1
    right_child=(2*root_index)+2
    if left_child<heap_size and nums[left_child]>nums[largest]:
        largest=left_child
    if right_child<heap_size and nums[right_child]>nums[largest]:
        largest=right_child
    if largest!=root_index:
        nums[root_index],nums[largest]=nums[largest],nums[root_index]
        heapify(nums,heap_size,largest)
def heap_sort(nums):
    n=len(nums)
    for i in range(n,-1,-1):
        heapify(nums,n,i)
    for i in range(n-1,0,-1):
        nums[i],nums[0]=nums[0],nums[i]
        heapify(nums,i,0)
n=7
payments=['2023-03-29 10:05:32 BTC 1 62000','2023-03-28 08:45:13 ETH 3 2500',
          '2023-03-28 09:13:27 BTC 2 62500','2023-03-29 09:30:11 ETH 2 2550',
          '2023-03-28 10:21:00 BTC 3 62200','2023-03-29 11:40:02 ETH 1 2580',
          '2023-03-29 13:20:10 BTC 1 62050']
heap_sort(payments)
print(payments)
