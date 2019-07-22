#快速排序简单版本，空间复杂度较高
import random

def QuickSort(target):
    left, mid, right = [], [], [] # 这三个必须为局部变量，一开始定义为全局变量导致三个list随着循环不断变大，耗尽内存卡死...
    if len(target) <= 1:
        return target
    else:
        temp = random.choice(target)
        for x in target:
            if x < temp:
                left.append(x)
            elif x > temp:
                right.append(x)
            else:
                mid.append(x)
        return QuickSort(left) + mid + QuickSort(right)

target = [18,22,1,6,2,88,7]
print("Origin list:", target)
print("Sorted list:", QuickSort(target))


# 快速排序原地排序版，不需要新增list，空间复杂度好
import random
def swap(numbers, a, b):
    numbers[a], numbers[b] = numbers[b], numbers[a]

def partition(numbers, left, right):
    p_index = random.randint(left,right)
    p_value = numbers[p_index]
    swap(numbers, p_index, right)

    s_index = left
    for i in range(left, right):
        if numbers[i] < p_value:
            swap(numbers, i, s_index)
            s_index += 1

    swap(numbers, s_index, right)
    return s_index

def sort(numbers, left=0, right=None):
    if right == None:
        right = len(numbers)-1
    if left > right:
        return 

    s_index = partition(numbers, left, right)
    sort(numbers, left, s_index-1)
    sort(numbers, s_index+1, right)

numbers = [9, 22, 88, 12, 0]
print("Origin list:", numbers)
sort(numbers)
print("Sorted list:", numbers)



