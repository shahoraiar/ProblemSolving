# proble : https://codeforces.com/problemset/problem/71/A

num = int(input())
num1 = []
for _ in  range(num) : 
    value = input()
    num1.append(value)



for word in num1 : 
    if len(word) > 10 : 
        result = word[0] + str(len(word) - 2) + word[-1]
        print(result)
    else : 
        print(word)
    





    
 

