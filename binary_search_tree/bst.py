
# PROBLEM 1
# Convert BST to Sorted Right-Skewed List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createPriorityQueue(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        stack = []
        current = root
        new_root = None
        previous = None

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            right_child = current.right

            current.left = None

            if new_root is None:
                new_root = current
            else:
                previous.right = current

            previous = current
            current = right_child

        if previous:
            previous.right = None

        return new_root


def buildTree(values):
    if not values or values[0] == "null":
        return None

    root = TreeNode(int(values[0]))
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)

        i += 1

        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)

        i += 1

    return root


def printList(root):
    result = []
    current = root

    while current:
        result.append(str(current.val))
        current = current.right

    print(" ".join(result))


def main():
    values = input().split()
    root = buildTree(values)

    solution = Solution()
    result = solution.createPriorityQueue(root)

    printList(result)


if __name__ == "__main__":
    main()



# PROBLEM 2
# Insert a Value into BST


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)

        current = root

        while True:
            if val < current.val:
                if current.left is None:
                    current.left = TreeNode(val)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(val)
                    break
                current = current.right

        return root


def build_tree(values):
    if not values or values[0] == -1:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] != -1:
            node.left = TreeNode(values[i])
            queue.append(node.left)

        i += 1

        if i < len(values) and values[i] != -1:
            node.right = TreeNode(values[i])
            queue.append(node.right)

        i += 1

    return root


def tree_to_list(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(-1)

    while result and result[-1] == -1:
        result.pop()

    return result


def main():
    n = int(input())

    if n == 0:
        input()
        val = int(input())
        print(val)
        return

    values = list(map(int, input().split()))
    val = int(input())

    root = build_tree(values)

    solution = Solution()
    result = solution.insertIntoBST(root, val)

    output = tree_to_list(result)
    print(" ".join(map(str, output)))


if __name__ == "__main__":
    main()



# PROBLEM 3
# Search in BST


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        current = root

        while current is not None:
            if current.val == val:
                return current

            if val < current.val:
                current = current.left
            else:
                current = current.right

        return None


def build_tree(values):
    if not values or values[0] == -1:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] != -1:
            node.left = TreeNode(values[i])
            queue.append(node.left)

        i += 1

        if i < len(values) and values[i] != -1:
            node.right = TreeNode(values[i])
            queue.append(node.right)

        i += 1

    return root


def tree_to_list(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(-1)

    while result and result[-1] == -1:
        result.pop()

    return result


def main():
    n = int(input())

    if n == 0:
        input()
        val = int(input())
        print("null")
        return

    values = list(map(int, input().split()))
    val = int(input())

    root = build_tree(values)

    solution = Solution()
    result = solution.searchBST(root, val)

    if result is None:
        print("null")
    else:
        output = tree_to_list(result)
        print(" ".join(map(str, output)))


if __name__ == "__main__":
    main()



# PROBLEM 4
# Find Mode(s) in BST


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTurnoutModes(self, root: TreeNode):
        if root is None:
            return []

        # First inorder traversal.
        # Find the maximum frequency.
        stack = []
        current = root

        previous = None
        current_count = 0
        max_count = 0

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            if previous is not None and previous.val == current.val:
                current_count += 1
            else:
                current_count = 1

            max_count = max(max_count, current_count)

            previous = current
            current = current.right

        # Second inorder traversal.
        # Collect all values with maximum frequency.
        modes = []

        stack = []
        current = root

        previous = None
        current_count = 0

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            if previous is not None and previous.val == current.val:
                current_count += 1
            else:
                current_count = 1

            if current_count == max_count:
                if not modes or modes[-1] != current.val:
                    modes.append(current.val)

            previous = current
            current = current.right

        return modes


def buildTree(values):
    if not values or values[0] == "null":
        return None

    root = TreeNode(int(values[0]))
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)

        i += 1

        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)

        i += 1

    return root


def main():
    values = input().split()

    root = buildTree(values)

    solution = Solution()
    result = solution.findTurnoutModes(root)

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()



