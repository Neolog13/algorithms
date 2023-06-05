#first algorithm
s = 'abddcdgaafbdda'
letter = ''
most_max = 0
quantity = 0
for i in range(len(s)):
    quantity = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            quantity += 1
    if most_max < quantity:
        most_max = quantity
        letter = s[i]
print(letter)
# О(N ** 2)
# O(N)


#second algorithm with an optimized solution through the use of set
s = 'abddcdgaafbdda'
letter = ''
most_max = 0
quantity = 0
for i in set(s):
    quantity = 0
    for j in range(len(s)):
        if i == s[j]:
            quantity += 1
    if most_max < quantity:
        most_max = quantity
        letter = i
print(letter)
# O(Nk) k - количество уникальных букв
# O(N+k) = O(N) - храним не только строку, но и множество


#third algorithm with an most optimyzed solution through the use of dictionary
s = 'abddcdgaafbdda'
dic = {}
letter = ''
count = 0
for i in s:
    if i not in dic:
        dic[i] = 0
    dic[i] += 1
for key in dic:
    if dic[key] > count:
        count = dic[key]
        letter = key
print(letter)
# O(N+k) k будет константой, поэтому ей можно пренебречь
# O(k)