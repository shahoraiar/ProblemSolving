# https://codeforces.com/problemset/problem/339/A
# → Problem tags : greedy, implementation, sortings, strings*800

# input_str  = input()
# # print('string : ', input_str)

# strip = input_str.split('+')
# # print('after strip : ', strip)

# int_str = list(map(int, strip))
# print('int list : ', int_str)

# # int_str = [int(x) for x in strip]
# # print('int : ', int_str)

# int_str.sort()

# # print('sort : ', int_str)

# str_int = list(map(str, int_str))
# # str_int = [str(x) for x in int_str]

# result_str = '+'.join(str_int)
# # print('result : ', result_str)
# print(result_str)

# -------------2nd approach---------------
def rearrange_sum(s):
    numbers = s.split('+')
    print('after split : ', numbers)
    numbers.sort()
    print('after sort : ', numbers)
    return '+'.join(numbers)

s = input()
print('type s : ', type(s))
print(rearrange_sum(s))
fun_type = rearrange_sum(s)
print('type fun : ', type(fun_type))





