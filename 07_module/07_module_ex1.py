"""
練習問題 11： 関数の定義
"""
# 定義した関数を使う例
import pandas as pd
import numpy as np

# 関数：ファイルを読み込む
def read_file(file_name):
    input_data = pd.read_csv(file_name)
    input_data = np.array(input_data)
    return input_data

# 関数：ファイルを書き出す
# 	引数1：書き込むデータ，引数2：ファイル名
def write_file(data, output_file):
	# ファイルの書き込みを行う処理をここに書く
	return 0

# ファイルの読み込み
input_data1 = read_file('fruits.csv')
input_data2 = read_file('weather.csv')
input_data3 = read_file('icecream.csv')

# 読み込んだデータの表示
print(input_data1)
print(input_data2)
print(input_data3)

# 書き込むファイルの名前
output_file1 = 'output1.csv'
output_file2 = 'output2.csv'
output_file3 = 'output3.csv'

# ファイルの書き込み
#write_file(input_data1, output_file1)
#write_file(input_data2, output_file2)
#write_file(input_data3, output_file3)