# PROBLEM 5
# Add Maturity Bonus / Greater Sum BST


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addMaturityBonus(self, root: TreeNode) -> TreeNode:
        running_sum = 0

        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.right

            current = stack.pop()

            running_sum += current.val
            current.val = running_sum

            current = current.left

        return root


def buildTree(values):
    if not values or values[0] == "null":
        return None

    root = TreeNode(int(values[0]))
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)

        i += 1

        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)

        i += 1

    return root


def printTree(root):
    if root is None:
        print("null")
        return

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    while result and result[-1] == "null":
        result.pop()

    print(" ".join(result))


def main():
    values = input().split()

    root = buildTree(values)

    solution = Solution()
    result = solution.addMaturityBonus(root)

    printTree(result)


if __name__ == "__main__":
    main()



# PROBLEM 6
# Recover Corrupted BST


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverDatabase(self, root: TreeNode) -> None:
        if root is None:
            return

        first = None
        second = None
        previous = None

        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            if previous is not None and previous.val > current.val:
                if first is None:
                    first = previous

                second = current

            previous = current
            current = current.right

        if first is not None and second is not None:
            first.val, second.val = second.val, first.val


def buildTree(values):
    if not values or values[0] == "null":
        return None

    root = TreeNode(int(values[0]))
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)

        i += 1

        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)

        i += 1

    return root


def printTree(root):
    if root is None:
        print("null")
        return

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    while result and result[-1] == "null":
        result.pop()

    print(" ".join(result))


def main():
    values = input().split()

    root = buildTree(values)

    solution = Solution()
    solution.recoverDatabase(root)

    printTree(root)


if __name__ == "__main__":
    main()



# PROBLEM 7
# Find Kth Smallest Element in BST


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            k -= 1

            if k == 0:
                return current.val

            current = current.right

        return -1


def buildTree(values):
    if not values or values[0] == "null":
        return None

    root = TreeNode(int(values[0]))
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)

        i += 1

        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)

        i += 1

    return root


def main():
    values = input().split()
    k = int(input())

    root = buildTree(values)

    solution = Solution()
    print(solution.kthSmallest(root, k))


if __name__ == "__main__":
    main()



# PROBLEM 8
# Find Lowest Common Ancestor in BST


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> TreeNode:
        current = root

        while current:
            if p < current.val and q < current.val:
                current = current.left

            elif p > current.val and q > current.val:
                current = current.right

            else:
                return current

        return None


def buildTree(values):
    if not values or values[0] == "null":
        return None

    root = TreeNode(int(values[0]))
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)

        i += 1

        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)

        i += 1

    return root


def main():
    values = input().split()
    p = int(input())
    q = int(input())

    root = buildTree(values)

    solution = Solution()
    result = solution.lowestCommonAncestor(root, p, q)

    if result:
        print(result.val)
    else:
        print("null")


if __name__ == "__main__":
    main()



# PROBLEM 9
# Validate Binary Search Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        current = root
        previous = None

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            if previous is not None and current.val <= previous:
                return False

            previous = current.val
            current = current.right

        return True


def buildTree(values):
    if not values or values[0] == "null":
        return None

    root = TreeNode(int(values[0]))
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)

        i += 1

        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)

        i += 1

    return root


def main():
    values = input().split()

    root = buildTree(values)

    solution = Solution()

    if solution.isValidBST(root):
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    main()



# PROBLEM 10
# Find Height of Binary Search Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def height(self, root: TreeNode) -> int:
        if root is None:
            return 0

        queue = [root]
        height = 0

        while queue:
            level_size = len(queue)
            height += 1

            for _ in range(level_size):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return height


def buildTree(values):
    if not values or values[0] == "null":
        return None

    root = TreeNode(int(values[0]))
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)

        i += 1

        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)

        i += 1

    return root


def main():
    values = input().split()

    root = buildTree(values)

    solution = Solution()
    print(solution.height(root))


if __name__ == "__main__":
    main()