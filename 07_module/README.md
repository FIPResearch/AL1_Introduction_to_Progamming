# モジュールと関数

Pythonは他のプログラミング言語と比べて，短いコードで複雑な処理を実行できるという特徴があります．
それを実現している要因が「モジュールと関数」が豊富に用意してあることです．
ここでは，モジュールと関数の使い方について学びましょう．

--- 
### モジュールと関数の基本

**関数** とは，データを受け取り，予め定められた処理を行って結果を返す命令のことをさします．例えばこれを見てみましょう．
```Python
print('Hello World!')
```
ここにある `print()` は， `'Hello World!'`という文字列を受け取り，出力に表示させる関数なんですね．Pythonには他にも膨大な数の関数が用意されています．

さて，関数を使うための準備を行いましょう．次のコードを見てください．
```Python
import pandas
```
この ` import` は，**モジュール** を読み込むための命令です．
モジュールとは，複数の関数をひとまとめにしたパッケージのことを指します．
例えば２行目の `pandas` というパッケージには以下の関数が収められています．

##### pandasパッケージ内の関数
- `read_csv()`：CSVファイルを読み込む．
- `to_csv()`：CSVファイルを書き込む．
- `read_excel()`：Excelファイル(.xlsx)を読み込む．
- `to_excel()`：Excelファイル(.xlsx)を書き込む．

他にも様々な関数がありますが，ここでは割愛します．( 特にモジュール内の関数のことを **メソッド** と読んだりします．) 

これらの関数を使うには， `import pandas` でモジュールを読み込んだあとに， `モジュール名.関数名` で関数を使えます．
例えば，
```Python
data = pandas.read_csv('input.csv')
```
で関数 `read_csv()` を使用できます．関数の実行結果は左辺の `data` に返されます．

---
### インポートの書き方

最初に `import` の書き方についてコメントします．
##### importの書き方
- 以下のコードでモジュールを読み込み，`as` 以降の名前で呼び出す．
```Python
import モジュール名 as 好きな名前
```
- 基本的に，`import` 文はコードの最初に書く．
- モジュールの関数(メソッド)を使うには，モジュール名に '.' して関数名を書く．例えば，`pandas.read_csv()` など．

`as` は「～として」という意味の英単語ですね．
例えばモジュール `pandas` の関数を使う際，いちいち `pandas.(関数名)` と書くのも煩わしいです．そんなとき，`as` を使って `pandas` を `pd` と名付けます．
```Python
import pandas as pd
```
これによって，例えば上の `read_csv()` に関するコードを実行する場合，`pandas` を `pd` に置き換えて
```Python
data = pd.read_csv('input.csv')
```
と書けばOKです．「書く量がちょっと少なくなっただけでは？」と感じるかもしれません．しかし長いコードを書いていると，この省略がものすご～くありがたく感じるものです．ぜひこの書き方に慣れましょう．

---
### 関数の定義

自分で関数を作ることも可能です．
繰り返し実行する処理はひとまとめに関数にしてしまうと便利です．
それでは関数を作る方法（定義）について簡単にコメントします．
##### 関数の定義
- 関数を以下のコードで定義する．
```Python
def 関数名 (引数1, 引数2, 引数3, ...):
	処理させたい内容
	...
	return 戻り値
```
- 「関数名」には好きな名前をいれることができる．
- 「引数1, 引数2, ...」 には処理に使う変数を書く．**引数** とは関数が受け取る変数のこと．
- 関数の最後に `return` を書く．`return` のあとに返したい処理結果を書く． **戻り値** とは関数が返す変数のこと．

例えば，複数のファイルを読み込む場合のコードを見てみましょう．
```Python
# 関数を定義しない例
import pandas as pd
import numpy as np
 
# ファイルの読み込み1
input_file = 'input1.csv'	# 読み込むファイル名
input_data1 = pd.read_csv(input_file)
input_data1 = np.array(input_data1)
 
# ファイルの読み込み2
input_file = 'input2.csv'	# 読み込むファイル名
input_data2 = pd.read_csv(input_file)
input_data2 = np.array(input_data2)
 
# ファイルの読み込み3
input_file = 'input3.csv'	# 読み込むファイル名
input_data3 = pd.read_csv(input_file)
input_data3 = np.array(input_data3)
 
# 読み込んだデータの表示
print(input_data1)
print(input_data2)
print(input_data3)
```

似たような処理ブロックが何度も出てきて，見にくいですよね．
これを関数を使って書き直すとこうなります．

```Python
# 定義した関数を使う例
import pandas as pd
import numpy as np
 
# 関数の定義
def read_file(file_name):
	input_data = pd.read_csv(file_name)
	input_data = np.array(input_data)
	return input_data
 
# ファイルの読み込み
input_data1 = read_file('input1.csv')
input_data2 = read_file('input2.csv')
input_data3 = read_file('input3.csv')
 
# 読み込んだデータの表示
print(input_data1)
print(input_data2)
print(input_data3)
```
すっきりとした印象ですよね？
このコードでは関数 `read_file()` を定義しています．
`read_file()` の引数には `file_name` がありますね．`file_name` は読み込むファイル名が入る引数です．

定義した関数を使うときにはこう書きます．
```Python
input_data1 = read_file('input1.csv')
```
引数 `file_name` に対応するところにファイル名を書いています．
戻り値 `input_data1` には読み込んだデータが入ります．

---
## 練習問題
### 練習問題 11： 関数の定義

コード [`07_module_ex1.py`](07_module_ex1.py) を眺めましょう．
ファイルからデータを読み込み，その読み込んだデータを別のファイルに書き込もうとしています．
関数 `write_file()` を正しく書き直し，データをファイルに書き出す処理を行うようにしてください．

使用するファイルは以下のリンクから開けます．

[>> `icecream.csv`](https://raw.githubusercontent.com/YosukeSugiura/Introduction_to_Programming/main/07_module/icecream.csv)  
[>> `fruits.csv`](https://raw.githubusercontent.com/YosukeSugiura/Introduction_to_Programming/main/07_module/fruits.csv)  
[>> `weather.csv`](https://raw.githubusercontent.com/YosukeSugiura/Introduction_to_Programming/main/07_module/weather.csv)

> ヒント：関数 `write_file()` の引数の１つ目は書き出すデータ，引数の２つ目は書き出すファイル名です．

---
## 演習課題
### 演習課題 5： 関数の定義１

コード [`07_module_def.py`](07_module_def.py) を眺めましょう．第１の処理ではリストの中に指定した果物があるかを検索し，結果を表示します．第２の処理ではリストの中に指定した動物があるかを検索し，結果を表示します．これらの処理には共通する部分がありますよね．共通する処理を関数にしましょう．

> ヒント：関数を定義するとき，`検索するリスト`と`検索ワード`の２つを引数に設定しましょう．


<!--
### 演習課題２： 関数の定義２

コードをさらに書き直し，リストに指定の文字がある場合，リストの何番目にあるかを表示させる処理してください．

> ヒント：ループの前に新たに変数 `Cnt=0` を用意して，インクリメントを利用すれば，リストの番目がわかります．
-->

---
[< 前へ](../06_read_write) | [トップに戻る](https://github.com/YosukeSugiura/Introduction_to_Programming) | [次へ >](../08_prob_plot)
