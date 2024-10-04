# problem : https://codeforces.com/problemset/problem/1/A 

# 8 x 8 and flagstone a = 4 x 4 
# length 8/4 = 2 || width 8/4 = 2
# print(2 x 2)

import math
n, m, a = map(int, input().split())

length = math.ceil(n/a)
width = math.ceil(m/a)

print(length * width)