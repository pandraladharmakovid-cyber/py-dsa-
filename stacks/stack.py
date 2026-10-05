# Problem 1 — Browser Navigation System

MAX_SIZE = 5

stack = []
n = int(input())

for _ in range(n):
    command = input().strip()

    if command.startswith("VISIT"):
        page = command.split()[1]

        if len(stack) == MAX_SIZE:
            print("History Full")
        else:
            stack.append(page)

    elif command == "BACK":
        if stack:
            stack.pop()

    elif command == "CURRENT":
        if stack:
            print(stack[-1])
        else:
            print("No Pages")

    elif command == "ISEMPTY":
        print("true" if len(stack) == 0 else "false")


# Problem 2 — Infix to Postfix

expression = input().strip()

stack = []
postfix = []

precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

for ch in expression:
    if ch.isalnum():
        postfix.append(ch)

    elif ch == '(':
        stack.append(ch)

    elif ch == ')':
        while stack and stack[-1] != '(':
            postfix.append(stack.pop())

        if stack:
            stack.pop()

    elif ch in precedence:
        while (
            stack
            and stack[-1] != '('
            and precedence[stack[-1]] >= precedence[ch]
        ):
            postfix.append(stack.pop())

        stack.append(ch)

while stack:
    postfix.append(stack.pop())

print(''.join(postfix))


# Problem 3 — Gilli Danda Score Tracking

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        scores = []

        for op in operations:
            if op == "C":
                scores.pop()

            elif op == "D":
                scores.append(2 * scores[-1])

            elif op == "+":
                scores.append(scores[-1] + scores[-2])

            else:
                scores.append(int(op))

        return sum(scores)


def main():
    n = int(input())
    operations = input().split()

    sol = Solution()
    result = sol.calPoints(operations)

    print(result)


if __name__ == "__main__":
    main()


# Problem 4 — Remove Outermost Parentheses

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0

        for ch in s:
            if ch == '(':
                if depth > 0:
                    result.append(ch)

                depth += 1

            else:
                depth -= 1

                if depth > 0:
                    result.append(ch)

        return ''.join(result)


def main():
    s = input().strip()

    sol = Solution()
    result = sol.removeOuterParentheses(s)

    print(result)


if __name__ == "__main__":
    main()


# Problem 5 — Make Good String

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for ch in s:
            if (
                stack
                and stack[-1].lower() == ch.lower()
                and stack[-1] != ch
            ):
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)


def main():
    s = input().strip()

    sol = Solution()
    result = sol.makeGood(s)

    print(result)


if __name__ == "__main__":
    main()


# Problem 6 — 132 Pattern

class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        n = len(nums)

        if n < 3:
            return False

        stack = []
        second = float('-inf')

        for i in range(n - 1, -1, -1):
            if nums[i] < second:
                return True

            while stack and nums[i] > stack[-1]:
                second = stack.pop()

            stack.append(nums[i])

        return False


def main():
    n = int(input())
    nums = list(map(int, input().split()))

    sol = Solution()
    result = sol.find132pattern(nums)

    print("true" if result else "false")


if __name__ == "__main__":
    main()


# Problem 7 — Exclusive Time of Functions

class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        result = [0] * n
        stack = []
        previous_time = 0

        for log in logs:
            function_id, action, timestamp = log.split(":")

            function_id = int(function_id)
            timestamp = int(timestamp)

            if action == "start":
                if stack:
                    result[stack[-1]] += timestamp - previous_time

                stack.append(function_id)
                previous_time = timestamp

            else:
                result[stack.pop()] += timestamp - previous_time + 1
                previous_time = timestamp + 1

        return result


def main():
    n = int(input())
    m = int(input())

    logs = []

    for _ in range(m):
        logs.append(input().strip())

    sol = Solution()
    result = sol.exclusiveTime(n, logs)

    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()


# Problem 8 — Next Greater Element II

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            current = nums[i % n]

            while stack and stack[-1] <= current:
                stack.pop()

            if i < n:
                if stack:
                    result[i] = stack[-1]

            stack.append(current)

        return result


def main():
    n = int(input())
    nums = list(map(int, input().split()))

    sol = Solution()
    result = sol.nextGreaterElements(nums)

    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()