# 1 find the leftmost occurrence of a number
# 2 fine the max number in a sequence
# 3 find second max number
# 4 find min even number
# 5 find all shotest words in a sentence
# 6 pitcraft
# 7 func rle

'''l = [1, 2, 3, 8, 4, 1]
def find_digit_left(seq, x):
    rez = -1
    for i in range(len(seq)):
        if seq[i] == 4:
            rez = i
            break
    print(rez)


l2 = [1, 2, 3, 4, 0, 1]
def find_digit_left_opt(seq, y):
    rez = -1
    for i in range(len(seq)):
        if seq[i] == 4 and rez == -1:
            rez = i
    print(rez)


find_digit_left(l, 8)
find_digit_left_opt(l2, 0)


# 2 fine the max number in a sequence
def search_max(seq):
    maxim = seq[0]
    for i in range(1, len(seq)):
        if maxim < seq[i]:
            maxim = seq[i]
    print(maxim)

search_max([1, 3, 5, 3, 8, 3, 1])

# can remember not value but index if the objects are very large
def search_max(seq):
    maxim = 0
    for i in range(1, len(seq)):
        if seq[maxim] < seq[i]:
            maxim = i
    print(seq[maxim])

search_max([1, 3, 5, 3, 8, 10, 1])

# 3 find second max number
def search_max(seq):
    maxim = 0
    l = []
    for i in range(1, len(seq)):
        if seq[maxim] <= seq[i]:
            maxim = i
    for j in range(len(seq)):
        if seq[j] == seq[maxim]:
            l.append(j)
    print(l[1])

search_max([1, 3, 10, 3, 8, 10, 1])

# second max if they don't repeat:
def search_max(seq):
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])
    for i in range(2, len(seq)):
        if seq[i] > max1:
            max2 = max1
            max1 = seq[i]
        elif seq[i] > max2:
            max2 = seq[i]    

    print(max1, max2)

search_max([1, 2, 4, 6, 3, 7, -8, 3, 1, 4])

# 4 find min even number
def even(seq):
    ev = seq[0]
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and ev > seq[i]:
            ev = seq[i]   
    else:
        ev = -1 
    print(ev)

even([1, 1, 3, 3, 3, 7, 3, 3, 1, 1])

#optimized
def even(seq):
    ev = -1
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (ev == -1 or seq[i] < ev):
            ev = seq[i]
    print(ev)

even([1, 1, 3, 3, 3, 7, 3, 4, 1, 1])

# optimized with flag / better choise
def even(seq):
    flag = False
    ev = -1
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (not flag or seq[i] < ev):
            ev = seq[i]
            flag = True
    print(ev)

even([1, 1, 3, 3, 3, 7, 3, 4, 1, 1])


# 5 find all shotest words in a sentence
def shortwords(words):
    m = words.split(' ')
    minlen = len(m[0])
    for word in m:
        if len(word) < minlen:
            minlen = len(word)
    s = []
    for word in m:
        if len(word) == minlen:
            s.append(word)
    print(' '.join(s))

shortwords('В языке Python есть еще унарный логический оператор not, то есть отрицание. Он превращает правду в ложь, 
а ложь в правду. Унарный он потому, что применяется к одному выражению, стоящему после него, а не справа и слева от него как 
в случае бинарных and и or.')


# 6 pitcraft
def isleflood(h):
    maxpos = 0
    for i in range(len(h)):
        if h[i] > h[maxpos]:
            maxpos = i
    ans = 0
    nown = 0
    for i in range(maxpos):
        if h[i] > nown:
            nown = h[i]
        ans += nown - h[i]
    nown = 0
    for i in range(len(h) - 1, maxpos, -1):
        if h[i] > nown:
            nown = h[i]
        ans += nown - h[i]
    return ans
    
print(isleflood([3, 2, 3, 5, 2, 6, 2, 3]))'''


# 7 func rle 
''' rle Кодирование длин серий (англ. run-length encoding, RLE) или кодирование повторов — алгоритм сжатия данных, 
заменяющий повторяющиеся символы (серии) на один символ и число его повторов. Серией называется последовательность, состоящая 
из нескольких одинаковых символов. При кодировании (упаковке, сжатии) строка одинаковых символов, составляющих серию, 
заменяется строкой, содержащей сам повторяющийся символ и количество его повторов.'''
'''def rle(s):
    lastsym = s[0]
    l = []
    b = 0
    for i in range(len(s)):
        if s[i] != lastsym:
            l.append(lastsym)
            l.append(str(i - b))
            lastsym = s[i]
            b = i
    l.append(lastsym)
    l.append(str(i - b))

        
    return ''.join(l)
        



print(rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBB'))'''