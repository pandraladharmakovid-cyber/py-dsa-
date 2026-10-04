# problem 1
# Guess Number

class Solution:
    def __init__(self, pick: int = 1):
        self.pick = pick

    def guess(self, num: int) -> int:
        if num == self.pick:
            return 0
        if num < self.pick:
            return 1
        return -1

    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            result = self.guess(mid)

            if result == 0:
                return mid
            elif result < 0:
                right = mid - 1
            else:
                left = mid + 1

        return -1


def main():
    data = list(map(int, input().split()))
    n = data[0]
    pick = data[1] if len(data) > 1 else (n + 1) // 2

    sol = Solution(pick)
    result = sol.guessNumber(n)

    print(result)


if __name__ == "__main__":
    main()


# problem 2
# Arrange Coins

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n

        while left <= right:
            mid = (left + right) // 2
            coins = mid * (mid + 1) // 2

            if coins == n:
                return mid
            elif coins < n:
                left = mid + 1
            else:
                right = mid - 1

        return right


def main():
    n = int(input())

    sol = Solution()
    result = sol.arrangeCoins(n)

    print(result)


if __name__ == "__main__":
    main()


# problem 3
# Peak Index in a Mountain Array

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    sol = Solution()
    result = sol.peakIndexInMountainArray(arr)

    print(result)


if __name__ == "__main__":
    main()


# problem 4
# Single Non-Duplicate

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]


def main():
    n = int(input())
    nums = list(map(int, input().split()))

    sol = Solution()
    result = sol.singleNonDuplicate(nums)

    print(result)


if __name__ == "__main__":
    main()


# problem 5
# Next Greatest Letter

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = (left + right) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return letters[left % len(letters)]


def main():
    n = int(input())
    letters = input().split()
    target = input().strip()

    sol = Solution()
    result = sol.nextGreatestLetter(letters, target)

    print(result)


if __name__ == "__main__":
    main()


# problem 6
# Minimum Eating Speed

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left


def main():
    n, h = map(int, input().split())
    piles = list(map(int, input().split()))

    sol = Solution()
    result = sol.minEatingSpeed(piles, h)

    print(result)


if __name__ == "__main__":
    main()


# problem 7
# K-th Smallest Pair Distance

class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort()

        left = 0
        right = nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2

            count = 0
            j = 0

            for i in range(len(nums)):
                while j < len(nums) and nums[j] - nums[i] <= mid:
                    j += 1

                count += j - i - 1

            if count >= k:
                right = mid
            else:
                left = mid + 1

        return left


def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    sol = Solution()
    result = sol.smallestDistancePair(nums, k)

    print(result)


if __name__ == "__main__":
    main()


# problem 8
# Ship Packages Within D Days

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            current_weight = 0
            days_needed = 1

            for weight in weights:
                if current_weight + weight > mid:
                    days_needed += 1
                    current_weight = weight
                else:
                    current_weight += weight

            if days_needed <= days:
                right = mid
            else:
                left = mid + 1

        return left


def main():
    n, days = map(int, input().split())
    weights = list(map(int, input().split()))

    sol = Solution()
    result = sol.shipWithinDays(weights, days)

    print(result)


if __name__ == "__main__":
    main()


# problem 9
# Split Array Largest Sum

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            current_sum = 0
            groups = 1

            for num in nums:
                if current_sum + num > mid:
                    groups += 1
                    current_sum = num
                else:
                    current_sum += num

            if groups <= k:
                right = mid
            else:
                left = mid + 1

        return left


def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    sol = Solution()
    result = sol.splitArray(nums, k)

    print(result)


if __name__ == "__main__":
    main()


# problem 10
# Minimize Maximum Gas Station Distance

import math


class Solution:
    def minmaxGasDist(self, stations: list[int], k: int) -> float:
        low = 0.0
        high = float(stations[-1] - stations[0])

        for _ in range(100):
            mid = (low + high) / 2.0

            needed = 0

            for i in range(1, len(stations)):
                gap = stations[i] - stations[i - 1]

                needed += math.ceil(gap / mid) - 1

                if needed > k:
                    break

            if needed <= k:
                high = mid
            else:
                low = mid

        return high


def main():
    n, k = map(int, input().split())
    stations = list(map(int, input().split()))

    sol = Solution()
    result = sol.minmaxGasDist(stations, k)

    print(f"{result:.6f}")


if __name__ == "__main__":
    main()


# problem 11
# Selection Sort

def selectionsort(a):
    for i in range(len(a)):
        min_index = i

        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

    return a


def main():
    a = list(map(int, input().split()))
    print(selectionsort(a))


if __name__ == "__main__":
    main()


# problem 12
# Bubble Sort

def bubblesort(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

    return a


def main():
    a = list(map(int, input().split()))
    print(bubblesort(a))


if __name__ == "__main__":
    main()


# problem 13
# Linear Search

def linearsearch(ar, target):
    for i in range(len(ar)):
        if ar[i] == target:
            print(f'{target} is found at index {i}')
            return i

    print(f'{target} is not found')
    return -1


def main():
    ar = list(map(int, input().split()))
    target = int(input())

    print(linearsearch(ar, target))


if __name__ == "__main__":
    main()


# problem 14
# Binary Search

def binarysearch(a, target=17):
    l = 0
    r = len(a) - 1

    while l <= r:
        m = (l + r) // 2

        if a[m] == target:
            print(f'{target} is found at index {m}')
            return m

        elif a[m] < target:
            l = m + 1

        else:
            r = m - 1

    print(f'{target} is not found')
    return -1


def main():
    a = list(map(int, input().split()))
    target = int(input())

    print(binarysearch(a, target))


if __name__ == "__main__":
    main()