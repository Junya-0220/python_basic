# 集合


a = {1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 6, 7, 7, 8, 9}
# 重複したものが削除される
print(a)
print(type(a))

b = {2, 3, 4, 5}
y = a - b

print(y)

# 重複したものが返る
x = a & b
print(x)

s = {1, 2, 3, 4, 5}
s.add(6)
print(s)
s.add(6)
s.remove(6)
print(s)
s.clear()
print(s)

my_friends = {'A', 'B', 'D'}
A_friends = {'A', 'C'}
print(my_friends & A_friends)

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)
