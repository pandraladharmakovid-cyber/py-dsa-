from collections import deque


# Problem 1
# Count Leaf Nodes in a Binary Tree


def problem_1():
    n = int(input().strip())

    if n == 0:
        print(0)
        return

    nodes = list(map(int, input().split()))

    leaf_count = 0

    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2

        if left >= n and right >= n:
            leaf_count += 1

    print(leaf_count)


def main_problem_1():
    problem_1()


# Problem 2
# Level-Order Insertion in a Binary Tree


def problem_2():
    n = int(input().strip())

    if n == 0:
        value = int(input().strip())
        print(value)
        return

    nodes = list(map(int, input().split()))
    value = int(input().strip())

    nodes.append(value)

    print(*nodes)


def main_problem_2():
    problem_2()


# Common TreeNode class for Problems 3 to 10


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Common buildTree function


def buildTree(values):
    if not values or values[0] == "null":
        return None

    root = TreeNode(int(values[0]))

    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)

        i += 1

        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)

        i += 1

    return root


# Problem 3
# Same Binary Tree


class SameTreeSolution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            if node1 is None and node2 is None:
                continue

            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False

            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))

        return True


def main_problem_3():
    values1 = input().split()
    values2 = input().split()

    p = buildTree(values1)
    q = buildTree(values2)

    sol = SameTreeSolution()

    result = sol.isSameTree(p, q)

    print("true" if result else "false")


# Problem 4
# Path Sum


class PathSumSolution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False

        stack = [(root, root.val)]

        while stack:
            node, current_sum = stack.pop()

            if node.left is None and node.right is None:
                if current_sum == targetSum:
                    return True

            if node.left is not None:
                stack.append(
                    (node.left, current_sum + node.left.val)
                )

            if node.right is not None:
                stack.append(
                    (node.right, current_sum + node.right.val)
                )

        return False


def main_problem_4():
    values = input().split()
    targetSum = int(input())

    root = buildTree(values)

    sol = PathSumSolution()

    result = sol.hasPathSum(root, targetSum)

    print("true" if result else "false")


# Problem 5
# Binary Tree Paths


class BinaryTreePathsSolution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        result = []

        def dfs(node, path):
            if node is None:
                return

            path.append(str(node.val))

            if node.left is None and node.right is None:
                result.append("->".join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)

            path.pop()

        dfs(root, [])

        return result


def main_problem_5():
    values = input().split()

    root = buildTree(values)

    sol = BinaryTreePathsSolution()

    result = sol.binaryTreePaths(root)

    if result:
        print(" ".join(result))
    else:
        print("empty")


# Problem 6
# Flatten Binary Tree to Linked List


class FlattenBinaryTreeSolution:
    def flatten(self, root: TreeNode) -> None:
        current = root

        while current is not None:
            if current.left is not None:
                predecessor = current.left

                while predecessor.right is not None:
                    predecessor = predecessor.right

                predecessor.right = current.right
                current.right = current.left
                current.left = None

            current = current.right


def printFlattenedTree(root):
    if root is None:
        print("empty")
        return

    result = []

    current = root

    while current is not None:
        result.append(str(current.val))
        current = current.right

    print(" ".join(result))


def main_problem_6():
    values = input().split()

    root = buildTree(values)

    sol = FlattenBinaryTreeSolution()

    sol.flatten(root)

    printFlattenedTree(root)


# Problem 7
# Binary Tree Pruning


class BinaryTreePruningSolution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if (
            root.val == 0
            and root.left is None
            and root.right is None
        ):
            return None

        return root


def printLevelOrder(root):
    if root is None:
        print("empty")
        return

    result = []

    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node is None:
            result.append("null")
            continue

        result.append(str(node.val))

        if node.left is not None or node.right is not None:
            queue.append(node.left)
            queue.append(node.right)

    while result and result[-1] == "null":
        result.pop()

    print(" ".join(result))


def main_problem_7():
    values = input().split()

    root = buildTree(values)

    sol = BinaryTreePruningSolution()

    root = sol.pruneTree(root)

    printLevelOrder(root)


# Problem 8
# All Nodes Distance K in Binary Tree


class DistanceKSolution:
    def distanceK(
        self,
        root: TreeNode,
        target: TreeNode,
        k: int
    ) -> list[int]:

        parent = {}
        order = {}

        queue = deque([root])
        parent[id(root)] = None
        index = 0

        while queue:
            node = queue.popleft()

            order[id(node)] = index
            index += 1

            if node.left is not None:
                parent[id(node.left)] = node
                queue.append(node.left)

            if node.right is not None:
                parent[id(node.right)] = node
                queue.append(node.right)

        queue = deque([target])
        visited = {id(target)}
        distance = 0

        while queue and distance < k:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                neighbors = [
                    node.left,
                    node.right,
                    parent[id(node)]
                ]

                for neighbor in neighbors:
                    if (
                        neighbor is not None
                        and id(neighbor) not in visited
                    ):
                        visited.add(id(neighbor))
                        queue.append(neighbor)

            distance += 1

        result = list(queue)

        ordered_result = []

        for i in range(index):
            for node in result:
                if order[id(node)] == i:
                    ordered_result.append(node.val)

        return ordered_result


def findNode(root, value):
    if root is None:
        return None

    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.val == value:
            return node

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return None


def main_problem_8():
    values = input().split()
    target_value = int(input())
    k = int(input())

    root = buildTree(values)

    target = findNode(root, target_value)

    sol = DistanceKSolution()

    result = sol.distanceK(root, target, k)

    if result:
        print(" ".join(map(str, result)))
    else:
        print("empty")


# Problem 9
# Maximum Depth of Binary Tree


class MaximumDepthSolution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            level_size = len(queue)
            depth += 1

            for _ in range(level_size):
                node = queue.popleft()

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

        return depth


def main_problem_9():
    values = input().split()

    root = buildTree(values)

    sol = MaximumDepthSolution()

    result = sol.maxDepth(root)

    print(result)


# Problem 10
# Invert Binary Tree


class InvertBinaryTreeSolution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return root


def main_problem_10():
    values = input().split()

    root = buildTree(values)

    sol = InvertBinaryTreeSolution()

    root = sol.invertTree(root)

    printLevelOrder(root)


