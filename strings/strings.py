
# STRING PROBLEM 1 - REVERSE STRING


class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


def main():
    n = int(input())
    s = input().split()

    sol = Solution()
    sol.reverseString(s)

    print(' '.join(s))


if __name__ == "__main__":
    main()



# STRING PROBLEM 2 - VALID PALINDROME


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True


def main():
    s = input().strip()

    sol = Solution()
    result = sol.isPalindrome(s)

    print("true" if result else "false")


if __name__ == "__main__":
    main()



# STRING PROBLEM 3 - FIRST OCCURRENCE OF STRING


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            j = 0

            while j < m and haystack[i + j] == needle[j]:
                j += 1

            if j == m:
                return i

        return -1


def main():
    haystack = input().strip()
    needle = input().strip()

    sol = Solution()
    result = sol.strStr(haystack, needle)

    print(result)


if __name__ == "__main__":
    main()



# STRING PROBLEM 4 - VALID PALINDROME II


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return check(left + 1, right) or check(left, right - 1)

            left += 1
            right -= 1

        return True


def main():
    s = input().strip()

    sol = Solution()
    result = sol.validPalindrome(s)

    print("true" if result else "false")


if __name__ == "__main__":
    main()



# STRING PROBLEM 5 - LICENSE KEY FORMATTING


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()

        if not s:
            return ""

        first = len(s) % k
        result = []

        if first > 0:
            result.append(s[:first])

        for i in range(first, len(s), k):
            result.append(s[i:i + k])

        return "-".join(result)


def main():
    s = input().strip()
    k = int(input().strip())

    sol = Solution()
    result = sol.licenseKeyFormatting(s, k)

    print(result)


if __name__ == "__main__":
    main()



# STRING PROBLEM 6 - COMPARE VERSION NUMBERS


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parts1 = version1.split(".")
        parts2 = version2.split(".")

        n = max(len(parts1), len(parts2))

        for i in range(n):
            num1 = int(parts1[i]) if i < len(parts1) else 0
            num2 = int(parts2[i]) if i < len(parts2) else 0

            if num1 < num2:
                return -1

            if num1 > num2:
                return 1

        return 0


def main():
    version1 = input().strip()
    version2 = input().strip()

    sol = Solution()
    result = sol.compareVersion(version1, version2)

    print(result)


if __name__ == "__main__":
    main()



# STRING PROBLEM 7 - STRING COMPRESSION


class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            current = chars[read]
            count = 0

            while read < len(chars) and chars[read] == current:
                read += 1
                count += 1

            chars[write] = current
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


def main():
    n = int(input())
    chars = input().split()

    sol = Solution()
    result = sol.compress(chars)

    print(result)
    print(' '.join(chars[:result]))


if __name__ == "__main__":
    main()



# STRING PROBLEM 8 - ANAGRAM


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency = {}

        for ch in s:
            frequency[ch] = frequency.get(ch, 0) + 1

        for ch in t:
            if ch not in frequency:
                return False

            frequency[ch] -= 1

            if frequency[ch] < 0:
                return False

        return True


def main():
    s = input().strip()
    t = input().strip()

    sol = Solution()
    result = sol.isAnagram(s, t)

    print("true" if result else "false")


if __name__ == "__main__":
    main()



# STRING PROBLEM 9 - LONGEST COMMON PREFIX


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix


def main():
    n = int(input())
    strs = []

    for _ in range(n):
        strs.append(input().strip())

    sol = Solution()
    result = sol.longestCommonPrefix(strs)

    print(result)


if __name__ == "__main__":
    main()


# STRING PROBLEM 10 - STRING ROTATION


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        return goal in (s + s)


def main():
    s = input().strip()
    goal = input().strip()

    sol = Solution()
    result = sol.rotateString(s, goal)

    print("true" if result else "false")


if __name__ == "__main__":
    main()