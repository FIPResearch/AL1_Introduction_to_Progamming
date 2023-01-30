"""
    多項式回帰による予測
    
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
input_file = 'bukka.csv'  # 読み込むファイル名
input_data = pd.read_csv(input_file)
input_data = np.array(input_data)

years = input_data[:,0] # 年次
bukka = input_data[:,1] # 消費者物価指数

# おまじない (配列サイズを1次元から2次元に拡張)
years = years[:,np.newaxis]
bukka = bukka[:,np.newaxis]

"""
データの標準化
"""
from sklearn.preprocessing import StandardScaler
scaler_year = StandardScaler()
scaler_bukka = StandardScaler()
years_std = scaler_year.fit_transform(years) # 標準化した年次
bukka_std = scaler_bukka.fit_transform(bukka) # 標準化した消費者物価指数

"""
多項式回帰：degreeで○次関数を決める．
"""
# 年次を入力として消費者物価指数を予測する．
polynomial_features= PolynomialFeatures(degree=2) # 2次関数(直線)を使用
input_ploy = polynomial_features.fit_transform(years_std) # 入力を定める

# 線形モデルを当てはめる
model = LinearRegression()  # 回帰分析の準備
model.fit(input_ploy, bukka_std)    # 回帰分析の実施
bukka_pred = model.predict(input_ploy)# 回帰分析の結果を出力

# 標準化したデータを元に戻す
bukka_pred = scaler_bukka.inverse_transform(bukka_pred)

# グラフにプロットする
plt.plot(years, bukka)  # 実データ
plt.plot(years, bukka_pred) # 回帰結果
plt.xlabel('年次')
plt.ylabel('消費者物価指数')

# R2スコア
r2 = r2_score(bukka, bukka_pred)
print('R2 Score : {0:.2}'.format(r2))

"""
2023年，2030年の予測
"""
years_future = np.array([2023,2030]) # 予測したい年のデータ
years_future = years_future[:,np.newaxis] # おまじない

# 標準化
years_future = scaler_year.transform(years_future)

# 予測
input_ploy = polynomial_features.fit_transform(years_future) # 入力を定める
bukka_future = model.predict(input_ploy) # 予測の結果

# 標準化したデータを元に戻す
bukka_future = scaler_bukka.inverse_transform(bukka_future)

print(' 2023年の消費者物価指数：{0:.1f} '.format(bukka_future[0,0]))
print(' 2030年の消費者物価指数：{0:.1f} '.format(bukka_future[1,0]))
