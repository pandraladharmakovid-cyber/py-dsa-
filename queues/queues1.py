#problem 1

from collections import deque

q = deque()
capacity = 5

n = int(input())

for _ in range(n):
    command = input().split()
    op = command[0]

    if op == "ARRIVE":
        x = int(command[1])

        if len(q) == capacity:
            print("Queue Full")
        else:
            q.append(x)

    elif op == "SERVE":
        if not q:
            print("No Customers")
        else:
            q.popleft()

    elif op == "FRONT":
        if not q:
            print("No Customers")
        else:
            print(q[0])

    elif op == "ISEMPTY":
        print("true" if not q else "false")


#problem 2

from collections import deque

q = deque()
capacity = 5

n = int(input())

for _ in range(n):
    command = input().split()
    op = command[0]

    if op == "ENQUEUE":
        x = int(command[1])

        if len(q) < capacity:
            q.append(x)

    elif op == "DEQUEUE":
        if not q:
            print("Waiting Area Empty")
        else:
            q.popleft()

    elif op == "ISEMPTY":
        print("true" if not q else "false")


#problem 3

from collections import deque

class MyQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        return self.queue.popleft()

    def peek(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0


def main():
    n = int(input())
    queue = MyQueue()

    for _ in range(n):
        line = input().split()
        op = line[0]

        if op == "push":
            queue.push(int(line[1]))
        elif op == "pop":
            print(queue.pop())
        elif op == "peek":
            print(queue.peek())
        elif op == "empty":
            print("true" if queue.empty() else "false")


if __name__ == "__main__":
    main()


#problem 4

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def _move_to_stack2(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def pop(self):
        self._move_to_stack2()
        return self.stack2.pop()

    def peek(self):
        self._move_to_stack2()
        return self.stack2[-1]

    def empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0


def main():
    n = int(input())
    queue = MyQueue()

    for _ in range(n):
        line = input().split()
        op = line[0]

        if op == "push":
            queue.push(int(line[1]))
        elif op == "pop":
            print(queue.pop())
        elif op == "peek":
            print(queue.peek())
        elif op == "empty":
            print("true" if queue.empty() else "false")


if __name__ == "__main__":
    main()


#problem 5

from collections import deque

class HitCounter:
    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp):
        self.hits.append(timestamp)

    def getHits(self, timestamp):
        start = timestamp - 299

        while self.hits and self.hits[0] < start:
            self.hits.popleft()

        return len(self.hits)


def main():
    n = int(input())
    counter = HitCounter()

    for _ in range(n):
        line = input().split()
        op = line[0]
        timestamp = int(line[1])

        if op == "hit":
            counter.hit(timestamp)
        elif op == "getHits":
            print(counter.getHits(timestamp))


if __name__ == "__main__":
    main()


#problem 6

n, k = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
zeros = 0
answer = 0

for right in range(n):
    if nums[right] == 0:
        zeros += 1

    while zeros > k:
        if nums[left] == 0:
            zeros -= 1
        left += 1

    answer = max(answer, right - left + 1)

print(answer)


#problem 7

from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        n = len(nums)

        dp = [0] * n
        dq = deque()

        dp[0] = nums[0]
        dq.append(0)

        for i in range(1, n):
            while dq and dq[0] < i - k:
                dq.popleft()

            dp[i] = nums[i] + max(0, dp[dq[0]])

            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()

            dq.append(i)

        return max(dp)


def main():
    line = input().split()
    n, k = int(line[0]), int(line[1])
    nums = list(map(int, input().split()))

    sol = Solution()
    result = sol.constrainedSubsetSum(nums, k)

    print(result)


if __name__ == "__main__":
    main()


#problem 8

from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()
        answer = n + 1

        for i in range(n + 1):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                answer = min(answer, i - dq.popleft())

            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(i)

        return answer if answer <= n else -1


def main():
    line = input().split()
    n, k = int(line[0]), int(line[1])
    nums = list(map(int, input().split()))

    sol = Solution()
    result = sol.shortestSubarray(nums, k)

    print(result)


if __name__ == "__main__":
    main()


#problem 9

class queue:
    def __init__(self, cap=8):
        self._a = [None for i in range(cap)]
        self._front = None
        self._rear = -1
        self._c = 0

    def enqueue(self, data):
        if self._c == len(self._a):
            return "overflow"

        if self._c == 0:
            self._a[self._c] = data
            self._front = 0
            self._c = 1
        else:
            self._a[self._c] = data
            self._c += 1

    def peek(self):
        if self._c == 0:
            return "no elements "
        return self._a[self._front]

    def peeklast(self):
        return self._a[self._c - 1]

    def dequeue(self):
        if self._c == 0:
            return "underflow"

        ar = [None for i in range(len(self._a))]

        for i in range(1, len(self._a)):
            ar[i - 1] = self._a[i]

        temp = self._a[0]
        self._a = ar
        self._c -= 1

        return temp

q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print(q.dequeue())
print(q.peek())


#problem 10

class queue:
    def __init__(self, cap=8):
        self._a = [None for i in range(cap)]
        self._front = None
        self._rear = -1
        self._c = 0

    def enqueue(self, data):
        if self._c == 0:
            self._a[self._c] = data
            self._front = 0
            self._c = 1
        else:
            self._a[self._c] = data
            self._c += 1

    def peek(self):
        return self._a[self._front]

    def peeklast(self):
        return self._a[self._c - 1]

    def dequeue(self):
        ar = [None for i in range(len(self._a))]

        for i in range(1, len(self._a)):
            ar[i - 1] = self._a[i]

        temp = self._a[0]
        self._a = ar
        self._c -= 1

        return temp

q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())
print(q.peek())


#problem 11

class queue:
    def __init__(self, cap=8):
        self._a = [None for i in range(cap)]
        self._front = None
        self._rear = -1
        self._c = 0

    def enqueue(self, data):
        if self._c == 0:
            self._a[self._c] = data
            self._front = 0
            self._c = 1
        else:
            self._a[self._c] = data
            self._c += 1

    def peek(self):
        return self._a[self._front]

    def peeklast(self):
        return self._a[self._c - 1]

    def dequeue(self):
        ar = [None for i in range(len(self._a))]

        for i in range(1, len(self._a)):
            ar[i - 1] = self._a[i]

        temp = self._a[0]
        self._a = ar
        self._c -= 1

        return temp

q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())


#problem 12

class queue:
    def __init__(self, cap=8):
        self._a = [None for i in range(cap)]
        self._front = None
        self._rear = -1
        self._c = 0

    def enqueue(self, data):
        if self._c == 0:
            self._a[self._c] = data
            self._front = 0
            self._c = 1
        else:
            self._a[self._c] = data
            self._c += 1

    def peek(self):
        return self._a[self._front]

    def peeklast(self):
        return self._a[self._rear]

q = queue()
q.enqueue(10)
q.enqueue(20)

print(q.peek())
print(q.peeklast())