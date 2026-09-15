ar = [3,5,6,8,12,15,16,19,21]
# key = 2
key = 15  

def binary_search(ar,key):
    # l,r,mid = 0,len(ar)-1,0

    l = 0
    r = len(ar)-1
    
    while l <= r:
        mid = (l+r)//2

        if key == ar[mid]:
            return mid
        
        elif key < ar[mid]:
            r = mid-1

        else:
            l = mid+1

    return -1

print(binary_search(ar,key))


# numbers = [10, 20, 30, 40, 50, 60, 70]

# target = 60

# left = 0
# right = len(numbers) - 1

# while left <= right:

#     middle = (left+right)//2

#     if numbers[middle] == target:
#         print("Found")
#         break

#     elif numbers[middle] < target:
#         left = middle+1

#     elif numbers[middle] > target:
#         right = middle-1