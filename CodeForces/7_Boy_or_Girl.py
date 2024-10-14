str_input = input()

# print(len(str_input))

dist_str = ""

for char in str_input : 
    if char not in dist_str:
        dist_str += char
        
# print('dist_str : ', dist_str)
# print(len(dist_str))

length = len(dist_str)
if length%2 == 0 :
    print('CHAT WITH HER!')
else : 
    print('IGNORE HIM!')
