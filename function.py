# def say_something():
#     print('hi')


# print(type(say_something))
# f = say_something
# f()


# def say_something2():
#     s = 'hi2'
#     return s


# result = say_something2()
# print(result)


# def what_is_this(color):
#     if color == 'red':
#         return 'tomaoto'
#     elif color == 'green':
#         return 'green papper'
#     else:
#         return 'I don\'t know'


# result = what_is_this('green')
# print(result)

# num: int = 10


# def add_num(a: int, b: int) -> int:
#     return a + b


# r = add_num('a', 'b')
# print(r)

# def menu(entree='beef', desert='ice', drink='wine'):
#     print('entree =', entree)
#     print('drink = ', drink)
#     print('desert = ', desert)


# menu(entree='chiken')

# def test_func(x, l=None):
#     if l is None:
#         l = []
#     l.append(x)
#     return l


# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)

# y = [1, 2, 3]
# r = test_func(200, y)
# print(r)

# r = test_func(100)
# print(r)

# r = test_func(100)
# print(r)

# def say_something(word, *args):
#     print('word = ', word)
#     for i in args:
#         print(i)


# t = ('Mike', 'Nancy')
# say_something('Hi', *t)

# def menu(**kwargs):
#     for k, v in kwargs.items():
#         print(k, v)


# d = {
#     'entree': 'beef',
#     'drink': 'ice coffee',
#     'desert': 'ice'
# }
# menu(**d)

# def outer(a, b):
#     def plus(c, d):
#         return c + d

#     r1 = plus(a, b)
#     r2 = plus(b, a)
#     print(r1 + r2)


# outer(1, 2)


# def outer(a, b):
#     def inner():
#         return a + b
#     return inner


# f = outer(1, 2)
# r = f()
# print(r)

# def print_more(func):
#     def wrapper(*args, **kwargs):
#         print('func:', func.__name__)
#         print('args', args)
#         print('kwargs:', kwargs)
#         result = func(*args, **kwargs)
#         print('result:', result)
#         return result
#     return wrapper


# def print_info(func):
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper


# @print_more
# @print_info
# def add_num(a, b):
#     return a + b


# r = add_num(10, 20)
# print(r)

# print('start')
# r = add_num(10, 20)
# print('end')
# print(r)


# l = ['Mon', 'tue', 'Wed', 'Thi', 'fri', 'sat', 'Sun']


# def change_words(words, func):
#     for word in words:
#         print(func(word))


# def sample_func(word):
#     return word.capitalize()
# def sample_func(word): return word.capitalize()


# change_words(l, lambda word: word.capitalize())
# change_words(l, lambda word: word.lower())

# l = ['good morning', 'good afternoon', 'good night']

# for i in l:
#     print(i)

# print('##########')


# def counter(num=10):
#     for _ in range(num):
#         yield 'run'


# def greeting():
#     yield 'good morning'
#     yield 'good afternoon'
#     yield 'good night'


# for g in greeting():
# print(g)

# g = greeting()
# c = counter()
# print(next(c))
# print(next(g))
# print(next(g))

# t = (1, 2, 3, 4, 5)
# t2 = (5, 6, 7, 8, 9, 10)

# r = []

# for i in t:
#     if i % 2 == 0:
#         r.append(i)
# print(r)

# r = [i for i in t if i % 2 == 0]
# print(r)
# for i in t:
#     for j in t2:
#         r.append(i * j)

# print(r)

# r = [i * j for i in t for j in t2]
# print(r)

# w = ['Mon', 'Tue', 'Wed']
# f = ['coffee', 'milk', 'water']

# d = {}
# for x, y in zip(w, f):
#     d[x] = y

# print(d)

# d = {x: y for x, y in zip(w, f)}
# print(d)

# s = set()

# for i in range(10):
#     s.add(i)

# print(s)

# s = {i for i in range(10) if i % 2 == 0}
# print(s)

# def g():
#     for i in range(10):
#         yield i


# g = g()

# g = (i for i in range(10) if i % 2 == 0)

# for x in g:
#     print(x)


# animal = 'cat'


# def f():
#     global animal
#     animal = 'dog'
#     print('local', animal)


# f()
# print('global', animal)

# l = [1, 2, 3]
# i = 5

# try:
#     l[i]
# except IndexError as exc:
#     print('don\'t worrry: {}'.format(exc))
