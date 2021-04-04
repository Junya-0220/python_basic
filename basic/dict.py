#　辞書型

d = {'x': 10, 'y': 20}

print(d)  # {'x': 10, 'y': 20}
print(type(d))  # <class 'dict'>
print(d['x'])  # 10
print(d['y'])  # 20

# xに100を代入
d['x'] = 100
print(d)  # {'x': 100, 'y': 20}

# 新しいキーとバリューを追加する
d['z'] = 200
print(d)  # {'x': 100, 'y': 20, 'z': 200}

# 新しい辞書の登録の仕方
dict_test = dict(a=10, b=20)
print(dict_test)  # {'a': 10, 'b': 20}

# 辞書のメソッド

print('メソッドはここから')
d = {'x': 10, 'y': 20}
print(d)

# helpを使うとメソッドの解説が見れる
# help(d)

# keyを取りたい場合
k = d.keys()
print(k)

# valueを取りたい場合
v = d.values()
print(v)

# update
# 現在のdの値→{'x': 10, 'y': 20}
d2 = dict(x=1000, j=500)
print(d2)
# dをd2でオーバーライドする
d.update(d2)
print(d)  # {'x': 1000, 'y': 20, 'j': 500}

# 辞書型のコピー
print('###########辞書型のコピー######')
x = {'a': 1}
y = x
y['a'] = 1000
print(x['a'])
print(y['a'])

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

# 辞書型の使い所
# 本の目次と考えるとわかりやすい
fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300
}
print(fruits['apple'])
