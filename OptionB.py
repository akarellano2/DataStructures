from LList import LList
from Node import Node

# METHOD THAT PRINTS THE FIRST 20 ELEMENTS OF THE LLIST


def top_elements_print(llink):
    temp = llink.head
    for i in range(20):
        print("Password: ", temp.password, "Number of times repeated: ", temp.count)
        temp = temp.next

#   METHOD THAT CHECKS IF PASSWORD HAS BEEN ALREADY ADDED TO THE LINKED LIST
#   BY TAKING IN A STRING AND THE LLIST AS A PARAMETER


def check_duplicate(string, linkl):
    temp = linkl.head

    while temp is not None:
        if temp.password == string:
            temp.count += 1
            return True
        else:
            temp = temp.next

    return False

# METHOD TO READ THE TEST FILE AND CREATE A LINKED LIST OUT OF THE TXT FILE


def read_create_combinations():

    first_list = LList()

    file = open("10-million-combos.txt", "r")
    line = file.readline()
    for line in file:

        line = line.strip().split("	")  # SPLITS THE LINE INTO INDEXES OF AN ARRAY
        username = line[0]
        password = line[-1]  # INDEX IN ARRAY WHICH CONTAINS PASSWORD
        # print(password)
        # CALLS METHODS TO CHECKS IF THE PASSWORD HAS BEEN REPEATED
        if not check_duplicate(password, first_list):  # If password was not found:
            first_list.head = Node(password, 1, first_list.head)    # WILL CREATE NEW NODE INTO LLIST WHICH WILL BE HEAD

    file.close()

    return first_list

    # METHOD TO CHECK IF LLIST WORKED
    # tmp = first_list.head
    # while tmp is not None:
    #     print(tmp.password, tmp.count)
    #     tmp = tmp.next

# METHOD THAT USES DICTIONARY TO CHECK IF THE PASSWORD HAS ALREADY BEEN REPEATED


def dictionary_list():
    second_llist = LList()
    combinations_in_dictionary = {}

    file = open("10-million-combos.txt", "r")  # SAME PROCESS TO READ THE TEXT FILE
    line = file.readline()
    for line in file:

        line = line.strip().split("	")
        username = line[0]
        password = line[-1]

        if password in combinations_in_dictionary:  # IF THE PASSWORD WERE TO ALREADY BE THERE, THE COUNT ONLY INCREASES
            combinations_in_dictionary[password].count += 1

        else:   # IF PASSWORD WAS NOT IN THE DICTIONARY THEN NEW NODE IS CREATED AND DICTIONARY STORES THE LOCATION
            second_llist.head = Node(password, 1, second_llist.head)
            combinations_in_dictionary[password] = second_llist.head

    file.close()

    # METHOD CREATED TO CHECK IF LINKED LIST WAS BEING CREATED
    # tmp = second_llist.head
    # while tmp is not None:
    #     print(tmp.password, tmp.count)
    #     tmp = tmp.next

    return second_llist

# TAKES IN A LINKED LIST AND SORTS IT BY THE NUMBER OF TIMES THE PASSWORD
# HAS BEEN REPEATED USING BUBBLE SORT


def bubble_sort(llink):
    swap = True
    while swap:
        current = llink.head
        swap = False
        while current.next is not None:

            if current.count < current.next.count:
                temp = current.count
                current.count = current.next.count
                current.next.count = temp
                swap = True

            current = current.next

    top_elements_print(llink)


# def merge_lists(llink1, llink2):
#     temp = None
#     if llink1 is None:
#         return llink2
#     if llink2 is None:
#         return llink1
#
#     if llink1.count <= llink2.count:
#         temp = llink1
#         temp.next = merge_lists(llink1.next, llink2)
#
#     else:
#         temp = llink2
#         temp.next = merge_lists(llink1, llink2.next)
#
#     return temp
#
#
# def merge_sort(llink):
#     temp = llink
#     if temp.head is None or temp.head.next is None:
#         return temp.head
#     llink1, llink2 = divide_lists(llink)
#     llink1 = merge_sort(llink1)
#     llink2 = merge_sort(llink2)
#     temp.head = merge_lists(llink1, llink2)
#     return llink1
#
#
# def divide_lists(llink):
#     temp = llink
#     slow = temp.head
#     fast = temp.head
#     if fast:
#         fast = fast.next
#     while fast:
#         fast = fast.next
#         if fast:
#             fast = fast.next
#             slow = slow.next
#     mid = slow.next
#     slow.next = None
#     return llink.head, mid


    # counter = 0
    # left_side = LList()
    # right_side = LList()
    #
    # if len(llink) > 1:
    #     middle_point = len(llink) // 2
    #     leftside = llink[:middle_point]
    #     rightside = llink[middle_point:]
    #
    #     merge_sort(rightside)
    #     merge_sort(leftside)
    #
    #     a = llink.head
    #     b = llink.head
    #     c = llink.head
    #     while a < len(leftside) and b < len(rightside):
    #         if leftside[a] < rightside [b]:
    #             llink[c] = leftside[a]
    #             a = a +1
    #
    #         else:
    #             llink[c] = rightside[b]
    #             b = b + 1
    #
    #         c = c + 1
    #
    #     while a < len(leftside):
    #         llink[c] = leftside[a]
    #         a = a + 1
    #         c = c + 1
    #
    #     while b < len(rightside):
    #         llink[c] = rightside[b]
    #         b = b + 1
    #         c = c + 1

def main():

    first_list = LList()
    first_list = read_create_combinations()
    bubble_sort(first_list)

    second_list = LList()
    second_list = dictionary_list()
    bubble_sort(second_list)


main()

