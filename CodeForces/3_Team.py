# problem : https://codeforces.com/problemset/problem/231/A 

num = int(input())

l = []
for _ in range(num) :
    row_value = list(map(int, input().split()))
    l.append(row_value)

count = 0

for row in l:
    print('row : ', row)
    sum_row = sum(row)
    if sum_row > 1 : 
        count+=1

print(count) 

