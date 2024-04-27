import math
import random

def rnd():
    return random.random()

i = 0
k = 0
while i < 10000:
    i += 1
    x = rnd()
    y = rnd()

    if math.sqrt(x**2 + y**2) < 1:
        k += 1

print(k*4/10000)


res = 0
for i in range(100, 1000):
    if len(str(i)) == 3:
        res += 1
print(res)


n = 0
l = 1
while n > 0:
    l *= n
    n = n - 1
print(l)
