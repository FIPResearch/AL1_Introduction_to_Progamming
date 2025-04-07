"""
練習問題 9： ファイルの読み込み
練習問題 10： 列の取り出し
"""
import pandas as pd
import numpy as np

# ファイルの読み込み
input_file = 'iris.csv'	# 読み込むファイル名
input_data = pd.read_csv(input_file)
input_data = np.array(input_data)

print(input_data)
