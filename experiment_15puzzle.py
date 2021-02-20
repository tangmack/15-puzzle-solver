# Mack Tang
# 15-Puzzle Solver
# A Solver that uses set (hash table) and deque (queue) data structures to run quickly
# Instructions to run:
# Put test cases at bottom of this file (by default 5 test cases will run)
# Run this file to write solutions to .txt file, and print action set list.

from collections import deque
import time
st = time.time()

class Solver:
    # switch two letters in a string
    def swap(self, s_, i1, i2):
        m = list(s_)
        m[i1], m[i2] = m[i2], m[i1]  # switch letters
        return ''.join(m)  # return as string

    # def swap(s, i, j):
    #     return ''.join((s[:i], s[j], s[i+1:j], s[i], s[j+1:]))

    # bidirectional translation of letter string to double digit number string
    def translate(self,str_in):
        str = str_in.replace(" ", "")  # remove any whitespaces

        if 'a' in str:
            L = list(str)
        else:
            L = [str[i:i + 2] for i in range(0, len(str), 2)]

        letters_2_numbers_dict = {'a': '01',
                                  'b': '02',
                                  'c': '03',
                                  'd': '04',
                                  'e': '05',
                                  'f': '06',
                                  'g': '07',
                                  'h': '08',
                                  'i': '09',
                                  'j': '10',
                                  'k': '11',
                                  'l': '12',
                                  'm': '13',
                                  'n': '14',
                                  'o': '15',
                                  'X': '00'
                                  }

        numbers_2_letters_dict = {'01': 'a',
                                  '02': 'b',
                                  '03': 'c',
                                  '04': 'd',
                                  '05': 'e',
                                  '06': 'f',
                                  '07': 'g',
                                  '08': 'h',
                                  '09': 'i',
                                  '10': 'j',
                                  '11': 'k',
                                  '12': 'l',
                                  '13': 'm',
                                  '14': 'n',
                                  '15': 'o',
                                  '00': 'X'
                                  }
        if 'a' in str:
            new_list = [letters_2_numbers_dict[x] for x in L]
        else:
            new_list = [numbers_2_letters_dict[x] for x in L]

        return ''.join(new_list)  # return as string

    # translate test case (list of lists) into string of letters
    def translate_test_case(self,LL):
        LL_str_list = ['0' * (2 - len(str(x))) + str(x) for sublist in LL for x in sublist]
        return self.translate(''.join(LL_str_list))

    # translate string of letters ie. '010203040506708' to list of lists ie. [[1,2,3,4],[5,6,7,8]]
    def translate_string_numbers_to_test_case(self, str):
        n = 2
        L = [int(str[i:i+n]) for i in range(0, len(str), n)]

        LL = [L[i:i + 4] for i in range(0, len(L), 4)]
        return LL


    # Custom data structure to translate from a tuple of position indexes (start, end) ie. (2,3) or (3,2)
    # to respective actions ie. Right or Left
    class DualWayMovesDict:
        def __init__(self, half_dict):
            self.dual_moves_dict = {}
            for idx, (key, value) in enumerate(half_dict.items()):
                self.dual_moves_dict[key] = value

                i1 = key[0]
                i2 = key[1]

                # self.dual_moves_dict[(i2, i1)] = value

                if value == 'R':
                    self.dual_moves_dict[(i2,i1)] = 'L'
                elif value == 'D':
                    self.dual_moves_dict[(i2,i1)] = 'U'





    # The main solver class, takes as input a test case (list of lists) and name of test case (string)
    def solve(self, Test_Case_N, Test_Case_Str):
        # declare half of the mappings from tuple of block indexes (start, end) ie. (2,3) or (3,2)
        # to respective actions ie. Right or Left
        # Later we will pass this into a DualWayMovesDict() class and essentially "double" the dictionary
        # since we know left and right, or up and down, are opposite moves to each other.
        numbers_tuple_dict = {(0,1):'R',
                              (1,2):'R',
                              (2,3):'R',
                              (4,5):'R',
                              (5,6):'R',
                              (6,7):'R',
                              (8,9):'R',
                              (9,10):'R',
                              (10,11):'R',
                              (12,13):'R',
                              (13,14):'R',
                              (14,15):'R',
                              (0,4):'D',
                              (1,5):'D',
                              (2,6):'D',
                              (3,7):'D',
                              (4,8):'D',
                              (5,9):'D',
                              (6,10):'D',
                              (7,11):'D',
                              (8,12):'D',
                              (9,13):'D',
                              (10,14):'D',
                              (11,15):'D',
                              }

        position_to_actionset_dict = self.DualWayMovesDict(numbers_tuple_dict)  # "double" the dictionary from positions to actions


        # Custom_Test_Case_1 = [[9,2,5,4],[13,11,0,3],[15,1,7,8],[10,6,14,12]]
        # Custom_Test_Case_2 = [[1,2,7,3],[11,6,8,0],[9,13,12,5],[14,15,4,10]]
        s = self.translate_test_case(Test_Case_N) # start position
        # s = self.translate_test_case(Custom_Test_Case_1) # start position

        solution = 'abcdefghijklmnoX' # desired solved position

        q = deque() # queue has O(1) pop time vs list's O(n)
        q.append(s)

        past_set = set() # store all previously checked nodes
        past_set.add(s)


        # Declare resulting state and corresponding action from a move (up to 4 possibilities) as None
        one = False
        two = False
        three = False
        four = False

        child_parent_dict = {} # keys are children, values are parents

        iterations = 0
        while(len(q) > 0):
        # while(iterations < 5000):

            node = q[0] # current node

            if node == solution:
                print("Solved!")
                break

            # locate index of "0"
            b = node.find('X') # blank index

            # Choose available moves (do not run into walls)
            if b == 0: # if blank tile index is 0
                one = self.swap(node, 0, 1) # first possible move swaps position index 0 and 1
                two = self.swap(node, 0, 4) # second possible move swaps position index 0 and 4
                three = False # no third move possible for this situation
                four = False # no third move possible for this situation
            elif b == 1:
                one = self.swap(node, 1, 0)
                two = self.swap(node, 1, 2)
                three = self.swap(node, 1, 5)
                four = False
            elif b == 2:
                one = self.swap(node, 2, 1)
                two = self.swap(node, 2, 3)
                three = self.swap(node, 2, 6)
                four = False
            elif b == 3:
                one = self.swap(node, 3, 2)
                two = self.swap(node, 3, 7)
                three = False
                four = False
            elif b == 4:
                one = self.swap(node, 4, 0)
                two = self.swap(node, 4, 5)
                three = self.swap(node, 4, 8)
                four = False
            elif b == 5:
                one = self.swap(node, 5, 1)
                two = self.swap(node, 5, 4)
                three = self.swap(node, 5, 6)
                four = self.swap(node, 5, 9)
            elif b == 6:
                one = self.swap(node, 6, 2)
                two = self.swap(node, 6, 5)
                three = self.swap(node, 6, 7)
                four = self.swap(node, 6, 10)
            elif b == 7:
                one = self.swap(node, 7, 3)
                two = self.swap(node, 7, 6)
                three = self.swap(node, 7, 11)
                four = False
            elif b == 8:
                one = self.swap(node, 8, 4)
                two = self.swap(node, 8, 9)
                three = self.swap(node, 8, 12)
                four = False
            elif b == 9:
                one = self.swap(node, 9, 5)
                two = self.swap(node, 9, 8)
                three = self.swap(node, 9, 10)
                four = self.swap(node, 9, 13)
            elif b == 10:
                one = self.swap(node, 10, 6)
                two = self.swap(node, 10, 9)
                three = self.swap(node, 10, 11)
                four = self.swap(node, 10, 14)
            elif b == 11:
                one = self.swap(node, 11, 7)
                two = self.swap(node, 11, 10)
                three = self.swap(node, 11, 15)
                four = False
            elif b == 12:
                one = self.swap(node, 12, 8)
                two = self.swap(node, 12, 13)
                three = False
                four = False
            elif b == 13:
                one = self.swap(node, 13, 9)
                two = self.swap(node, 13, 12)
                three = self.swap(node, 13, 14)
                four = False
            elif b == 14:
                one = self.swap(node, 14, 10)
                two = self.swap(node, 14, 13)
                three = self.swap(node, 14, 15)
                four = False
            elif b == 15:
                one = self.swap(node, 15, 11)
                two = self.swap(node, 15, 14)
                three = False
                four = False
            else:
                one = False
                two = False
                three = False
                four = False

            # Add new nodes to queue, and explored nodes set
            if one is not False:
                if not one in past_set:
                        q.append(one)
                        past_set.add(one)
                        child_parent_dict[one] = node # child is key, parent is current node
            if two is not False:
                if not two in past_set:
                        q.append(two)
                        past_set.add(two)
                        child_parent_dict[two] = node
            if three is not False:
                if not three in past_set:
                        q.append(three)
                        past_set.add(three)
                        child_parent_dict[three] = node
            if four is not False:
                if not four in past_set:
                        q.append(four)
                        past_set.add(four)
                        child_parent_dict[four] = node



            # add to checked list (or set, in this case)
            past_set.add(node)
            q.popleft() # remove first element of queue (as we have checked that)

            iterations += 1

        # print(past_set)
        # print(iterations)

        soln_list = []
        current_node = q[0]
        # Build back up node solution path (from goal to start)
        while(1):
            if current_node == s:
                soln_list.append(current_node)
                break

            soln_list.append(current_node)
            parent_node = child_parent_dict[current_node]
            current_node = parent_node

        # print(soln_list)
        soln_list.reverse() # reverse (to get start to goal)

        action_list = []
        # Build back up action set list
        for node in soln_list: # ignore first element (start pos) since it has no parent node
            p1 = node.find('X')
            try:
                p2 = child_parent_dict[node].find('X') # child is key, parent is current node
                action_list.append( position_to_actionset_dict.dual_moves_dict[(p2,p1)] )
            except:
                action_list.append('START')

        # action_list.reverse() # reverse (to get start to goal)

        print(action_list)

        ####### Send to text file ###########################
        soln_list_numbers = []
        for element in soln_list:
            soln_list_numbers.append(self.translate_string_numbers_to_test_case(self.translate(element)))

        # Save lists to file
        the_filename = Test_Case_Str + '.txt'
        with open(the_filename, 'w') as f:
            for s in soln_list_numbers:
                for e in s:
                    # print(', '.join(map(str, e)))
                    f.write(',  '.join(map(str, e)) + '\n')

                f.write('\n')
                # print("\n")




if __name__ == '__main__':
    solver_object = Solver()

    Test_Case_1 = [[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 7, 12], [13, 14, 11, 15]]
    Test_Case_2 = [[1, 0, 3, 4], [5, 2, 7, 8], [9, 6, 10, 11], [13, 14, 15, 12]]
    Test_Case_3 = [[0, 2, 3, 4], [1, 5, 7, 8], [9, 6, 11, 12], [13, 10, 14, 15]]
    Test_Case_4 = [[5, 1, 2, 3], [0, 6, 7, 4], [9, 10, 11, 8], [13, 14, 15, 12]]
    Test_Case_5 = [[1, 6, 2, 3], [9, 5, 7, 4], [0, 10, 11, 8], [13, 14, 15, 12]]

    solver_object.solve(Test_Case_1, "Test_Case_1")
    solver_object.solve(Test_Case_2, "Test_Case_2")
    solver_object.solve(Test_Case_3, "Test_Case_3")
    solver_object.solve(Test_Case_4, "Test_Case_4")
    solver_object.solve(Test_Case_5, "Test_Case_5")

    solver_object.solve(Test_Case_5, "nodePath") # Also write 5th test case to nodePath.txt

