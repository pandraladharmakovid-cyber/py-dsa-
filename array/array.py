# problem 1 

def longest_unique_substring(s):
  char_index ={}
  max_length=0
  start=0

  for end in range(len(s)):
    if s[end] in char_index and char_index[s[end]] >= start:
      start = char_index[s[end]]+1

    char_index[s[end]]=end
    max_length = max(max_length , end - start + 1 )

  return max_length 

print(longest_unique_substring("bbbbb"))

# problem 2 

a = [2, 3, 4, 5, 6, 7, 8, 9]
k = 3

def maxavgsubarray(a, k):
    sum = 0
    for i in range(k):
        sum += a[i]

    maxavg = sum/k

    for i in range(k, len(a)):
        sum = sum + a[i] - a[i - k]
        avg = sum/k
        if avg>maxavg:
            maxavg = avg

    print(maxavg)

maxavgsubarray(a, k)

#problem 3

a = [2, 3, 4, 5, 6, 7, 8, 9]
k = 3

def minavgsubarray(a, k):
    sum = 0
    for i in range(k):
        sum += a[i]

    minavg = sum/k

    for i in range(k, len(a)):
        sum = sum + a[i] - a[i - k]
        avg = sum/k
        if avg<minavg:
            minavg = avg

    print(minavg)

minavgsubarray(a, k)




# Q4 - SORT ARRAY BY PARITY


def sort_array_by_parity(nums):
    left = 0
    right = len(nums) - 1

    while left < right:

        while left < right and nums[left] % 2 == 0:
            left += 1

        while left < right and nums[right] % 2 == 1:
            right -= 1

        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums


n = int(input())
nums = list(map(int, input().split()))

result = sort_array_by_parity(nums)

print(*result)


# Q5 - BEST TIME TO BUY AND SELL STOCK II


def max_profit(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


n = int(input())
prices = list(map(int, input().split()))

print(max_profit(prices))



# Q6 - ROTATE IMAGE 90 DEGREES CLOCKWISE


def rotate(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse every row
    for row in matrix:
        row.reverse()


n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

rotate(matrix)

for row in matrix:
    print(*row)

