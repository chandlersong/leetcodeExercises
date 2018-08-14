from unittest import TestCase


class MyNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """

        i = 0;
        result = self.__head
        while result is not None and i < index:
            result = result.next
            i = i + 1

        if result is None:
            return -1

        return result.value

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """

        new_header = MyNode(value=val, next=self.__head)
        self.__head = new_header

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if self.__head is None:
            self.__head = MyNode(value=val, next=self.__head)
            return
        next = self.__head
        while next.next is not None:
            next = next.next

        next.next = MyNode(value=val, next=None)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        i = 0;
        result = self.__head
        previous = None
        while result is not None and i < index:
            previous = result
            result = result.next
            i = i + 1

        if previous is None:
            if index == 0:
                self.__head = MyNode(value=val, next=result)
            return

        previous.next = MyNode(value=val, next=result)

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """

        i = 0;
        result = self.__head
        previous = None
        while result is not None and i < index:
            previous = result
            result = result.next
            i = i + 1

        if result is None:
            return

        previous.next = result.next


class TestLinkedList(TestCase):

    def test_1(self):
        linked_list = MyLinkedList()
        linked_list.addAtHead(1)
        linked_list.addAtIndex(1, 2)
        print(linked_list.get(1))
        print(linked_list.get(0))
        print(linked_list.get(2))

    def test_2(self):
        linked_list = MyLinkedList()
        print(linked_list.get(0))
        linked_list.addAtIndex(1, 2)
        print(linked_list.get(0))
        print(linked_list.get(1))
        linked_list.addAtIndex(0, 1)
        print(linked_list.get(0))
        print(linked_list.get(1))

    def test_3(self):
        linked_list = MyLinkedList()
        linked_list.addAtHead(1)
        linked_list.addAtIndex(1, 2)
        print(linked_list.get(1))
        print(linked_list.get(0))
        print(linked_list.get(2))

    def test_4(self):
        linked_list = MyLinkedList()
        print(linked_list.get(0))
        linked_list.addAtIndex(1, 2)
        print(linked_list.get(0))
        print(linked_list.get(1))
        linked_list.addAtIndex(0, 1)
        print(linked_list.get(0))
        print(linked_list.get(1))
