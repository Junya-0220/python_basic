print('xxxxxx')
# test
print('yyyyyy')

"""
コメントを複数行書きたい場合は
こんなかんじで囲ってあげるといいよ
"""

x = 10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('1000000000')
else:
    print('positive')

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

y = [1, 2, 3]
x = 1

if 1 in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

if a != b:
    print('Not equal')

is_ok = True
if not is_ok:
    print('hello')

if is_ok:
    print('ok')


is_ok = ['a']


if len(is_ok) > 0:
    print('ok')
else:
    print('ng')

is_empty = None
print(is_empty)

if is_empty is None:
    print('None')
