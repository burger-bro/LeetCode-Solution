import random
import time

def test(func):
    MAX = 1000
    start_time = time.time()
    for _ in range(MAX):
        length = random.randint(0, MAX)
        case_array = [random.randint(-MAX, MAX) for _ in range(length)]
        answer = sorted(case_array)
        res = func(case_array)
        if answer != res:
            print("fail:")
            print(answer)
            print(res)
    print(f"{func.__name__} finish! time:{time.time() - start_time}")

def fair_multi_test(funcs):
    MAX = 1000
    funcs_time = [0] * len(funcs)
    for _ in range(MAX):
        length = random.randint(0, MAX)
        case_array = [random.randint(-MAX, MAX) for _ in range(length)]
        answer = sorted(case_array)

        for i, func in enumerate(funcs):
            start_time = time.time()
            res = func(case_array.copy())
            if answer != res:
                print("fail:")
                print(answer)
                print(res)
            funcs_time[i] += time.time() - start_time
    for i, func in enumerate(funcs):       
        print(f"{func.__name__} finish! time:{funcs_time[i]}")

def bubble(array):
    n = len(array)
    for i in range(n-1):
        for j in range(1, n-i):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
    return array

def bubble_new1(array):
    n = len(array)
    for i in range(n):
        break_flag = True
        for j in range(1, n-i):
            if array[j-1] > array[j]:
                break_flag = False
                array[j-1], array[j] = array[j], array[j-1]
        if break_flag: break
    return array

def bubble_new2(array):
    n = len(array)
    end = n
    while end:
        k = 0
        for j in range(1, end):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                k = j
        end = k
    return array

def bubble_new3(array):
    n = len(array)
    left, right = 0, n-1
    while left < right:
        flag = True

        for p in range(left, right):
            if array[p] > array[p+1]:
                flag = False
                array[p], array[p+1] = array[p+1], array[p]
                right = p

        for p in range(right, left, -1):
            if array[p-1] > array[p]:
                flag = False
                array[p-1], array[p] = array[p], array[p-1]
                left = p
        
        if flag: break
    # print(array)
    return array

def selection(array):
    n = len(array)
    for i in range(n):
        minimum = array[i]
        index = i
        for j in range(i+1, n):
            if array[j] < minimum:
                minimum = array[j]
                index = j
        if index != i:
            array[i], array[index] = array[index], array[i]
    return array

def selection_new1(array):
    n = len(array)
    for i in range(n-1):
        for j in range(i+1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

def merge_sort(array):
    n = len(array)
    if n == 1 or n == 0:
        return array
    middle = len(array)//2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    new = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    while i < len(left):
        new.append(left[i])
        i += 1
    while j < len(right):
        new.append(right[j])
        j += 1
    return new


def quick_sort(array):
    if len(array) == 1 or len(array) == 0:
        return array
    middle = array[-1]
    left, right = [], []
    for n in array[:-1]:
        if n < middle:
            left.append(n)
        else:
            right.append(n)
    left_new = quick_sort(left)
    right_new = quick_sort(right)
    return left_new + [middle] + right_new


def insertion(array):
    for i in range(1, len(array)):
        s = array[i]
        j = i
        while j - 1 >= 0 and array[j-1] > s:
            array[j] = array[j-1]
            j -= 1
        array[j] = s
    return array

def qsort(array):
    def helper(array, s, e):
        if s >= e: 
            return
        pivot = array[e]
        # p, q = 0, len(array)-1
        p, q = s, e
        while p < q:
            while p < q and array[p] <= pivot:
                p += 1
            array[q], array[p] = array[p], array[q]
            while p < q and array[q] >= pivot:
                q -= 1
            array[q], array[p] = array[p], array[q]
        helper(array, s, p-1)
        helper(array, q+1, e)
    helper(array, 0, len(array)-1)

    return array

case1 = [9, 3, 0, 2, 1, 100]
case2 = [9, 3, 0, 2, 1, 100, 5, 15, 0, 32, 4]
case3 = [1, 2, 3, 4, 7, 8, 9, 5]
case4 = [1, 1, 1, 1, 1]
case5 = [1, 2, 3, 4, 5]
case6 = [5, 4, 3, 2, 1]
# bubble_new3(case2)
# qsort(case6)
# insertion(case1)

# test(bubble)
# test(bubble_new1)
# test(bubble_new2)
# test(bubble_new3)
fair_multi_test([bubble_new1, bubble_new2, bubble_new3, bubble])

# test(bubble2)
# test(bubble_new2)
# test(selection)
# test(selection_new1)
# test(insertion)

# test(merge_sort)
# test(quick_sort)
# test(qsort)