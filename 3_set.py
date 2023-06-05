# searching O(K/N)
# двумерный массив, хеш таблица. Хеш функция "Остаток от деления"
# коллизия - совпадение значений хеш-функции для разных параметров.
# эффективно можно хранить только неизменяемые объекты.
# для неизменяемых объектов можно посчитать значение хеш-функции при из создании.
# хеш-функция должна давать равномерное распределение.
'''setsize = 10
myset = [[] for _ in range(setsize)]

def add(x):
    if not find(x):  # without this string we have multiset. Doesn't check entry 
        myset[x % setsize].append(x)

def find(x):
    for i in myset[x % setsize]:
        if i == x:
            return True
    return False

def delete(x):
    xlist = myset[x % setsize]
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i] = xlist[len(xlist) - 1]
            xlist.pop()
            return
        


add(32)
add(52)
print(myset)
print(find(52))
print(find(40))
delete(32)
print(myset)


# find in sequence two numbers if their sum == x 
def two(n, x):
    l = set()
    for num in n:
        if x - num in l:
            return num, x - num
        l.add(num)
    return 0, 0
        
        
print(two([1, 3, 5, 4, 8], 9))'''


# find word without letter
# нужно закончить
def generatedic(dic, text):
    goodwords = set(dic)
    for word in dic:
        for delpos in range(len(word)):
            goodwords.add(word[:delpos] + word[delpos + 1:])
    l = []
    for word in text:
        l.append(word in goodwords)
    print(l)

s = ['hello', 'byu', 'good']
ss = ['bu', 'helo']
generatedic(s, ss)
