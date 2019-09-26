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
            
    def clear(self):
        self.head = None

    def contains_item(self, item):
        tmp = self.head
        while tmp is not None:
            if item is tmp.item:
                return True
                break

            else:
                tmp = tmp.next
        return False


    def get_index_of(self, item):
        temp = self.head
        while temp is not None:
            if item is temp.item:
                return temp
                break

            else:
                temp = temp.next

    def get(self, index):
        count = 0
        tmp = self.head

        if tmp is None:
            return None

        else:
            while count is not index:
                if tmp.next is None:
                    return None
                count += 1
                tmp = tmp.next
            return tmp.item

    def get_first(self):
        if self is None:
            return -1
        else:
            return self.head

    def get_last(self):
        temp = self.head
        while temp is not None:
            if temp.next is None:
                return temp.item

            else:
                temp = temp.next

    def remove_index(self, index):
        count = 0
        temp = self.head









