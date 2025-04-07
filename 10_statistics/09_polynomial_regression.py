"""
    多項式回帰による予測

    練習問題 16：線形回帰と多項式回帰
    練習問題 17：多項式回帰の次数と過学習
    
    注意：このコードの実行前にに以下のコードを実行してください．
    
    !pip install japanize-matplotlib
    
"""


"""
モジュールのインポート
"""
import numpy as np  # Numpyモジュール
import pandas as pd # Pandasモジュール
import scipy as sp  # 数値計算用モジュール
import matplotlib.pyplot as plt   # プロット用モジュール
import japanize_matplotlib # 日本語表示用モジュール

from sklearn.preprocessing import PolynomialFeatures # 回帰分析する入力を定める関数
from sklearn.linear_model import LinearRegression # 回帰分析する関数
from sklearn.metrics import r2_score # R2スコア(どれだけモデルがデータにマッチしているか)算出

"""
データの読みこみ
"""
input_file = 'fruits.csv'  # 読み込むファイル名
input_data = pd.read_csv(input_file)
input_data = np.array(input_data)

years = input_data[:,0] # 年次
mikan = input_data[:,1] # みかんの収穫量

# おまじない (配列サイズを1次元から2次元に拡張)
years = years[:,np.newaxis]
mikan = mikan[:,np.newaxis]

"""
多項式回帰：degreeで○次関数を決める．
"""
# 年次を入力としてみかんの収穫量を予測する．
polynomial_features= PolynomialFeatures(degree=2) # 2次関数(直線)を使用
input_ploy = polynomial_features.fit_transform(years) # 入力を定める

# 線形モデルを当てはめる
model = LinearRegression()  # 回帰分析の準備
model.fit(input_ploy, mikan)    # 回帰分析の実施
mikan_pred = model.predict(input_ploy)# 回帰分析の結果を出力

# グラフにプロットする
plt.plot(years, mikan)  # 実データ
plt.plot(years, mikan_pred) # 回帰結果
plt.xlabel('年次')
plt.ylabel('収穫量 [t]')

# R2スコア
r2 = r2_score(mikan, mikan_pred)
print('R2 Score : {0:.2}'.format(r2))

# 2023年，2030年の予測
years_future = np.array([2023,2030]) # 予測したい年のデータ
years_future = years_future[:,np.newaxis] # おまじない

input_ploy = polynomial_features.fit_transform(years_future) # 入力を定める
mikan_future = model.predict(input_ploy) # 予測の結果

print(' 2023年のみかんの収穫量：{0:.0f} t'.format(mikan_future[0,0]))
print(' 2030年のみかんの収穫量：{0:.0f} t'.format(mikan_future[1,0]))
