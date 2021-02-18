

# s = "abcdefghijklmnop" # p is fifteen
s = "pabcdefghijklmno" # p is fifteen
original = s
L = []

# locate index of "p"
b = s.find('p') # blank index


if b == 0:
    m = list(s)
    m[0], m[1] = m[1], m[0] # switch letters
    L.append(''.join(m)) # add to list

    m = list(s)
    m[0], m[4] = m[4], m[0]
    L.append(''.join(m)) # add to list
elif b == 1:
    pass
elif b == 2:
    pass
elif b == 3:
    m = list(s)
    m[3], m[2] = m[2], m[3]
    L.append(''.join(m))

    m = list(s)
    m[3], m[7] = m[7], m[3]
    L.append(''.join(m))
elif b == 4:
    pass
elif b == 5:
    pass
elif b == 6:
    pass
elif b == 7:
    pass
elif b == 8:
    pass
elif b == 9:
    pass
elif b == 10:
    pass
elif b == 10:
    pass
elif b == 12:
    m = list(s)
    m[12], m[8] = m[8], m[12]
    L.append(''.join(m))

    m = list(s)
    m[12], m[13] = m[13], m[12]
    L.append(''.join(m))
elif b == 13:
    pass
elif b == 14:
    pass
elif b == 15:
    m = list(s)
    m[12], m[8] = m[8], m[12]
    L.append(''.join(m))

    m = list(s)
    m[12], m[13] = m[13], m[12]
    L.append(''.join(m))

L
print(L)

