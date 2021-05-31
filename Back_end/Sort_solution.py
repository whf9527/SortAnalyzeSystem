import logging
import math
from utils import logging_config


def bubble_sort(Orig_Seq):
    seq = Orig_Seq.copy()
    compare_count = 0
    move_count = 0
    for i in range(len(seq)):
        for j in range(len(seq) - i - 1):
            if seq[j] > seq[j + 1]:
                seq[j + 1], seq[j] = seq[j], seq[j + 1]
                move_count += 1
            else:
                pass
            compare_count += 1
    logging.info('bubble sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare_count, move_count))
    return [seq, compare_count, move_count]


def quick_sort(seq_o):
    """
    : seq: 未排序的列表，例如[10, 3, 5, 6]
    : return: [seq, compare, exchange]，seq为排好序的列表[3,5,6,10]，compare为比较次数，exchange为交换次数
    """
    seq = [i for i in seq_o]
    compare = 0
    exchange = 0
    if len(seq) < 2:
        logging.info('quick sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare, exchange))
        return [seq, compare, exchange]
    l = 0
    r = len(seq) - 1
    stack = [l, r]
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = seq[high]
        i = low - 1
        for j in range(low, high):
            compare += 1
            if seq[j] <= x:
                i += 1
                if i == j:
                    continue
                exchange += 1
                seq[i], seq[j] = seq[j], seq[i]
        if i + 1 != high:
            exchange += 1
            seq[i + 1], seq[high] = seq[high], seq[i + 1]
        stack.extend([low, i, i + 2, high])
    logging.info('quick sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare, exchange))
    return [seq, compare, exchange]


# %% 选择排序
def select_sort(Orig_Seq):
    seq = Orig_Seq.copy()
    compare = 0
    exchange = 0
    for i in range(len(seq) - 1):
        min_index = i
        for j in range(i + 1, len(seq)):
            compare += 1
            if seq[j] < seq[min_index]:
                min_index = j
        if min_index != i:
            seq[min_index], seq[i] = seq[i], seq[min_index]
            exchange += 1
    logging.info(
        'select sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare, exchange))
    return [seq, compare, exchange]


def merge(a, b):
    c = []
    a_idx, b_idx = 0, 0
    compare = 0
    exchange = 0
    if isinstance(a[0], list):
        compare += a[1]
        exchange += a[2]
        a = a[0]
    if isinstance(b[0], list):
        compare += b[1]
        exchange += b[2]
        b = b[0]
    while a_idx < len(a) and b_idx < len(b):
        compare += 1
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
            exchange += 1
    if a_idx == len(a):
        c.extend(b[b_idx:])
    else:
        c.extend(a[a_idx:])
        exchange += 1
    logging.info(
        'merge sort: sorted seq:{}, compare_count={}, move_count={}'.format(c, compare, exchange))
    return [c, compare, exchange]


# performs merge sort on the input array
def merge_sort(Orig_Seq):
    seq = Orig_Seq.copy()
    # a list of zero or one elements is sorted, by definition
    if len(seq) <= 1:
        logging.info(
            'merge sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, 0, 0))
        return seq, 0, 0
    # split the list in half and call merge sort recursively on each half
    left, right = merge_sort(seq[:int(len(seq) / 2)]), merge_sort(seq[int(len(seq) / 2):])
    # merge the now-sorted sublists
    return merge(left, right)


def insert_sort(Orig_Seq):
    # 插入排序
    seq = Orig_Seq.copy()
    compare = 0
    exchange = 0
    for i in range(1, len(seq)):
        key = seq[i]
        j = i - 1
        while j >= 0:
            compare += 1
            if seq[j] > key:
                seq[j + 1] = seq[j]
                seq[j] = key
                exchange += 1
            j -= 1
    logging.info(
        'insert sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare, exchange))
    return [seq, compare, exchange]


def heapify(arr, n, i, cn, num):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
        cn += 1

    if r < n and arr[largest] < arr[r]:
        largest = r
        cn += 1

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        num += 1
        cn += 1
        heapify(arr, n, largest, cn, num)
        # print(cn, num)
    # print('-', cn, num)
    return cn, num


def heap_sort(seq):

    arr = [i for i in seq]
    n = len(arr)
    exchange = 0
    compare = 0
    flag = 0

    if n <= 1:
        logging.info(
            'merge sort: sorted seq:{}, compare_count={}, move_count={}'.format(arr, compare, exchange))
        return [seq, compare, exchange]

    for i in range(0, n - 1, 1):
        if arr[i] > arr[i + 1] or arr[i] == arr[i + 1]:
            flag = -1
            break
        else:
            flag += 1
    if flag == n - 1:
        return [arr, int(n * math.log(n, 2)), 0]

    # Build a maxheap.
    for i in range(n, -1, -1):
        cpr, exc = heapify(arr, n, i, 0, 0)
        compare += cpr
        exchange += exc

        # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        exchange += 1
        cpr, exc = heapify(arr, i, 0, 0, 0)
        compare += cpr
        exchange += exc

    logging.info(
        'merge sort: sorted seq:{}, compare_count={}, move_count={}'.format(arr, compare, exchange))
    return [arr, compare, exchange]

# WHF add
#希尔排序
def ShellSort(Orig_Seq):
    """

    Parameters
    ----------
    Orig_Seq

    Returns
    -------

    """
    seq = Orig_Seq.copy()
    compare = 0
    exchange = 0
    n = len(seq)
    gap = n // 2

    if len(seq) <= 1:
        logging.info(
            'Shell sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare, exchange))
        return seq, 0, 0
    while gap > 0 :
        for i in range(gap,n):
            temp = seq[i]
            tail = i
            compare+= 1
            while tail >= gap and temp<seq[tail-gap]:
                exchange += 1
                seq[tail] = seq[tail-gap]
                tail = tail - gap
            seq[tail] = temp
        gap = gap // 2
    logging.info(
        'Shell sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare, exchange))
    return [seq, compare, exchange]

# WHF add
#基数排序
def RadixSort(Orig_Seq):
    """
    Parameters
    ----------
    Orig_Seq

    Returns
    -------
    object

    """
    seq = Orig_Seq.copy()
    compare = 0
    exchange = 0
    n_seq = len(seq)
    n_num = len(str(max(seq)))
    if n_seq <= 1:
        logging.info(
            'RadixSort sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare, exchange))
        return seq, 0, 0
    for k in range(n_num):
        bucket_list=[[] for i in range(10)]
        for i in seq:
            # exchange += 1
            bucket_list[i//(10**k)%10].append(i)
        count=0
        for i in bucket_list:
            for j in i:
                exchange += 1
                seq[count] = j
                count+=1
    logging.info(
        'Radix Sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare, exchange))
    return [seq, compare, exchange]

# WHF add
#二分插入排序
def BinaryInsertSort(Orig_Seq):
    # 取出列表长度
    seq = Orig_Seq.copy()
    compare = 0
    exchange = 0

    if len(seq) <= 1:
        logging.info(
            'BinaryInsert sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare, exchange))
        return seq, 0, 0
    for index in range(1, len(seq)):
        left = 0
        right = index - 1
        temp = seq[index]
        position = index
        while left <= right:
            mid = (left + right) // 2
            compare += 1    #计算比较次数
            if seq[mid] < temp:
                left = mid + 1
            else:
                right = mid - 1
        while position > left:
            exchange += 1       #计算移动次数
            seq[position] = seq[position-1]
            position -= 1
        exchange += 1
        seq[position] = temp

    logging.info(
        'BinaryInsert Sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare, exchange))
    return [seq, compare, exchange]


def CoaktailSort(Orig_Seq):
    seq = Orig_Seq.copy()
    compare = 0
    exchange = 0
    n = len(seq)
    flag = True

    if n <= 1:
        logging.info(
            'Coaktail sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare, exchange))
        return seq, 0, 0
    for i in range(n // 2):
        if flag:
            flag = False
            for j in range(i, n - i - 1):
                compare += 1
                if seq[j] > seq[j + 1]:
                    exchange += 1
                    seq[j], seq[j + 1] = seq[j + 1], seq[j]
                    flag = True
            for k in range(n - i - 2, i, -1):
                compare += 1
                if seq[k] < seq[k - 1]:
                    exchange += 1
                    seq[k], seq[k - 1] = seq[k - 1], seq[k]
                    flag = True
        else:
            break
    logging.info('Coaktail Sort: sorted seq:{}, compare_count={}, move_count={}'.format(seq, compare, exchange))
    return [seq, compare, exchange]

if __name__ == '__main__':
    logging_config(folder='log', name='sort_solution')
    sequence = [12, 34, 54, 2, 3]
    # bubble_sort(sequence)
    # quick_sort(sequence)
    # select_sort(sequence)
    # merge_sort(sequence)
    # insert_sort(sequence)
    # heap_sort(sequence)
    CoaktailSort(sequence)

    # print(heap_sort(sequence))
    print(CoaktailSort(sequence))
    # print(quick_sort(sequence))
