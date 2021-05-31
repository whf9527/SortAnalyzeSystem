from random import randint
import numpy as np
import pandas as pd
from Back_end.Sort_solution import *
from utils import logging_config


def generate_random_sequence(Min, Max, Seq_len, seq_method):
    """
    生成seq_len个数组成的随机序列，数组元素的值在[min, max)
    :param Min: 数组元素最小值
    :param Max: 数组元素最大值
    :param Seq_len: 数组长度
    :param seq_method:前端选择的生成序列的排列方式 01-正序，02-乱序，03-倒序
    :return: seq_len个数组成的随机序列
    """

    Rand_seq = []
    if seq_method == '01':
        init_num = randint(Min, Max)
        for i in range(Seq_len):
            Rand_seq.append(init_num + i)
    elif seq_method == '02':
        Rand_seq = np.random.randint(Min, Max, size=Seq_len).tolist()
    elif seq_method == '03':
        init_num = randint(Min, Max)
        while init_num < Seq_len:  # 保证序列里面不会出现负数
            init_num = randint(Min, Max)
        for i in range(Seq_len):
            Rand_seq.append(init_num - i)
    logging.info('rand seq:{}'.format(Rand_seq))
    return Rand_seq


def generate_datasets(Min, Max, Seq_len_max, Sample_num, Sort_type, Save_path, seq_method):
    """
    生成某个排序方式(Sort_type)的数据集
    :param Min: 数组元素最小值
    :param Max: 数组元素最大值
    :param Seq_len_max: 最大输入规模（数组的最大长度,数组长度范围:[1,Seq_len_max]）
    :param Sample_num: 对于每个输入规模, 生成样本的数量, 总计样本数量=seq_len_max* example_num
    :param Sort_type: 排序方式(冒泡排序,,,)
    :param Save_path: 数据集保存的路径
    :param seq_method:前端选择的生成序列的排列方式 01-正序，02-乱序，03-倒序
    :return:
    """
    # 每组样本由输入规模，比较次数，移动次数组成
    sample = pd.DataFrame({'sample_id': range(1, Seq_len_max * Sample_num + 1),
                           'seq_length': 0,
                           'compare_count': 0,
                           'move_count': 0})
    logging.info('sample:\n{}'.format(sample))
    logging.info('sample columns:{}'.format(sample.columns.values.tolist()))

    sample_count = 0  # 记录样本数量
    sorted_seq = []
    compare_count = 0
    move_count = 0

    for seq_len in range(1, Seq_len_max + 1):  # 1~seq_len_max 从长度为1开始生成
        logging.info('-------seq_len:{}-------'.format(seq_len))
        for n in range(Sample_num):
            rand_seq = generate_random_sequence(Min, Max, seq_len, seq_method)
            sorted_seq, compare_count, move_count = globals()[Sort_type](rand_seq)  #调用相应的排序算法，返回相应值
            sample.loc[sample_count, 'seq_length'] = seq_len
            sample.loc[sample_count, 'compare_count'] = compare_count
            sample.loc[sample_count, 'move_count'] = move_count
            sample_count += 1
            logging.info('## have generated sample:{}'.format(sample_count))

    logging.info('sample:\n{}'.format(sample))
    logging.info('sample columns:{}'.format(sample.columns.values.tolist()))
    logging.info(sample.describe())
    sample.to_csv(Save_path + '.csv', index=False)  # columns=44


if __name__ == '__main__':
    logging_config(folder='log', name='datasets')

    min = 0  # 数组元素最小值
    max = 100  # 数组元素最大值
    seq_len_max = 30  # 最大输入规模（数组长度)
    sample_num = 6  # 对于每个规模, 生成样本数量, 总计样本数量= seq_len_max * example_num
    seq_method = '02'

    data_folder = './data/'
    sort_type_list = ['bubble_sort', 'quick_sort', 'select_sort', 'merge_sort', 'insert_sort', 'heap_sort', "ShellSort", "RadixSort","BinaryInsertSort","CoaktailSort"]

    for sort_type in sort_type_list:
        save_path = data_folder + sort_type
        generate_datasets(min, max, seq_len_max, sample_num, sort_type, save_path, seq_method)
