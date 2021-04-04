# s = """\
# AAA
# BBB
# CCC
# DDD
# """
# with open('test.txt', 'w') as f:
#     f.write(s)


# with open('test.txt', 'r') as f:
# print(f.read())
# while True:
#     chunk = 2
#     line = f.readline(chunk)
#     print(line)
#     if not line:
#         break
# print(f.tell())
# print(f.read(1))
# f.seek(5)
# print(f.read(1))

# with open('test.txt', 'r+') as f:
#     f.write(s)

#     print(f.read())

# import string

# with open('design/email_template.txt') as f:
#     t = string.Template(f.read())

# contents = t.substitute(name='Mike', contents='How are you?')
# print(contents)


# import csv

# with open('test.csv', 'w') as csv_file:
#     fieldnames = ['Name', 'Count']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'Name': 'A', 'Count': 1})
#     writer.writerow({'Name': 'B', 'Count': 2})

# with open('test.csv', 'r') as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         print(row['Name'], row['Count'])

# import os
# import pathlib
# import glob
# import shutil

# print(os.path.exists('test.txt'))
# print(os.path.isfile('test.txt'))
# print(os.path.isdir('test.txt'))

# os.rename('test.txt', 'renamed.txt')
# os.symlink('renamed.txt', 'symlink.txt')

# os.mkdir('test_dir')
# os.rmdir('test_dir')

# pathlib.Path('empty.txt').touch()
# os.remove('empty.txt')

# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# print(os.listdir('test_dir'))
# pathlib.Path('test_dir/test_dir2/empty.txt').touch()
# shutil.copy('test_dir/test_dir2/empty.txt', 'test_dir/test_dir2/empty2.txt')
# print(glob.glob('test_dir/test_dir2/*'))
# shutil.rmtree('test_dir')
# print(os.getcwd())

# import tarfile

# with tarfile.open('test.tar.gz', 'w:gz') as tr:
#     tr.add('test_dir')


# with tarfile.open('test.tar.gz', 'r:gz') as tr:
#     # tr.extractall(path='test_tar')
#     with tr.extractfile('test_dir/sub_dir/sub.txt') as f:
#         print(f.read())

# import glob
# import zipfile

# with zipfile.ZipFile('test.zip', 'w') as z:
#     # z.write('test_dir')
#     # z.write('test_dir/test.txt')
#     for f in glob.glob('test_dir/**', recursive=True):
#         print(f)
#         z.write(f)

# with zipfile.ZipFile('test.zip', 'r') as z:
#     # z.extractall('zzz2')
#     with z.open('test_dir/test.txt') as f:
#         print(f.read())

# import tempfile

# with tempfile.TemporaryFile(mode='w+') as t:
#     t.write('hello')
#     t.seek(0)
#     print(t.read())

# with tempfile.NamedTemporaryFile(delete=False) as t:
#     print(t.name)
#     with open(t.name, 'w+') as f:
#         f.write('test\n')
#         f.seek(0)
#         print(f.read())

# with tempfile.TemporaryDirectory() as td:
#     print(td)

# temp_dir = tempfile.mkdtemp()
# print(temp_dir)


# import subprocess

# subprocess.run(['ls', '-al'])
# subprocess.run('ls -al | grep test', shell=True)

# import shutil
# import os
# import time
# import datetime

# now = datetime.datetime.now()
# print(now)
# print(now.isoformat())
# print(now.strftime('%d/%m/%y-%H%M%S'))

# today = datetime.date.today()
# print(today)
# print(today.isoformat())

# t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
# print(t)
# print(t.strftime('%d/%m/%y-%H%M%S'))

# print(now)
# d = datetime.timedelta(weeks=1)
# print(now + d)

# # print('###')
# # time.sleep(2)
# # print('###')


# file_name = 'test.txt'

# if os.path.exists(file_name):
#     shutil.copy(file_name, "{}.{}".format(
#         file_name, now.strftime('%Y_%m_%d_%H_%M_%S')))

# with open(file_name, 'w') as f:
#     f.write('test')
