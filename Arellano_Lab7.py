# Name: Ana K. Arellano
# Lab: 7
# ID: 80631366


def edit_distance(string, string_2, length_1, length_2):
    if length_1 == 0:
        return length_2
    elif length_2 == 0:
        return length_1
    elif string[length_1 - 1] == string_2[length_2 - 1]:
        return edit_distance(string, string_2, length_1 - 1, length_2 - 1)

    return min(edit_distance(string, string_2, length_1, length_2 - 1),
               edit_distance(string, string_2, length_1 - 1, length_2), edit_distance(string, string_2,
                                                                                      length_1 - 1, length_2 - 1)) + 1


def main():
    print("test case 1:")
    string_1 = "money"
    string_2 = "miner"
    print("words:", string_1, string_2)
    distance = edit_distance(string_1, string_2, len(string_1), len(string_2))
    print("edit distance between them:", distance)

    print()
    print("test case 2:")
    string_3 = "shark"
    string_4 = "smarts"
    print("words:", string_3, string_4)
    distance_2 = edit_distance(string_3, string_4, len(string_3), len(string_4))
    print("edit distance between them:", distance_2)

    print()
    print()
    print("test case 3:")
    string_5 = "cars"
    string_6 = "bicycle"
    print("words:", string_5, string_6)
    distance_3 = edit_distance(string_5, string_6, len(string_5), len(string_6))
    print("edit distance between them:", distance_3)




main()
