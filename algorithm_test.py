from random import randint
from Back_end.generate_dataset import generate_datasets
import pandas as pd
import numpy as np
from Back_end.poly_fit import regression_using_polynomial


def single_sequence(seq_n, seq_method):
    """
    :param seq_n: 排序算法测试要求生成的单个序列长度
    :param seq_method: 生成序列的方式分别为以下三种
    :return: 目标长度和生成方式的单个序列
    """
    result_seq = []  #待生成目标序列
    
    if seq_method == '01':
        init_num = randint(1, 300)
        for i in range(seq_n):
            result_seq.append(init_num + i)
    elif seq_method == '02':
        for i in range(seq_n):
            result_seq.append(randint(1, 300))
    elif seq_method == '03':
        init_num = 1
        while init_num < seq_n:
            init_num = randint(1, 300)
        for i in range(seq_n):
            result_seq.append(init_num - i)
    return result_seq


def poly_fit_speed_test():
    analyze_max_n = 500
    dataset_name = 'quick_sort'
    save_paths = 'data/quick_sort'
    analyze_data_method = '03'
    generate_datasets(1, 120, int(analyze_max_n), 10, dataset_name, save_paths, analyze_data_method)
    # 读取数据集seq_length、compare_count、move_count列作为参数，拟合得到系数和方差
    sample = pd.read_csv(save_paths + '.csv')
    seq_len = np.array(sample['seq_length'])
    comp_count = np.array(sample['compare_count'])
    move_count = np.array(sample['move_count'])
    print("start poly fit")
    poly_fit_result = regression_using_polynomial(dataset_name, seq_len, comp_count, move_count)
    print("finished")
    print(poly_fit_result)
