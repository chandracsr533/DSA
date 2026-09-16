numbers = [7, 4, 9, 2, 5, 1]
n = len(numbers)

for i in range(n):

    min_index = i

    for j in range(i+1,n):

        if numbers[j] < numbers[min_index]:
            min_index = j
            
    numbers[i],numbers[min_index]=numbers[min_index],numbers[i]

print(numbers)
