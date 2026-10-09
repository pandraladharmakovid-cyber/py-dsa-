
# Problem 1: Kth Largest Element in a Stream
import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = []
        for val in nums:
            self.add(val)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]

def main_1():
    k, n = map(int, input().split())
    nums = list(map(int, input().split())) if n > 0 else []
    
    obj = KthLargest(k, nums)
    
    q = int(input())
    for _ in range(q):
        val = int(input())
        print(obj.add(val))

if __name__ == "__main__":
    main_1()



# Problem 2: Last Player Strength / Last Stone Weight

import heapq

class Solution2:
    def lastPlayerStrength(self, strengths: list[int]) -> int:
        max_heap = [-s for s in strengths]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            
            if first != second:
                heapq.heappush(max_heap, -(first - second))
                
        return -max_heap[0] if max_heap else 0

def main_2():
    n = int(input())
    strengths = list(map(int, input().split()))
    
    sol = Solution2()
    print(sol.lastPlayerStrength(strengths))

if __name__ == "__main__":
    main_2()



# Problem 3: The K Weakest Rows in a Matrix

import heapq

class Solution3:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        heap = [(sum(row), i) for i, row in enumerate(mat)]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

def main_3():
    first_line = input().split()
    m = int(first_line[0])
    n = int(first_line[1])
    k = int(first_line[2])

    mat = []
    for _ in range(m):
        row = list(map(int, input().split()))
        mat.append(row)

    sol = Solution3()
    result = sol.kWeakestRows(mat, k)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main_3()



# Problem 4: Remove Root from Min Heap

import sys
import heapq

def main_4():
    input_data = sys.stdin.read().split()
    if not input_data:
        print("Heap Empty")
        return

    n = int(input_data[0])
    if n <= 1:
        print("Heap Empty")
        return

    heap = [int(x) for x in input_data[1:n + 1]]
    heapq.heappop(heap)

    if not heap:
        print("Heap Empty")
    else:
        print(*(heap))

if __name__ == "__main__":
    main_4()



# Problem 5: Insert into Max Heap

import sys

def insert_max_heap(heap: list[int], val: int):
    heap.append(val)
    idx = len(heap) - 1
    
    while idx > 0:
        parent = (idx - 1) // 2
        if heap[idx] > heap[parent]:
            heap[idx], heap[parent] = heap[parent], heap[idx]
            idx = parent
        else:
            break

def main_5():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    heap = [int(x) for x in input_data[1:n + 1]]
    x = int(input_data[n + 1])
    
    insert_max_heap(heap, x)
    print(*(heap))

if __name__ == "__main__":
    main_5()


# Problem 6: Seat Reservation Manager

import heapq

class SeatManager:
    def __init__(self, n: int):
        self.marker = 1
        self.available = []

    def reserve(self) -> int:
        if self.available:
            return heapq.heappop(self.available)
        seat = self.marker
        self.marker += 1
        return seat

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available, seatNumber)

def main_6():
    line1 = input().split()
    n, q = int(line1[0]), int(line1[1])

    manager = SeatManager(n)

    for _ in range(q):
        op = input().split()
        if op[0] == "reserve":
            print(manager.reserve())
        else:
            manager.unreserve(int(op[1]))

if __name__ == "__main__":
    main_6()



# Problem 7: Minimum Cost to Hire K Workers

import heapq

class Solution7:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        
        min_cost = float('inf')
        total_quality = 0
        max_heap = []
        
        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality += q
            
            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)
                
            if len(max_heap) == k:
                min_cost = min(min_cost, total_quality * ratio)
                
        return min_cost

def main_7():
    line1 = input().split()
    n, k = int(line1[0]), int(line1[1])
    quality = list(map(int, input().split()))
    wage = list(map(int, input().split()))

    sol = Solution7()
    result = sol.mincostToHireWorkers(quality, wage, k)

    print(f"{result:.5f}")

if __name__ == "__main__":
    main_7()


# Problem 8: Single-Threaded CPU

import heapq

class Solution8:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        indexed_tasks = sorted([(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))])
        
        result = []
        min_heap = []
        time = 0
        i = 0
        n = len(tasks)
        
        while len(result) < n:
            if not min_heap and time < indexed_tasks[i][0]:
                time = indexed_tasks[i][0]
                
            while i < n and indexed_tasks[i][0] <= time:
                heapq.heappush(min_heap, (indexed_tasks[i][1], indexed_tasks[i][2]))
                i += 1
                
            proc_time, idx = heapq.heappop(min_heap)
            time += proc_time
            result.append(idx)
            
        return result

def main_8():
    n = int(input())
    tasks = []
    for _ in range(n):
        enqueue, process = map(int, input().split())
        tasks.append([enqueue, process])

    sol = Solution8()
    result = sol.getOrder(tasks)

    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main_8()




# Problem 9: Kth Smallest Element in a Sorted Matrix


import heapq

class Solution9:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        min_heap = [(matrix[i][0], i, 0) for i in range(min(n, k))]
        heapq.heapify(min_heap)
        
        val = 0
        for _ in range(k):
            val, r, c = heapq.heappop(min_heap)
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
                
        return val

def main_9():
    n, k = map(int, input().split())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
        
    sol = Solution9()
    print(sol.kthSmallest(matrix, k))

if __name__ == "__main__":
    main_9()


# Problem 10: Continuous Median from Data Stream

import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max heap (inverted numbers)
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0

def main_10():
    q = int(input())
    mf = MedianFinder()
    for _ in range(q):
        line = input().split()
        if line[0] == "add":
            mf.addNum(int(line[1]))
        elif line[0] == "find":
            print(f"{mf.findMedian():.1f}")

if __name__ == "__main__":
    main_10()