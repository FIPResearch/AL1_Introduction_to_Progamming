"""
リストを利用したforループ
"""
Fruits = ['オレンジ', 'りんご', 'バナナ']
Fruits.append('キウイ')

# リスト Fruits 内の要素を順番に取り出して fruit_ に入れる．
i = 1
for fruit_ in Fruits:
	print('{0}番目に好きなフルーツは{1}です．'.format(i, fruit_))
	i = i + 1