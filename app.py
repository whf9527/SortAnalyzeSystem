# coding=utf-8
from flask import Flask, render_template, request, json
from Back_end.Sort_solution import *
from Back_end.function import sort
from Back_end.generate_dataset import generate_datasets, generate_random_sequence
from Back_end.poly_fit import regression_using_polynomial
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result_seq_test', methods=['GET'])
def result_seq_test():
    """
    通过ajax传输获取待生成序列的长度，以及序列的排列方式
    调用序列生成函数generate_random_sequence（）得到目标序列
    将list转换为json数据格式
    :return: 将json格式的待排序序列返回到前端
    """
    cal_cap_n = request.args.get('cal_cap_n')
    range_method = request.args.get('range_method')
    result_seq = generate_random_sequence(1, 300, int(cal_cap_n), range_method)
    result_seq_json = json.dumps(result_seq)
    return result_seq_json


@app.route('/sort_result_test', methods=['GET'])
def sort_result_test():
    """
    通过ajax传输获取待排序序列
    调用排序函数得到排序后的序列以及完成一次排序后比较次数和移动次数，调用顺序为选择、冒泡、快速、堆、归并、插入
    将每一种排序算法的排序后序列，比较次数，移动次数生成一个List数组
    将list转换为json数据格式
    :return:
    """
    cal_test_data = request.args.get('cal_test_data')
    Org_Seq = json.loads(cal_test_data)  # json转化为list
    # 分别调用选择、冒泡、快速、堆、归并、插入排序算法（需要修改）
    test_sort_result = json.dumps(sort(Org_Seq))
    return test_sort_result


@app.route('/result_seq_analyze', methods=['GET'])
def result_seq_analyze():
    """
    通过ajax传输获取n-序列的最大规模，seq_method-生成序列的排列方式-正序、乱序、倒序
    遍历六种排序方式，生成完成排序后序列规模、比较次数、移动次数的数据集，调用顺序为选择、冒泡、快速、堆、归并、插入
    分别读取每种算法的数据集，以序列规模为x轴，比较次数、移动次数为y轴做2次回归分析，得到系数a1,a2,a3和均方差
    以n = [[0, 1, 2, 3, 4, 5, 6, 7, 8] 带入a1,a2,a3为多项式系数的二次方程计算对应的比较次数和移动次数
    得到list[[比较/移动次数系数], 均方差, [n], [拟合结果计算出来的比较/移动次数]]数组
    将两个数组合并
    将list转换为json数据格式
    :return:
    """
    # 获取最大序列长度，和生成序列的方式
    analyze_max_n = request.args.get('analyze_max_n')
    analyze_data_method = request.args.get('analyze_data_method')
    compare_time_fitting = []  # 存储6种排序算法关于比较次数的所有信息
    move_time_fitting = []  # 存储6种排序算法关于移动次数的所有信息
    fact_seq_zero = [0]  # 传递实际操作次数的时候，序列长度为0意义不大，为了与拟合结果比较，设定序列长度为0时，比较，移动次数均为0
    data_folder = './Back_end/data/'
    saveFigFath_root = './Back_end/resutls_pic/'
    dataset_name_list = ['bubble_sort', 'quick_sort', 'select_sort', 'merge_sort', 'insert_sort', 'heap_sort',
                         "ShellSort", "RadixSort", "BinaryInsertSort", "CoaktailSort"]

    for dataset_name in dataset_name_list:
        save_paths = data_folder + dataset_name
        saveFigFath = saveFigFath_root + dataset_name
        compare_result_list = []  # 单个排序算法比较次数拟合多项式的结果
        move_result_list = []  # # 单个排序算法移动次数拟合多项式的结果
        # 每次运行重新生成数据集
        generate_datasets(1, 100, int(analyze_max_n), 1, dataset_name, save_paths, analyze_data_method)

        # 读取数据集seq_length、compare_count、move_count列作为参数，拟合得到系数和方差
        sample = pd.read_csv(save_paths + '.csv')
        seq_len = np.array(sample['seq_length'])
        comp_count = np.array(sample['compare_count'])
        move_count = np.array(sample['move_count'])

        poly_fit_result = regression_using_polynomial(saveFigFath, seq_len, comp_count, move_count)

        # 根据计算出来的系数和n带入多项式中计算拟合数据的比较次数和移动次数，n为最大序列长度
        result_num_test_list = []
        for len_chart in range(int(analyze_max_n) + 1):
            result_num_test_list.append(len_chart)
        for i in result_num_test_list:
            compare_result = round(float((poly_fit_result['compare'][0] * i * i) + (poly_fit_result['compare'][1] * i)
                                         + poly_fit_result['compare'][2]), 2)
            compare_result_list.append(compare_result)
            move_result = round(float((poly_fit_result['move'][0] * i * i) + (poly_fit_result['move'][1] * i)
                                      + poly_fit_result['move'][2]), 2)
            move_result_list.append(move_result)
        """
        xyf: 拟合结果返回格式 '对比较次数拟合的结果'：[a1,a2,a3,rmse_comp],'对移动次数拟合的结果'：[a1,a2,a3,rmse_move]
            poly_fit_result['compare'][:3] 前3项为多项式系数
        poly_fit_result['compare'][3] 第三项为均方根误差
        """
        compare_time = [poly_fit_result['compare'][:3], poly_fit_result['compare'][3],
                        result_num_test_list, compare_result_list, fact_seq_zero + seq_len.tolist(),
                        fact_seq_zero + comp_count.tolist()]  # 存储单个排序算法比较次数所有信息
        move_time = [poly_fit_result['move'][:3], poly_fit_result['move'][3],
                     result_num_test_list, move_result_list, fact_seq_zero + seq_len.tolist(),
                     fact_seq_zero + move_count.tolist()]  # 存储单个排序算法移动次数所有信息
        compare_time_fitting.append(compare_time)
        move_time_fitting.append(move_time)
    test_time_two_total = [compare_time_fitting, move_time_fitting]
    test_time_two_total_json = json.dumps(test_time_two_total)
    return test_time_two_total_json


if __name__ == '__main__':
    app.run()
