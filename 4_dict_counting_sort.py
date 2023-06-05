# 1 counting_sort (сортировка подсчетом) O(N + K) and memory O(K)
# 2 dict

# 1 counting sort
'''def sort_count(seq):
    minval = min(seq)
    maxval = max(seq)
    k = (maxval - minval + 1)
    data = [0] * k
    for i in seq:
        data[i - minval] += 1
    nowpos = 0
    for j in range(0, k):
        for k in range(data[j]):
            seq[nowpos] = j + minval
            nowpos += 1
    return seq

l = [5, 4, 5, 3, 2, 1, 5]
n = 5
print(sort_count(l))


# Дано два числа x и y без ведущих нулей
# Необходимо проверить, можно ли получить первое из второго перестановкой цифр
def shift_digit(x, y):
    q = [x, y]
    data = [[0] * len(str(x))] * 2
    for i in range(2):
        while q[i] > 0:
            a = q[i] % 10
            q[i] //= 10
            data[i][a] += 1
    print(data[0] == data[1])


shift_digit(2021, 1202)'''

# 2 dict
# ассоциативная структура позволяющая по ключу узнавать значение
# Константа в сложности словарей заметно больше, чем у массивов, поэтому где можно - лучше использовать сортировку подсчетом.
# Сортировку подсчетом неразумно использовать, если данные разреженные.
#O(N)


'''def countbeatingrooks(rookcoords):
    def addrook(roworcol, key):
        if key not in roworcol:
            roworcol[key] = 0
        roworcol[key] += 1

    def countpairs(roworcol):
        pairs = 0
        for key in roworcol:
            pairs += roworcol[key] - 1
        return pairs

    
    rooksinrow = {}
    rooksincol = {}
    for row, col in rookcoords:
        addrook(rooksinrow, row)
        addrook(rooksincol, col)
    return countpairs(rooksinrow) + countpairs(rooksincol)
    
print(countbeatingrooks(((1, 2), (4, 2))))'''


# Дана строка. Выведите гистограмму как в примере (коды символов отсортированы) O(N ** 2)
# S = Hello, world!
'''def printchart(s):
    symcount = {}
    maxsymcount = 0
    for sym in s:
        if sym not in symcount:
            symcount[sym] = 0
        symcount[sym] += 1
        maxsymcount = max(maxsymcount, symcount[sym])
    sorteduniqsyms = sorted(symcount.keys())
    for row in range(maxsymcount, 0, -1):
        for sym in sorteduniqsyms:
            if symcount[sym] >= row:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(''.join(sorteduniqsyms))

printchart('Hello, world')'''


# сгрупировать слова по общим буквам

def sorted_words(words):
    groups = {}
    for word in words:
        sortedword = ''.join(sorted(word))
        if sortedword not in groups:
            groups[sortedword] = []
        groups[sortedword].append(word)
    ans = []
    for sortedword in groups:
        ans.append(groups[sortedword])
    return ans


print(sorted_words(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))

