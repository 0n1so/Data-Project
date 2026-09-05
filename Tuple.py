numbers = (2, 7, 4, 3, 5, 1, 9, 6)
N = 8

i = 0


for i in range(len(numbers)):
   def find_pairs(numbers, N):
    numbers = sorted(numbers)
    left = 0
    right = len(numbers) - 1
    pairs = []

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == N:
            pairs.append((numbers[left], numbers[right]))
            left += 1
            right -= 1
        elif current_sum < N:
            left += 1
        else:
            right -= 1

    return pairs

print(find_pairs(numbers, N))

     