class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_last(self, item):
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = (item, None)

    def add_first(self, item):
        self.head = Node(item, self.head)

    def add(self, index, item):
        if index <= 0:
            self.head = Node(item, self.head)
            return
        count = 0
        tmp = self.head
        temp = Node(item)
        while count is not index:
            if tmp.next is not None:
                count += 1
                tmp = tmp.next
            else:
                break

            other = other.next
            tmp.next = temp
            temp.next = other









