# problem 1 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        cn = self.head
        while cn.next is not None:
            cn = cn.next

        cn.next = new_node
        self.size += 1

    def traversal(self):
        if self.head is None:
            print("no elements")
            return

        cn = self.head
        while cn is not None:
            print(cn.data, end="->")
            cn = cn.next

        print("None")

    def search(self, data):
        cn = self.head
        ind = 0

        while cn is not None:
            if cn.data == data:
                print(f"element {data} is at {ind} index")
                return

            cn = cn.next
            ind += 1

        print("element not found")

    def length(self):
        return self.size

    def insBig(self, data):
        obj = Node(data)
        obj.next = self.head
        self.head = obj
        self.size += 1

    def delbig(self):
        if self.head is None:
            return

        self.head = self.head.next
        self.size -= 1

    def dellast(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            self.size -= 1
            return

        cn = self.head
        while cn.next.next is not None:
            cn = cn.next

        cn.next = None
        self.size -= 1

    def insAt(self, data, position):
        if position < 0 or position > self.size:
            print("invalid position")
            return

        obj = Node(data)

        if position == 0:
            obj.next = self.head
            self.head = obj
            self.size += 1
            return

        cn = self.head
        for _ in range(position - 1):
            cn = cn.next

        obj.next = cn.next
        cn.next = obj
        self.size += 1

    def count(self, data):
        count = 0
        cn = self.head

        while cn is not None:
            if cn.data == data:
                count += 1
            cn = cn.next

        return count


ll = linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)

ll.traversal()
ll.search(20)
print(ll.length())

ll.insBig(5)
ll.traversal()

ll.delbig()
ll.traversal()

ll.insAt(50, 2)
ll.traversal()

# problem 2 

class Node:
    def __init__(self,data):
      self.data=data
      self.next=None
class linkedlist:
    def __init__(self):
      self.head=None
      self.size=0
    def add(self,data):
      if self.head==None:
        self.head=Node(data)
        self.size+=1
        return
      cn=self.head
      while cn.next is not None:
        cn=cn.next
      cn.next=Node(data)
      self.size+=1
    def traversal(self):
      if self.head==None:
          print('no elements')
      cn=self.head
      while cn is not None:
          print(cn.data,end="->")
          cn=cn.next
      print(cn)
    def search(self,data):
  
      cn=self.head
      ind=0
      while cn is not None:
          if cn.data == data:
            print(f'element {data} is at {ind} index')
            return
          cn=cn.next
          ind+=1
      print('element not found')
    def length(self):
      return self.size
    def insBig(self,data):
      obj=Node(data)
      obj.next=self.head
      self.head=obj
    def delbig(self):
      if self.head is None:
          return
      self.head=self.head.next
    def dellast(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        cn = self.head
        while cn.next.next is not None:
            cn = cn.next
        cn.next = None


ll=linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.traversal()
ll.search(20)
print(ll.length())
ll.insBig(5)
ll.traversal() 
ll.delbig()  
ll.traversal()

#problem 3 

class Node:
    def __init__(self,data):
      self.data=data
      self.next=None
class linkedlist:
    def __init__(self):
      self.head=None
      self.size=0
    def add(self,data):
      if self.head==None:
        self.head=Node(data)
        self.size+=1
        return
      cn=self.head
      while cn.next is not None:
        cn=cn.next
      cn.next=Node(data)
      self.size+=1
    def traversal(self):
      if self.head==None:
          print('no elements')
      cn=self.head
      while cn is not None:
          print(cn.data,end="->")
          cn=cn.next
      print(cn)
    def search(self,data):
  
      cn=self.head
      ind=0
      while cn is not None:
          if cn.data == data:
            print(f'element {data} is at {ind} index')
            return
          cn=cn.next
          ind+=1
      print('element not found')
    def length(self):
      return self.size
    def insBig(self,data):
      obj=Node(data)
      obj.next=self.head
      self.head=obj
    def delbig(self):
      if self.head is None:
          return
      self.head=self.head.next
  
  
ll=linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.traversal()
ll.search(20)
print(ll.length())
ll.insBig(5)
ll.traversal() 
ll.delbig()  
ll.traversal()

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteNode(node):
    if node is None or node.next is None:
        return

    node.val = node.next.val
    node.next = node.next.next


def buildList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    cur = head

    for x in arr[1:]:
        cur.next = ListNode(x)
        cur = cur.next

    return head


def printList(head):
    result = []

    while head:
        result.append(str(head.val))
        head = head.next

    print(" ".join(result))


def main():
    n = int(input())

    if n == 0:
        print("empty")
        return

    arr = list(map(int, input().split()))
    head = buildList(arr)

    if n > 1:
        cur = head
        for _ in range(n // 2 - 1):
            cur = cur.next
        deleteNode(cur.next)

    printList(head)


if __name__ == "__main__":
    main()


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev = None
    cur = head

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev


def buildList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    cur = head

    for x in arr[1:]:
        cur.next = ListNode(x)
        cur = cur.next

    return head


def printList(head):
    result = []

    while head:
        result.append(str(head.val))
        head = head.next

    print(" ".join(result))


def main():
    n = int(input())

    if n == 0:
        print("empty")
        return

    arr = list(map(int, input().split()))
    head = buildList(arr)
    head = reverseList(head)

    printList(head)


if __name__ == "__main__":
    main()


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    if head is None or head.next is None:
        return True

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    cur = slow

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    left = head
    right = prev

    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


def buildList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    cur = head

    for x in arr[1:]:
        cur.next = ListNode(x)
        cur = cur.next

    return head


def main():
    n = int(input())

    if n == 0:
        print("true")
        return

    arr = list(map(int, input().split()))
    head = buildList(arr)

    print("true" if isPalindrome(head) else "false")


if __name__ == "__main__":
    main()


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA, headB):
    if headA is None or headB is None:
        return None

    a = headA
    b = headB

    while a is not b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a


def buildList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    cur = head

    for x in arr[1:]:
        cur.next = ListNode(x)
        cur = cur.next

    return head


def main():
    n = int(input())
    arr1 = list(map(int, input().split())) if n > 0 else []

    m = int(input())
    arr2 = list(map(int, input().split())) if m > 0 else []

    headA = buildList(arr1)
    headB = buildList(arr2)

    result = getIntersectionNode(headA, headB)

    print(result.val if result else "None")


if __name__ == "__main__":
    main()


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = first.next

        first.next = second.next
        second.next = first
        prev.next = second

        prev = first

    return dummy.next


def buildList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    cur = head

    for x in arr[1:]:
        cur.next = ListNode(x)
        cur = cur.next

    return head


def printList(head):
    result = []

    while head:
        result.append(str(head.val))
        head = head.next

    print(" ".join(result))


def main():
    n = int(input())

    if n == 0:
        print("empty")
        return

    arr = list(map(int, input().split()))
    head = buildList(arr)
    head = swapPairs(head)

    printList(head)


if __name__ == "__main__":
    main()


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None

    prev = None
    cur = second

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    second = prev
    first = head

    while second:
        first_next = first.next
        second_next = second.next

        first.next = second
        second.next = first_next

        first = first_next
        second = second_next

    return head


def buildList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    cur = head

    for x in arr[1:]:
        cur.next = ListNode(x)
        cur = cur.next

    return head


def printList(head):
    result = []

    while head:
        result.append(str(head.val))
        head = head.next

    print(" ".join(result))


def main():
    n = int(input())

    if n == 0:
        print("empty")
        return

    arr = list(map(int, input().split()))
    head = buildList(arr)

    reorderList(head)

    printList(head)


if __name__ == "__main__":
    main()


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head):
    if head is None:
        return None

    node_map = {}
    cur = head

    while cur:
        node_map[cur] = Node(cur.val)
        cur = cur.next

    cur = head

    while cur:
        node_map[cur].next = node_map.get(cur.next)
        node_map[cur].random = node_map.get(cur.random)
        cur = cur.next

    return node_map[head]


