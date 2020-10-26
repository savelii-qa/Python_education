from random import randint
#import statistics

import numpy as np

array = [randint(-1000, 1000) for x in range(1000)]
avg = int(np.mean(array))
dif = (avg/100)*20
a = int(avg - dif)
b = int(avg + dif)
print('Values from', a)
print('Values to', b)
print('Average value', avg)
array2 = []
for i in array:
    if a < i < b:
        array2.append(i)
print('First array', array)
print('Array +-20%', array2)
max1 = max(array)
max2 = []
for i in array:
    if i not in max2 and i != max1:
        max2.append(i)
max2 = max(max2)
assert max1 != max2, "Attention - max values identical"
print('Max_1 =', max1)
print('Max_2 =', max2)