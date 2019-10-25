# Lab3 OptionB
# LastName = "Arellano"
# FirstName = "Ana"
# ID = "80631366"

# import RedBlack
# import AVL


def print_anagrams(word, prefix= ""):
    if len(word) <= 1:
        str = prefix + word

        if str in english_words:
            print(prefix + word)

    else:
        for i in range(len(word)):
            temp = word[i: i+1]
            before = word[0: i]  # letters before temp
            after = word[i+1:]  # letters after temp

            if temp not in before:
                print_anagrams(before + after, prefix + temp)

# TEST TO READ FILE
# def read_file():
#     file = open("words.txt", "r")
#     line = file.readline()
#     for line in file:
#         print(line)


def count_anagrams(single_word, all_english_words,prefix=""):
    if len(single_word) <= 1:
        elem = prefix + single_word
        if all_english_words.avl_tree_search(prefix + word, english_words.root):
            count += 1
        else:
            for i in range(len(single_word)):
                temp = single_word[i: i+1]
                previous_word = single_word[0: i]
                next_word = single_word[i + 1:]
                if temp not in previous_word:
                    count_anagrams(previous_word + next_word, all_english_words, prefix + temp)
        return count


# def greatest_number_of_anagrams():

# Method that reads text file into a red and black tree
def red_black_read():
    file = open("words.txt", "r")
    single_line = file.readline()
    rbt_tree = RedBlack()
    for single_line in file:
        single_word = single_line.replace("\n", "")
        rbt_tree.rbt_insert(single_word)

    return rbt_tree


#method that reads text file into an AVL tree
def avl_tree_read():
    file = open("words.txt", "r")
    single_line = file.readline() #read line by line at a time
    avl_tree = AVL()
    for single_line in file:
        single_word = single_line.replace("\n", "")
        avl_tree.avl_tree_insert(single_word)

    return avl_tree


def main():

    print("Hello! What type of tree would you like to use, AVL or Red and Black?")
    print("Type AVL or RBT")
    user_input = input()

    if user_input == "AVL" or "avl":
        avl_tree_file = avl_tree_read()

    elif user_input == "RBT" or "rbt":
        rbt_tree_file = red_black_read()

    else:
        print("That's not a valid tree")


main()

