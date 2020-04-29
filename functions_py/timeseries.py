import numpy as np
import pandas as pd

def read_data(input_file, i): 
    '''
    入力ファイルからデータを読み込む関数
    input_file: 入力ファイル
    i: データの列番後
    '''

    def to_date(x, y):
        return str(int(x)) + '-' + str(int(y))

    # 入力ファイルからデータを読み込んだら最初の行から開始日を取得し関数to_date()で変換

    input_data = np.loadtxt(input_file, delimiter=',')
    start = to_date(input_data[0, 0], input_data[0, 1])

    if input_data[-1, 1] == 12:
        year = input_data[-1, 0] + 1
        month = 1

    else:
        year = input_data[-1, 0]
        month = input_data[-1, 1] + 1

    end = to_date(year, month)

    date_indices = pd.date_range(start, end, freq = 'M')
    output = pd.Series(input_data[:, i], index=date_indices)
    return output
