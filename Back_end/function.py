from random import randint
import numpy as np
import pandas as pd
from Back_end.Sort_solution import *
from Back_end.generate_dataset import *
from Back_end.poly_fit import *
from utils import logging_config


def generate_random_sequence(Min, Max, Seq_len, Seq_method):
    """
    1. 指定数组规模，按正序/逆序/乱序随机生成数组

    生成seq_len个数组成的随机序列，数组元素的值在[min, max)
    :param Min: 数组元素最小值
    :param Max: 数组元素最大值
    :param Seq_len: 数组长度
    :param Seq_method:前端选择的生成序列的排列方式 01-正序，02-乱序，03-倒序
    :return: seq_len个数组成的随机序列
    """

    Rand_seq = []
    if Seq_method == '01':
        init_num = randint(Min, Max)
        for i in range(Seq_len):
            Rand_seq.append(init_num + i)
    elif Seq_method == '02':
        Rand_seq = np.random.randint(Min, Max, size=Seq_len).tolist()
    elif Seq_method == '03':
        init_num = randint(Min, Max)
        while init_num < Seq_len:  # 保证序列里面不会出现负数
            init_num = randint(Min, Max)
        for i in range(Seq_len):
            Rand_seq.append(init_num - i)
    logging.info('rand seq:{}'.format(Rand_seq))
    return Rand_seq


def sort(Org_seq):
    """
    2. 对待排序的数组，分别按6种排序方式进行排序,返回各自排序结果及基本运算次数（比较、移动）

    :param Org_seq: 待排序的数组
    :return: 6种方式的排序结果
             6种方式的基本运算次数（比较、移动）
    """
    result_select = select_sort(Org_seq)  # 选择排序
    result_bubble = bubble_sort(Org_seq)  # 冒泡排序
    result_quick = quick_sort(Org_seq)  # 快速排序
    result_heap = heap_sort(Org_seq)  # 堆排序
    result_merge = merge_sort(Org_seq)  # 归并排序
    result_insert = insert_sort(Org_seq)  # 插入排序
    result_shell = ShellSort(Org_seq)
    result_radix = RadixSort(Org_seq)
    result_binaryInsert = BinaryInsertSort(Org_seq)
    result_coaktail = CoaktailSort(Org_seq)

    # 以字典形式存储6种排序方式对应对排序结果
    ordered_sequences = {
        'select': result_select[0],  # result_select[0] 有序数组
        'bubble': result_bubble[0],
        'quick': result_quick[0],
        'heap': result_heap[0],
        'merge': result_merge[0],
        'insert': result_insert[0],
        'shell': result_shell[0],
        'radix': result_radix[0],
        'binaryInsert': result_binaryInsert[0],
        'coaktail': result_coaktail[0]

    }

    # 以列表+字典形式存储6种排序方式的基本运算次数
    basic_operate_counts = [
        {'sort_type': 'select', 'compare_count': result_select[1], 'move_count': result_select[2]},
        {'sort_type': 'bubble', 'compare_count': result_bubble[1], 'move_count': result_bubble[2]},
        {'sort_type': 'quick', 'compare_count': result_quick[1], 'move_count': result_quick[2]},
        {'sort_type': 'heap', 'compare_count': result_heap[1], 'move_count': result_heap[2]},
        {'sort_type': 'merge', 'compare_count': result_merge[1], 'move_count': result_merge[2]},
        {'sort_type': 'insert', 'compare_count': result_insert[1], 'move_count': result_insert[2]},
        {'sort_type': 'shell', 'compare_count': result_shell[1], 'move_count': result_shell[2]},
        {'sort_type': 'radix', 'compare_count': result_radix[1], 'move_count': result_radix[2]},
        {'sort_type': 'binaryInsert', 'compare_count': result_binaryInsert[1], 'move_count': result_binaryInsert[2]},
        {'sort_type': 'coaktail', 'compare_count': result_coaktail[1], 'move_count': result_coaktail[2]},
    ]
    result_total = [result_select, result_bubble, result_quick, result_heap, result_merge, result_insert, result_shell,
                    result_radix, result_binaryInsert, result_coaktail]

    return result_total