def buildRandomList(values, random_indices):
    if not values:
        return None

    nodes = [Node(x) for x in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    for i, index in enumerate(random_indices):
        if index != -1:
            nodes[i].random = nodes[index]

    return nodes[0]


def printRandomList(head):
    nodes = []
    cur = head

    while cur:
        nodes.append(cur)
        cur = cur.next

    index_map = {node: i for i, node in enumerate(nodes)}

    result = []
    cur = head

    while cur:
        random_index = -1

        if cur.random:
            random_index = index_map[cur.random]

        result.append(f"{cur.val}({random_index})")
        cur = cur.next

    print(" ".join(result))


def main():
    n = int(input())

    if n == 0:
        print("empty")
        return

    values = list(map(int, input().split()))
    random_indices = list(map(int, input().split()))

    head = buildRandomList(values, random_indices)
    copied = copyRandomList(head)

    printRandomList(copied)


if __name__ == "__main__":
    main()


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge(a, b):
    dummy = ListNode(0)
    cur = dummy

    while a and b:
        if a.val <= b.val:
            cur.next = a
            a = a.next
        else:
            cur.next = b
            b = b.next

        cur = cur.next

    cur.next = a if a else b

    return dummy.next


def sortList(head):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None

    left = sortList(head)
    right = sortList(second)

    return merge(left, right)


def buildList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    cur = head

    for x in arr[1:]:
        cur.next = ListNode(x)
        cur = cur.next

    return head


def printList(head):
    result = []

    while head:
        result.append(str(head.val))
        head = head.next

    print(" ".join(result))


def main():
    n = int(input())

    if n == 0:
        print("empty")
        return

    arr = list(map(int, input().split()))

    head = buildList(arr)
    head = sortList(head)

    printList(head)


if __name__ == "__main__":
    main()