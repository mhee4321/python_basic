def add(x, y):
    return x + y

print(add(10, 20))

add2 = lambda x, y: x + y
print(add2(10,20))

print((lambda x, y: x + y)(10, 20))

print((lambda x: x ** 2)(10))



#map(함수, list)함수
double_val = lambda x: x ** 2
print(double_val(2))

my_list = [1, 2, 3, 4, 5]
# for loop 사용해서 함수호출
result_list = []
for val in my_list:
    # print(double_val(val))
    result_list.append(double_val(val))
print(result_list)

result = map(double_val, my_list)
print(type(result), result)

result = list(map(double_val, my_list))
print(result)

# my_list를 순회(iterate) 하면서 값을 제곱값을 반환하는 함수를 호출한다.
result = list(map(lambda x: x ** 2, my_list))
print(result)


# [1,2,3,4,5], [10,20,30,40,50] 두개의 리스트의 값을 더하기
# [11,22,33,44,55]
# lambda 함수와 map 함수 사용
add = lambda x, y : x + y
print(add(1,10))
my_list1 = [1,2,3,4,5]
my_list2 = [10,20,30,40,50]
result = list(map(add, my_list1, my_list2))
print(result)

result = list(map(lambda x, y : x + y, my_list1, my_list2))
print(result)

# 짝수만 제곱하는 함수
double_even = lambda x: x ** 2 if x % 2 == 0 else x
print(double_even(4), double_even(5))
print(list(map(double_even, my_list1)))
print(list(map(lambda x: x ** 2 if x % 2 == 0 else x, my_list1)))

# reduce함수
from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))