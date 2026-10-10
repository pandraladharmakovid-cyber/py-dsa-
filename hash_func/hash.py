# Problem 1: Happy Number (Auspicious Vehicle Numbers)
class Solution1:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10
            n = total
        return n == 1

def main_1():
    n = int(input())
    sol = Solution1()
    result = sol.isHappy(n)
    print("true" if result else "false")

if __name__ == "__main__":
    main_1()


# Problem 2: Jewels and Stones (Siddhivinayak Temple Offerings)
class Solution2:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        count = 0
        for s in stones:
            if s in jewel_set:
                count += 1
        return count

def main_2():
    jewels = input()
    stones = input()
    sol = Solution2()
    result = sol.numJewelsInStones(jewels, stones)
    print(result)

if __name__ == "__main__":
    main_2()


# Problem 3: Find the Difference (Amazon Warehouse Shuffled Inventory)
class Solution3:
    def findTheDifference(self, s: str, t: str) -> str:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        for char in t:
            if counts.get(char, 0) == 0:
                return char
            counts[char] -= 1

def main_3():
    import sys
    lines = sys.stdin.read().splitlines()
    if len(lines) == 0:
        s, t = "", ""
    elif len(lines) == 1:
        s, t = "", lines[0]
    else:
        s, t = lines[0], lines[1]
    sol = Solution3()
    result = sol.findTheDifference(s, t)
    print(result)

if __name__ == "__main__":
    main_3()


# Problem 4: First Repeating Element (Payment System Transaction Log)
import sys

def main_4():
    input_data = sys.stdin.read().split()
    if not input_data:
        print("No Repetition")
        return
    n = int(input_data[0])
    transactions = [int(x) for x in input_data[1:n + 1]]
    counts = {}
    for tx in transactions:
        counts[tx] = counts.get(tx, 0) + 1
    for tx in transactions:
        if counts[tx] > 1:
            print(tx)
            return
    print("No Repetition")

if __name__ == "__main__":
    main_4()


# Problem 5: Frequency of Page Visits (Website Traffic Analytics)
import sys

def main_5():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    if n == 0:
        return
    page_ids = [int(x) for x in input_data[1:n + 1]]
    counts = {}
    for page in page_ids:
        counts[page] = counts.get(page, 0) + 1
    for page, freq in counts.items():
        print(page, freq)

if __name__ == "__main__":
    main_5()


# Problem 6: Word Pattern (Kendriya Vidyalaya Timetable Pattern)
class Solution6:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        char_to_word = {}
        word_to_char = {}
        for c, w in zip(pattern, words):
            if c in char_to_word and char_to_word[c] != w:
                return False
            if w in word_to_char and word_to_char[w] != c:
                return False
            char_to_word[c] = w
            word_to_char[w] = c
        return True

def main_6():
    pattern = input()
    s = input()
    sol = Solution6()
    result = sol.wordPattern(pattern, s)
    print("true" if result else "false")

if __name__ == "__main__":
    main_6()


# Problem 7: Minimum Window Substring (Supreme Court Legal Documents)
class Solution7:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        missing = len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            if need.get(c, 0) > 0:
                missing -= 1
            need[c] = need.get(c, 0) - 1
            if not missing:
                while need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i < J - I:
                    I, J = i, j
                need[s[i]] += 1
                missing += 1
                i += 1
        return s[I:J]

def main_7():
    s = input()
    t = input()
    sol = Solution7()
    result = sol.minWindow(s, t)
    print(result)

if __name__ == "__main__":
    main_7()


# Problem 8: Max Points on a Line (Rajasthan Land Survey Reference Points)
from math import gcd
from collections import defaultdict

class Solution8:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        ans = 1
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                slopes[(dx, dy)] += 1
            if slopes:
                current_max = max(slopes.values()) + 1
                if current_max > ans:
                    ans = current_max
        return ans

def main_8():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append([x, y])
    sol = Solution8()
    result = sol.maxPoints(points)
    print(result)

if __name__ == "__main__":
    main_8()


# Problem 9: Group Anagrams (Document Categorization)
from collections import defaultdict

class Solution9:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return list(groups.values())

def main_9():
    import sys
    words = sys.stdin.read().split()
    sol = Solution9()
    result = sol.groupAnagrams(words)
    for group in result:
        print(" ".join(group))

if __name__ == "__main__":
    main_9()


# Problem 10: Longest Consecutive Sequence (Inventory Serial Number Streaks)
class Solution10:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    streak += 1
                longest = max(longest, streak)
        return longest

def main_10():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        print(0)
        return
    nums = [int(x) for x in input_data]
    sol = Solution10()
    print(sol.longestConsecutive(nums))

if __name__ == "__main__":
    main_10()
