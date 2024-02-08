"""
演習課題 4 : 2次元データの取り扱い
"""

import pandas as pd
import numpy as np

# ファイルの読み込み
input_file = 'iris.csv'	# 読み込むファイル名
input_data = pd.read_csv(input_file)
input_data = np.array(input_data)

# 「variety」以外の要素を配列output_dataに入れる
output_data = []
for row in input_data:	# １行ずつ取り出して row に入れる
  # ここでコードを書いてください
  # ↓↓↓

  # ↑↑↑
	output_data.append(row[0:4])
output_data = np.array(output_data) # おまじない

# ここでcsvファイルを保存する内容を書いてください
# ↓↓↓

# ↑↑↑
print(output_data)
