from collections import deque
import time
st = time.time()

class Solver:
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

    # Custom data structure to translate from a tuple of position indexes (start, end) ie. (2,3) or (3,2)
    # to respective actions ie. Right or Left
    class DualWayMovesDict():
        def __init__(self, half_dict):
            self.dual_moves_dict = {}
            for idx, (key, value) in enumerate(half_dict.items()):
                self.dual_moves_dict[key] = value

                i1 = key[0]
                i2 = key[1]

                self.dual_moves_dict[(i2, i1)] = value

                # if value == 'R':
                #     self.dual_moves_dict[(i2,i1)] = 'L'
                # elif value == 'D':
                #     self.dual_moves_dict[(i2,i1)] = 'U'







    def solve(self):
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

        # s = "abcdefghijklmnoX" # o is fifteen
        # s = "abcdefghijklmnXo" # o is fifteen
        # s = "Xabcdefghijklmno" # o is fifteen
        # s = "abcdeXfghijklmno" # o is fifteen

        # s = translate('01 02 03 04 05 06 08 14 09 11 07 00 13 10 15 12')
        # s = translate('01 02 03 04 05 06 07 08 09 10 11 12 13 00 14 15')
        # s = translate('01 02 03 04 05 06 07 08 09 10 11 12 13 00 14 15')
        # s = translate('123456')

        Test_Case_1 = [[1, 2, 3, 4],[ 5, 6, 0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]]
        Test_Case_2 = [[1, 0, 3, 4],[ 5, 2, 7, 8], [9, 6, 10, 11] , [13, 14, 15, 12]]
        Test_Case_3 = [[0, 2, 3, 4],[ 1,5, 7, 8], [9, 6, 11, 12] , [13, 10, 14, 15]]
        Test_Case_4 = [[5, 1, 2, 3],[0,6, 7, 4], [9, 10, 11, 8] , [13, 14, 15, 12]]
        Test_Case_5 = [[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]]

        # Custom_Test_Case_1 = [[9,2,5,4],[13,11,0,3],[15,1,7,8],[10,6,14,12]]
        s = self.translate_test_case(Test_Case_5) # start position
        # s = translate_test_case(Custom_Test_Case_1) # start position

        solution = 'abcdefghijklmnoX' # desired solved position

        q = deque() # queue has O(1) pop time vs list's O(n)
        q.append(s)

        print(q)

        past_set = set() # store all previously checked nodes
        past_set.add(s)


        # Declare resulting state and corresponding action from a move (up to 4 possibilities) as None
        one = None; one_a =  None
        two = None; two_a =  None
        three = None; three_a =  None
        four = None; four_a =  None

        child_parent_dict = {} # keys are children, values are parents

        max_length_q = len(q)
        iterations = 0
        while(len(q) > 0):
        # while(iterations < 5000):

            if q[0] == solution: # note: maybe consider reading q[0] to memory, since it's used later
                print("Solved!")
                break

            # locate index of "0"
            b = q[0].find('X') # blank index


            if b == 0:
                one = self.swap(q[0], 0, 1)
                two = self.swap(q[0], 0, 4)
                three = None
                four = None
            elif b == 1:
                one = self.swap(q[0], 1, 0)
                two = self.swap(q[0], 1, 2)
                three = self.swap(q[0], 1, 5)
                four = None
            elif b == 2:
                one = self.swap(q[0], 2, 1)
                two = self.swap(q[0], 2, 3)
                three = self.swap(q[0], 2, 6)
                four = None
            elif b == 3:
                one = self.swap(q[0], 3, 2)
                two = self.swap(q[0], 3, 7)
                three = None
                four = None
            elif b == 4:
                one = self.swap(q[0], 4, 0)
                two = self.swap(q[0], 4, 5)
                three = self.swap(q[0], 4, 8)
                four = None
            elif b == 5:
                one = self.swap(q[0], 5, 1)
                two = self.swap(q[0], 5, 4)
                three = self.swap(q[0], 5, 6)
                four = self.swap(q[0], 5, 9)
            elif b == 6:
                one = self.swap(q[0], 6, 2)
                two = self.swap(q[0], 6, 5)
                three = self.swap(q[0], 6, 7)
                four = self.swap(q[0], 6, 10)
            elif b == 7:
                one = self.swap(q[0], 7, 3)
                two = self.swap(q[0], 7, 6)
                three = self.swap(q[0], 7, 11)
                four = None
            elif b == 8:
                one = self.swap(q[0], 8, 4)
                two = self.swap(q[0], 8, 9)
                three = self.swap(q[0], 8, 12)
                four = None
            elif b == 9:
                one = self.swap(q[0], 9, 5)
                two = self.swap(q[0], 9, 8)
                three = self.swap(q[0], 9, 10)
                four = self.swap(q[0], 9, 13)
            elif b == 10:
                one = self.swap(q[0], 10, 6)
                two = self.swap(q[0], 10, 9)
                three = self.swap(q[0], 10, 11)
                four = self.swap(q[0], 10, 14)
            elif b == 11:
                one = self.swap(q[0], 11, 7)
                two = self.swap(q[0], 11, 10)
                three = self.swap(q[0], 11, 15)
                four = None
            elif b == 12:
                one = self.swap(q[0], 12, 8)
                two = self.swap(q[0], 12, 13)
                three = None
                four = None
            elif b == 13:
                one = self.swap(q[0], 13, 9)
                two = self.swap(q[0], 13, 12)
                three = self.swap(q[0], 13, 14)
                four = None
            elif b == 14:
                one = self.swap(q[0], 14, 10)
                two = self.swap(q[0], 14, 13)
                three = self.swap(q[0], 14, 15)
                four = None
            elif b == 15:
                one = self.swap(q[0], 15, 11)
                two = self.swap(q[0], 15, 14)
                three = None
                four = None
            else:
                one = None
                two = None
                three = None
                four = None

            if one is not None:
                if not one in past_set:
                        q.append(one)
                        past_set.add(one)
                        child_parent_dict[one] = q[0] # child is key, parent is current node
            if two is not None:
                if not two in past_set:
                        q.append(two)
                        past_set.add(two)
                        child_parent_dict[two] = q[0]
            if three is  not None:
                if not three in past_set:
                        q.append(three)
                        past_set.add(three)
                        child_parent_dict[three] = q[0]
            if four is not None:
                if not four in past_set:
                        q.append(four)
                        past_set.add(four)
                        child_parent_dict[four] = q[0]

            current_length_q = len(q)
            if current_length_q >= max_length_q:
                max_length_q = current_length_q


            # add to checked list (or set, in this case)
            past_set.add(q[0])
            q.popleft() # remove first element of queue (as we have checked that)


            # q
            # print(q)
            # print( str(iterations) + "----%.2f----" % (time.time() - st))
            iterations += 1

        print(past_set)
        print(iterations)

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

        soln_list.reverse() # reverse (to get start to goal)

        action_list = []
        # Build back up action set list
        for node in soln_list: # ignore first element (start pos) since it has no parent node
            p1 = node.find('X')
            try:
                p2 = child_parent_dict[node].find('X')
                action_list.append( position_to_actionset_dict.dual_moves_dict[(p1,p2)] )
            except:
                action_list.append('SSS')

        print("length of set: ", len(past_set))
        print(max_length_q)
        pass

if __name__ == '__main__':
    solver_object = Solver()
    solver_object.solve()
