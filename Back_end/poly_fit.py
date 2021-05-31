import numpy as np
import pandas as pd
import math
import logging
import matplotlib.pyplot as plt
from utils import logging_config
from sklearn.metrics import mean_squared_error, r2_score


def regression_using_polynomial(Save_Path, Seq_len, Comp_count, Move_count):
    """
    利用2次多项式（y=a(x**2)+bx+c）分别对比较次数和移动次数进行拟合
    拟合曲线画图保存在'results_pic/'中, 图像命名为dataset_name
    返回2个多项式的系数
    :param Dataset_name: 数据集名称,以排序类型命名
    :param Seq_len: 规模
    :param Comp_count: 比较次数
    :param Move_count: 移动次数
    :return: 2个多项式的系数
    """
    plt.clf()
    plt.scatter(Seq_len, Comp_count, c='#996699', label='Compare')
    plt.scatter(Seq_len, Move_count, c='#669999', label='Move')

    # np.polyfit:
    # Fit a polynomial p(x) = p[0] * x**deg + ... + p[deg] of degree deg to points (x, y).
    # Returns a vector of coefficients p that minimises the squared error in the order deg, deg-1, … 0.
    # Deg: Degree of the fitting polynomial
    coef_comp = np.polyfit(Seq_len, Comp_count, 2)
    logging.info('********************** Analysis of comparing **********************')
    logging.info('coefficients:{}'.format(coef_comp))
    poly_fit_comp = np.poly1d(coef_comp)
    plt.plot(Seq_len, poly_fit_comp(Seq_len), c='#666666', label="Regression line of comparing")
    logging.info('2-order polynomial:\n{}'.format(poly_fit_comp))

    # 计算拟合时的均方误差
    pred_comp_count = poly_fit_comp(Seq_len)
    poly_rmse_comp = np.sqrt(mean_squared_error(Comp_count, pred_comp_count))
    poly_rmse_comp = round(poly_rmse_comp, 2)
    logging.info('the RMSE of poly_fit_comp:{}'.format(poly_rmse_comp))

    # 多项式系数，保留两位小数
    a_comp = round(float(coef_comp[0]), 2)
    b_comp = round(float(coef_comp[1]), 2)
    c_comp = round(float(coef_comp[2]), 2)
    logging.info('y=a(x**2)+bx+c  a={}, b={}, c={}'.format(a_comp, b_comp, c_comp))

    coef_move = np.polyfit(Seq_len, Move_count, deg=2)
    logging.info('********************** Analysis of moving **********************')
    logging.info('coefficients:{}'.format(coef_move))
    poly_fit_move = np.poly1d(coef_move)  # 获得拟合多项式
    plt.plot(Seq_len, poly_fit_move(Seq_len), c='#666666', label="Regression line of moving")
    logging.info('2-order polynomial:\n{}'.format(poly_fit_move))

    # 计算拟合时的均方误差
    pred_move_count = poly_fit_move(Seq_len)
    poly_rmse_move = np.sqrt(mean_squared_error(Move_count, pred_move_count))
    poly_rmse_move = round(poly_rmse_move, 2)
    logging.info('the RMSE of poly_fit_move:{}'.format(poly_rmse_move))

    # 多项式系数，保留两位小数
    a_move = round(float(coef_move[0]), 2)
    b_move = round(float(coef_move[1]), 2)
    c_move = round(float(coef_move[2]), 2)
    logging.info('y=a(x**2)+bx+c  a={}, b={}, c={}'.format(a_move, b_move, c_move))

    plt.legend(loc='upper left')
    plt.xlabel('the length of sequence')
    plt.ylabel('times')

    plt.savefig(Save_Path + '.png')
    # plt.show()
    Dataset_name = Save_Path.split("/")[-1]
    print(Dataset_name)
    # 返回两个多项式的系数及均方根误差
    result_dict = {'sort_type': Dataset_name,
                   'compare': [a_comp, b_comp, c_comp, poly_rmse_comp],
                   'move': [a_move, b_move, c_move, poly_rmse_move]}

    return result_dict


if __name__ == '__main__':
    logging_config(folder='log', name='poly_fit')

    data_folder = './data/'
    saveFigFath_root = './resutls_pic/'

    dataset_name_list = ['bubble_sort', 'quick_sort', 'select_sort', 'merge_sort', 'insert_sort', 'heap_sort',
                         "ShellSort", "RadixSort", "BinaryInsertSort", "CoaktailSort"]  # 差堆排序

    for dataset_name in dataset_name_list:
        logging.info('\n--------------- Regression analysis of {} ---------------'.format(dataset_name))
        saveFigFath = saveFigFath_root + dataset_name
        sample = pd.read_csv(data_folder + dataset_name + '.csv')
        seq_len = np.array(sample['seq_length'])
        comp_count = np.array(sample['compare_count'])
        move_count = np.array(sample['move_count'])
        logging.info('seq_len shape:{}'.format(seq_len.shape))
        logging.info('comp_count shape:{}'.format(comp_count.shape))
        logging.info('move_count shape:{}'.format(move_count.shape))

        coefs = regression_using_polynomial(saveFigFath, seq_len, comp_count, move_count)
        # print(coefs['compare'])
        # print(coefs['move'])
