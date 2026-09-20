numbers = [2, 3, 5, 7, 8, 11]
target = 10

left = 0
right = len(numbers)-1

while left < right:

    current_sum = numbers[left]+numbers[right]

    if current_sum == target:
        print(numbers[left],numbers[right])
        break
    elif current_sum < target:
        left+=1
    else:
        right-=1