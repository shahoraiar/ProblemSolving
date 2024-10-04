# proble : https://codeforces.com/problemset/problem/282/A
# start from count= 0 || if x++ or ++x then count increase || else decrease

n = int(input())

count = 0
for i in range(n):
    operation = input()
    if operation == 'X++' or operation == '++X':
        count+=1
    else : 
        count -= 1

print(count)