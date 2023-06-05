# 1 Построение массива префиксных сумм:
# O(N): prefixsum[i] = prefixsum[i-1] + nums[i-1]
# Ответ на запрос суммы на отрезке:
# O(N): sum(l, r) = prefixsum[r] - prefixsum[l]
# RSQ (range minimum/sum query) реализация через префиксные суммы
# 2 Два указателя


'''def makeprefixsum(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefixsum[i] = prefixsum[i-1] + nums[i-1]
    return prefixsum


def rsq(prefixsum, l, r):
    return prefixsum[r] - prefixsum[l]

a = makeprefixsum([2, 3, 1, 5, 3, 7, 4, 2])
print(rsq(a, 2, 6))'''

# O(NM) В худшем случае каждый запрос O(N). М - количество запросов
'''def cnt(nums, l, r):
    n = 0
    for i in range(l, r):
        if nums[i] == 0:
            n += 1
    return n

print(cnt([0, 3, 0, 5, 0, 7, 0, 2], 1, 7))'''


# Применяем идею префиксных сумм для аналогичной задачи
# O(N+M)
'''def makeprefixzeroes(nums):
    cnt = 0
    prefixzeroes = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        if nums[i-1] == 0:
            cnt += 1
        prefixzeroes[i] = cnt
    return prefixzeroes

def prefixzeroes(a, l, r):
    return a[r] - a[l]

a = makeprefixzeroes([2, 0, 1, 0, 3, 7, 0, 0])
print(prefixzeroes(a, 1, 5))'''


# нужно найти все нулевые суммы в рядом расположенных парах в последовательности
# O(N ** 3)

'''def count_zero_sum(nums):
    result = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sum_pair = 0
            for k in range(i, j):
                sum_pair += nums[k]
            if sum_pair == 0:
                result += 1
    return result

print(count_zero_sum([1, -1, 2, 3, -3, 4, 1]))'''

# мое решение, но я не понял. Какая-то фигня. Вроде нужно чтоб пары были из всех чисел, не только рядом расположенных
'''def count_zero_sum_2(nums):
    cnt = 0
    for i in range(0, len(nums) - 1):
        if nums[i] + nums[i + 1] == 0:
            cnt += 1
    return cnt

print(count_zero_sum_2([1, -1, 2, 3, -3, 4, 1]))'''

# нужно разобраться с этим решением. O(N)
'''def countprefixsums(nums):
    psv = {0 : 1}
    nowsum = 0
    for now in nums:
        nowsum += now
        if nowsum not in psv:
            psv[nowsum] = 0
        psv[nowsum] += 1
    return psv

def count_zero_sum(psv):
    cnt = 0
    for nowsum in psw:
        cntsum = psv[nowsum]
        cnt += cntsum * (cntsum - 1) // 2
    return cnt'''


# Два указателя
# упорядоченная последовательность
# O(N ** 2)
'''l = [1, 3, 7, 8]
def more(numbers, k):
    n = 0
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            if numbers[j] - numbers[i] > k:
                n += 1
    return n


print(more(l, 4))'''

#O(N)
'''l = [1, 3, 5, 7, 8]
def more(numbers, k):
    n = 0
    j = 0
    for i in range(len(numbers)):
        while j < len(numbers) and numbers[j] - numbers[i] <= k:
            j += 1
        n += len(numbers) - j
        
    return n


print(more(l, 4))'''

#футбольная команда
'''def bestteam(players):
    bestsum = 0
    nowsum = 0
    last = 0
    for first in range(len(players)):
        while last < len(players) and (last == first or players[first] \
        + players[first + 1] >= players[last]):
            nowsum += players[last]
            last += 1
        bestsum = max(bestsum, nowsum)
        nowsum -= players[first]
    return bestsum
    
print(bestteam([1, 1, 3, 3, 4, 6, 11]))'''

# merge
def merge(a, b):
    merged = [0] * (len(a) + len(b))
    l = []
    first = 0
    second = 0
    for k in range(len(a) + len(b)):
        if first != len(a) and (second == len(b) or a[first] < b[second]):
            merged[k] = a[first]
            first += 1
        else:
            merged[k] = b[second]
            second += 1
    return merged


print(merge([1, 2, 5, 7], [3, 4, 4]))
