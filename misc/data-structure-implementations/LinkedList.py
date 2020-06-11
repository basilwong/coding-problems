class Node:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length or index < 0:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.value


    def addAtHead(self, value: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if not self.__conditional_add_first(value):
            self.head.prev = Node(value)
            self.head.prev.next = self.head
            self.head = self.head.prev
        self.length += 1


    def addAtTail(self, value: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.__conditional_add_first(value):
            self.tail.next = Node(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        self.length += 1


    def addAtIndex(self, index: int, value: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length or index < 0:
            return
        elif index == 0:
            self.addAtHead(value)
        elif index == self.length:
            self.addAtTail(value)
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            self.__insert_between(value, cur.prev, cur)
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.length or index < 0:
            return
        elif index == 0 and self.length == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            temp = self.head
            self.head = self.head.next
            del temp
        elif index == self.length - 1:
            temp = self.tail
            self.tail = self.tail.prev
            del temp
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            self.__remove_from_middle(cur, cur.prev, cur.next)
        self.length -= 1


    def __conditional_add_first(self, value):
        if self.length == 0:
            self.head = Node(value)
            self.tail = self.head
            return True
        return False

    def __insert_between(self, value, before, after):
        new_node = Node(value)
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

    def __remove_from_middle(self, removed, before, after):
        before.next = after
        after.next = before
        del removed
