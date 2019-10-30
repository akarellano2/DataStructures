#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:04:46 2019

@author: karenarellano
"""
# Ana Karen Arellano
# ID: 80631366
# Lab 4
# CS2302

import matplotlib.pyplot as plt


class BTreeNode:
    # Constructor
    def __init__(self, keys=[], children=[], is_leaf=True, max_num_keys=5):
        self.keys = keys
        self.children = children
        self.is_leaf = is_leaf
        if max_num_keys < 3:  # max_num_keys must be odd and greater or equal to 3
            max_num_keys = 3
        if max_num_keys % 2 == 0:  # max_num_keys must be odd and greater or equal to 3
            max_num_keys += 1
        self.max_num_keys = max_num_keys

    def is_full(self):
        return len(self.keys) >= self.max_num_keys
    
class BTree:
    # Constructor
    def __init__(self, max_num_keys=5):
        self.max_num_keys = max_num_keys
        self.root = BTreeNode(max_num_keys=max_num_keys)

    def find_child(self, k, node=None):
        # Determines value of c, such that k must be in subtree node.children[c], if k is in the BTree
        if node is None:
            node = self.root

        for i in range(len(node.keys)):
            if k < node.keys[i]:
                return i
        return len(node.keys)

    def insert_internal(self, i, node=None):

        if node is None:
            node = self.root

        # node cannot be Full
        if node.is_leaf:
            self.insert_leaf(i, node)
        else:
            k = self.find_child(i, node)
            if node.children[k].is_full():
                m, l, r = self.split(node.children[k])
                node.keys.insert(k, m)
                node.children[k] = l
                node.children.insert(k + 1, r)
                k = self.find_child(i, node)
            self.insert_internal(i, node.children[k])

    def split(self, node=None):
        if node is None:
            node = self.root
        # print('Splitting')
        # PrintNode(T)
        mid = node.max_num_keys // 2
        if node.is_leaf:
            left_child = BTreeNode(node.keys[:mid], max_num_keys=node.max_num_keys)
            right_child = BTreeNode(node.keys[mid + 1:], max_num_keys=node.max_num_keys)
        else:
            left_child = BTreeNode(node.keys[:mid], node.children[:mid + 1], node.is_leaf, max_num_keys=node.max_num_keys)
            right_child = BTreeNode(node.keys[mid + 1:], node.children[mid + 1:], node.is_leaf, max_num_keys=node.max_num_keys)
        return node.keys[mid], left_child, right_child

    def insert_leaf(self, i, node=None):
        if node is None:
            node = self.root

        node.keys.append(i)
        node.keys.sort()

    def leaves(self, node=None):
        if node is None:
            node = self.root
        # Returns the leaves in a b-tree
        if node.is_leaf:
            return [node.keys]
        s = []
        for c in node.children:
            s = s + self.leaves(c)
        return s

    def insert(self, i, node=None):
        if node is None:
            node = self.root
        if not node.is_full():
            self.insert_internal(i, node)
        else:
            m, l, r = self.split(node)
            node.keys = [m]
            node.children = [l, r]
            node.is_leaf = False
            k = self.find_child(i, node)
            self.insert_internal(i, node.children[k])

    def height(self, node=None):
        if node is None:
            node = self.root
        if node.is_leaf:
            return 0
        return 1 + self.height(node.children[0])

    def print(self, node=None): #printing the tree
        # Prints keys in tree in ascending order
        if node is None:
            node = self.root

        if node.is_leaf:
            for t in node.keys:
                print(t, end=' ')
                print('\n') #printing words in different lines
        else:
            for i in range(len(node.keys)):
                self.print(node.children[i])
                print(node.keys[i], end=' ')
                print('\n') #printing words in different lines
            self.print(node.children[len(node.keys)])

    def print_d(self, space, node=None):
        if node is None:
            node = self.root
        # Prints keys and structure of B-tree
        if node.is_leaf:
            for i in range(len(node.keys) - 1, -1, -1):
                print(space, node.keys[i])
        else:
            self.print_d(space + '   ', node.children[len(node.keys)])
            for i in range(len(node.keys) - 1, -1, -1):
                print(space, node.keys[i])
                self.print_d(space + '   ', node.children[i])

    def search(self, k, node=None):
        if node is None:
            node = self.root
        # Returns node where k is, or None if k is not in the tree
        if k in node.keys:
            return node
        if node.is_leaf:
            return None
        return self.search(k, node.children[self.find_child(k, node)])

    #def _set_x(self, dx, node=None):
        #if node is None:
            #node = self.root
        # Finds x-coordinate to display each node in the tree
        #if node.is_leaf:
            #return
       # else:
            #for c in node.children:
               # self._set_x(dx, c)
           # d = (dx[node.children[0].keys[0]] + dx[node.children[-1].keys[0]] + 10 * len(node.children[-1].keys)) / 2
           # dx[node.keys[0]] = d - 10 * len(node.keys) / 2

    #def _draw_btree(self, dx, y, y_inc, fs, ax, node=None):
       # if node is None:
         #   node = self.root
        # Function to display b-tree to the screen
        # It works fine for trees with up to about 70 keys
       # xs = dx[node.keys[0]]
       # if node.is_leaf:
       #     for itm in node.keys:
         #       ax.plot([xs, xs + 10, xs + 10, xs, xs], [y, y, y - 10, y - 10, y], linewidth=1, color='k')
               # ax.text(xs + 5, y - 5, str(itm), ha="center", va="center", fontsize=fs)
               # xs += 10
      #  else:
           # for i in range(len(node.keys)):
             #   xc = dx[node.children[i].keys[0]] + 5 * len(node.children[i].keys)
             #   ax.plot([xs, xs + 10, xs + 10, xs, xs], [y, y, y - 10, y - 10, y], linewidth=1, color='k')
             #   ax.text(xs + 5, y - 5, str(node.keys[i]), ha="center", va="center", fontsize=fs)
             #   ax.plot([xs, xc], [y - 10, y - y_inc], linewidth=1, color='k')
             #   self._draw_btree(dx, y - y_inc, y_inc, fs, ax, node.children[i])
             #   xs += 10
           # xc = dx[node.children[-1].keys[0]] + 5 * len(node.children[-1].keys)
           # ax.plot([xs, xc], [y - 10, y - y_inc], linewidth=1, color='k')
            #self._draw_btree(dx, y - y_inc, y_inc, fs, ax, node.children[-1])

    #def draw(self):
        # Find x-coordinates of leaves
       # ll = self.leaves()
        #dx = {}
       # d = 0
        #for l in ll:
          #  dx[l[0]] = d
           # d += 10 * (len(l) + 1)
            # Find x-coordinates of internal nodes
       # self._set_x(dx)
      #  # plt.close('all')
      #  fig, ax = plt.subplots()
       # self._draw_btree(dx, 0, 30, 10, ax)
      #  ax.set_aspect(1.0)
      #  ax.axis('off')
       # plt.show()
        
#class Execute:
    
def print_anagrams(word,english_words_tree, prefix= ""):
    if len(word) <= 1:

        if english_words_tree.search(prefix + word, english_words_tree.root):
            print(prefix + word)

    else:
        for i in range(len(word)):
            temp = word[i: i+1]
            before = word[0: i]  # letters before temp
            after = word[i+1:]  # letters after temp

            if temp not in before:
                print_anagrams(before + after, english_words_tree, prefix + temp)
                
        

def read_file_btree(user_number):

    word_file = open('test.txt', 'r')
    line = word_file.readline()
    b_tree = BTree(max_num_keys = user_number)
    
    for line in word_file:
        b_tree.insert(line.replace('\n',''))
        
    return b_tree

def count_anagrams(word,english_words_tree,prefix=""):
    count = 0
    if len(word) <= 1:
        elem = prefix + word
    if english_words_tree.search(prefix + word, english_words_tree.root):
        count += 1
    else:
        for i in range(len(word)):
            temp = word[i: i+1]
            previous_word = word[0: i]
            next_word = word[i + 1:]
            if temp not in previous_word:
                count_anagrams(previous_word + next_word, english_words_tree, prefix + temp)
    return count
        

def main():
    plt.close('all')
        
    print('Hello, today we will be using a B-Tree')
    print('What do you want the max number of keys to be?')
    
    user_number = int(input())
    
    #count = 0
    if user_number == 0:
        print('You can not use that number')
        
    else:
        english_words_tree = read_file_btree(user_number)
        
        english_words_tree.print(english_words_tree.root)
        
        print('Choose a word to find its anagrams')
        user_word = input()
        print_anagrams(user_word, english_words_tree)
        print('Number of anagrams:')
        count_words = count_anagrams(user_word, english_words_tree)
        print(count_words)
        
    
main()

#        #if english_words_tree.search(prefix + word, english_words_tree.root):

