# Скрипт номер один
from itertools import count

start = 3
stop = 10

for num in count(start):
    print(num)
    if num == stop:
        break
# Скрипт номер два
from itertools import cycle

lst = [1, 2, 3, 4]
num_iterations = 3

for i, elem in enumerate(cycle(lst)):
    print(elem)
    if i == num_iterations * len(lst) - 1:
        break