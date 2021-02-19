from collections import deque

def swap(s_, i1, i2):
    m = list(s_)
    m[i1], m[i2] = m[i2], m[i1] # switch letters
    return ''.join(m)  # return as string

# bidirectional translation of letter string to double digit number string
def translate(str_in):
    str = str_in.replace(" ","") # remove any whitespaces

    if 'a' in str:
        L = list(str)
    else:
        L = [str[i:i+2] for i in range(0,len(str), 2)]



    letters_2_numbers_dict = {'a':'01',
                     'b':'02',
                     'c':'03',
                     'd':'04',
                     'e':'05',
                     'f':'06',
                     'g':'07',
                     'h':'08',
                     'i':'09',
                     'j':'10',
                     'k':'11',
                     'l':'12',
                     'm':'13',
                     'n':'14',
                     'o':'15',
                     'X':'00'
                     }

    numbers_2_letters_dict = {'01':'a',
                     '02':'b',
                     '03':'c',
                     '04':'d',
                     '05':'e',
                     '06':'f',
                     '07':'g',
                     '08':'h',
                     '09':'i',
                     '10':'j',
                     '11':'k',
                     '12':'l',
                     '13':'m',
                     '14':'n',
                     '15':'o',
                     '00':'X'
                     }
    if 'a' in str:
        new_list = [letters_2_numbers_dict[x] for x in L]
    else:
        new_list = [numbers_2_letters_dict[x] for x in L]


    return ''.join(new_list)  # return as string



# s = "abcdefghijklmnoX" # p is fifteen
# s = "abcdefghijklmnXo" # p is fifteen
# s = "Xabcdefghijklmno" # p is fifteen
# s = "abcdeXfghijklmno" # p is fifteen

# s = translate('01 02 03 04 05 06 08 14 09 11 07 00 13 10 15 12')
# s = translate('01 02 03 04 05 06 07 08 09 10 11 12 13 00 14 15')
s = translate('01 02 03 04 05 06 07 08 09 10 11 12 13 00 14 15')
# s = translate('123456')

q = deque() # queue has O(1) pop time vs list's O(n)
q.append(s)

print(q)

past_set = set() # store all previously checked nodes
past_set.add(s)


one = None
two = None
three = None
four = None
while(len(q) > 0):

    if q[0] == 'abcdefghijklmnoX': # note: maybe consider reading q[0] to memory, since it's used later
        print("Solved!")
        break

    # locate index of "0"
    b = q[0].find('X') # blank index


    if b == 0:
        one = swap(q[0], 0, 1)
        two = swap(q[0], 0, 4)
        three = None
        four = None
    elif b == 1:
        one = swap(q[0], 1, 0)
        two = swap(q[0], 1, 2)
        three = swap(q[0], 1, 5)
        four = None
    elif b == 2:
        one = swap(q[0], 2, 1)
        two = swap(q[0], 2, 3)
        three = swap(q[0], 2, 6)
        four = None
    elif b == 3:
        one = swap(q[0], 3, 2)
        two = swap(q[0], 3, 7)
        three = None
        four = None
    elif b == 4:
        one = swap(q[0], 4, 0)
        two = swap(q[0], 4, 5)
        three = swap(q[0], 4, 8)
        four = None
    elif b == 5:
        one = swap(q[0], 5, 1)
        two = swap(q[0], 5, 4)
        three = swap(q[0], 5, 6)
        four = swap(q[0], 5, 9)
    elif b == 6:
        one = swap(q[0], 6, 2)
        two = swap(q[0], 6, 5)
        three = swap(q[0], 6, 7)
        four = swap(q[0], 6, 10)
    elif b == 7:
        one = swap(q[0], 7, 3)
        two = swap(q[0], 7, 6)
        three = swap(q[0], 7, 11)
        four = None
    elif b == 8:
        one = swap(q[0], 8, 4)
        two = swap(q[0], 8, 9)
        three = swap(q[0], 8, 12)
        four = None
    elif b == 9:
        one = swap(q[0], 9, 5)
        two = swap(q[0], 9, 8)
        three = swap(q[0], 9, 10)
        four = swap(q[0], 9, 13)
    elif b == 10:
        one = swap(q[0], 10, 6)
        two = swap(q[0], 10, 9)
        three = swap(q[0], 10, 11)
        four = swap(q[0], 10, 14)
    elif b == 11:
        one = swap(q[0], 11, 7)
        two = swap(q[0], 11, 10)
        three = swap(q[0], 11, 15)
        four = None
    elif b == 12:
        one = swap(q[0], 12, 8)
        two = swap(q[0], 12, 13)
        three = None
        four = None
    elif b == 13:
        one = swap(q[0], 13, 9)
        two = swap(q[0], 13, 12)
        three = swap(q[0], 13, 14)
        four = None
    elif b == 14:
        one = swap(q[0], 14, 10)
        two = swap(q[0], 14, 13)
        three = swap(q[0], 14, 15)
        four = None
    elif b == 15:
        one = swap(q[0], 15, 11)
        two = swap(q[0], 15, 14)
        three = None
        four = None
    else:
        one = None
        two = None
        three = None
        four = None

    if one is not None and not one in q:
        if not one in past_set:
            q.append(one)
    if two is not None and not two in q:
        if not two in past_set:
            q.append(two)
    if three is  not None and not three in q:
        if not three in past_set:
            q.append(three)
    if four is not None and not four in q:
        if not four in past_set:
            q.append(four)


    # add to checked list (or set, in this case)
    past_set.add(q[0])
    q.popleft() # remove first element of queue (as we have checked that)


    q
    print(q)

print(past_set)