def sort_on_basic_operators(Basic_Op_counts, Basic_Op, ascend=True):
    """
    3. 根据时间效率（比较，移动）对6种算法进行排序
    (对6种排序方式的比较次数or移动次数进行按生序or降序排序)

    :param Basic_Op_counts: 6种排序方式的基本运算次数
    :param Basic_Op: 'compare_count'/'move_count'  按比较次数/移动次数进行排序
    :param ascend: 升序or降序，默认为升序
    :return:
    """
    if ascend:
        print("对 {} 按升序排序: ".format(Basic_Op))
        sorted_relsults = sorted(Basic_Op_counts, key=lambda i: i[Basic_Op])
    else:
        print("对 {} 按降序排序: ".format(Basic_Op))
        sorted_relsults = sorted(Basic_Op_counts, key=lambda i: i[Basic_Op], reverse=True)

    print(sorted_relsults)
    return sorted_relsults


# 4. 指定最大规模及数组随机生成方式，对6种算法进行回归分析（比较次数和移动次数）
def regression_analysis(Seq_len_max, Min, Max, Sam_num, Seq_method):
    """
    4. 指定最大规模及数组随机生成方式，对6种算法进行回归分析（比较次数和移动次数）

    :param Seq_len_max: 最大规模
    :param Min: 数组元素最小值
    :param Max: 数组元素最大值
    :param Sam_num: 对于每个规模, 生成样本数量, 总计样本数量=(Seq_len_max-2)* Sam_num
    :param Seq_method: 前端选择的生成序列的排列方式 01-正序，02-乱序，03-倒序
    :return: 详见function_info
    """
    # Min = 0  # 数组元素最小值
    # Max = 100  # 数组元素最大值
    # Sam_num = 10  # 对于每个规模, 生成样本数量, 总计样本数量=(Seq_len_max-2)* Sam_num

    results_list = []

    Data_folder = 'data/'
    Sort_type_list = ['bubble_sort', 'quick_sort', 'select_sort', 'merge_sort', 'insert_sort', 'heap_sort',
                         "ShellSort", "RadixSort", "BinaryInsertSort", "CoaktailSort"]  # 差堆排序

    for Sort_type in Sort_type_list:
        Save_path = Data_folder + Sort_type
        generate_datasets(Min, Max, Seq_len_max, Sam_num, Sort_type, Save_path, Seq_method)

    for Sort_type in Sort_type_list:
        logging.info('\n--------------- Regression analysis of {} ---------------'.format(Sort_type))

        Sample = pd.read_csv(Data_folder + Sort_type + '.csv')
        Seq_len = np.array(Sample['seq_length'])
        Comp_count = np.array(Sample['compare_count'])
        Move_count = np.array(Sample['move_count'])
        logging.info('seq_len shape:{}'.format(Seq_len.shape))
        logging.info('comp_count shape:{}'.format(Comp_count.shape))
        logging.info('move_count shape:{}'.format(Move_count.shape))

        results = regression_using_polynomial(Sort_type, Seq_len, Comp_count, Move_count)
        # results 字典
        results_list.append(results)
    print(results_list)
    return results_list


def prediction_and_truth(Rand_seq):
    """
    5. 对于某一个待排序数组，根据其规模利用已经生成的回归模型进行预测'基本运算次数估计值',并调用排序算法计算其'基本运算次数实际值',返回估计值与实际值

    :param Rand_seq: 待排序的数组(由1生成)
    :return:
    """
    i = len(Rand_seq)  # 规模
    bubble_pre_compare_count = int(float((0.5 * i * i) + (-0.5 * i) + 0.0))
    bubble_pre_move_count = int(float((0.27 * i * i) + (-1.167 * i) + 6.239))
    _, bubble_truth_compare_count, bubble_truth_move_count = bubble_sort(Rand_seq)
    bubble_results = {'sort_type': 'bubble_sort',
                      'pre_comp_count': bubble_pre_compare_count,
                      'truth_comp_count': bubble_truth_compare_count,
                      'pre_move_count': bubble_pre_move_count,
                      'truth_move_count': bubble_truth_move_count}

    quick_pre_compare_count = int(float((0.05 * i * i) + (3.03 * i) + -9.82))
    quick_pre_move_count = int(float((0.05 * i * i) + (3.03 * i) + -9.82))
    _, quick_truth_compare_count, quick_truth_move_count = quick_sort(Rand_seq)
    quick_results = {'sort_type': 'quick_sort',
                     'pre_comp_count': quick_pre_compare_count,
                     'truth_comp_count': quick_truth_compare_count,
                     'pre_move_count': quick_pre_move_count,
                     'truth_move_count': quick_truth_move_count}

    select_pre_compare_count = int(float((0.5 * i * i) + (-0.5 * i) + 0.0))
    select_pre_move_count = int(float((0.0 * i * i) + (1.0 * i) + -1.0))
    _, select_truth_compare_count, select_truth_move_count = select_sort(Rand_seq)
    select_results = {'sort_type': 'select_sort',
                      'pre_comp_count': select_pre_compare_count,
                      'truth_comp_count': select_truth_compare_count,
                      'pre_move_count': select_pre_move_count,
                      'truth_move_count': select_truth_move_count}

    merge_pre_compare_count = int(float((0.04 * i * i) + (2.82 * i) + -8.35))
    merge_pre_move_count = int(float((0.02 * i * i) + (2.0 * i) + -5.05))
    _, merge_truth_compare_count, merge_truth_move_count = merge_sort(Rand_seq)
    merge_results = {'sort_type': 'merge_sort',
                     'pre_comp_count': merge_pre_compare_count,
                     'truth_comp_count': merge_truth_compare_count,
                     'pre_move_count': merge_pre_move_count,
                     'truth_move_count': merge_truth_move_count}

    insert_pre_compare_count = int(float((0.5 * i * i) + (-0.5 * i) + 0.0))
    insert_pre_move_count = int(float((0.27 * i * i) + (-0.95 * i) + 4.62))
    _, insert_truth_compare_count, insert_truth_move_count = insert_sort(Rand_seq)
    insert_results = {'sort_type': 'insert_sort',
                      'pre_comp_count': insert_pre_compare_count,
                      'truth_comp_count': insert_truth_compare_count,
                      'pre_move_count': insert_pre_move_count,
                      'truth_move_count': insert_truth_move_count}

    heap_pre_compare_count = int(float((0.0 * i * i) + (3.35 * i) + -8.02))
    heap_pre_move_count = int(float((0.0 * i * i) + (2.42 * i) + -4.16))
    _, heap_truth_compare_count, heap_truth_move_count = heap_sort(Rand_seq)
    heap_results = {'sort_type': 'heap_sort',
                    'pre_comp_count': heap_pre_compare_count,
                    'truth_comp_count': heap_truth_compare_count,
                    'pre_move_count': heap_pre_move_count,
                    'truth_move_count': heap_truth_move_count}
    results_list = [bubble_results, quick_results, select_results,
                    merge_results, insert_results, heap_results]
    print(results_list)
    return results_list


if __name__ == '__main__':
    logging_config(folder='log', name='functions')

    min = 0  # 数组元素最小值
    max = 100  # 数组元素最大值
    seq_len = 8  # 最大输入规模（数组长度)
    seq_len_max = 40
    sam_num = 10

    seq_method = '02'
    rand_seq = generate_random_sequence(min, max, seq_len, seq_method)
    ord_seqs, basic_Op_counts = sort(rand_seq)
    sort_on_basic_operators(basic_Op_counts, 'move_count', ascend=False)
    # regression_analysis(seq_len_max, min, max, sam_num, seq_method)

    prediction_and_truth(rand_seq)

    # result_num_test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # for i in result_num_test_list:
    #     compare_result = round(float((poly_fit_result['compare'][0] * i * i) + (poly_fit_result['compare'][1] * i)
    #                                  + poly_fit_result['compare'][2]), 2)
    #     compare_result_list.append(compare_result)
    #     move_result = round(float((poly_fit_result['move'][0] * i * i) + (poly_fit_result['move'][1] * i)
    #                               + poly_fit_result['move'][2]), 2)
    #     move_result_list.append(move_result)
