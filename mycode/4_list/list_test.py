'''
list 타입을 선언하고 list에 eliment 추가, 삭제
'''

num_list = [60, 10, 30, 70, 80]
num_list2 = [1, 2, 3, 4, 5]
print(num_list == num_list2)
# 리스트의 메모리 저장 방식
print(num_list, num_list2)
num_list2 = num_list
print(num_list, num_list2)
num_list.sort()
print(num_list, num_list2)
num_list2 = [1, 2, 3, 4, 5]
num_list.sort()
print(num_list, num_list2)

print(type(num_list), num_list)
print(num_list[0], num_list[0:3], num_list[3:])
# enumerate -> index값 구할 때
for idx, num in enumerate(num_list):
    print(idx, num)

str_list = ['python', 'java', 'kotlin', 'c++', 'scalar']
print(type(str_list), str_list)
# index로 list의 엘리먼트 값을 변경
str_list[1] = 'javascript'
print(str_list[1], str_list[2:4])
# 엘리먼트 추가
str_list.append('Cobol')
str_list.insert(1, 'Typescript')
print(str_list)
print('----------------------')
# 엘리먼트 삭제
str_list.remove('Cobol')
del str_list[0]
del str_list[:3]
print(str_list * 2)
print('Scalar' in str_list)
print('java' in str_list)

for idx, val in enumerate(str_list):
    print(idx, val)

mix_list = [100, 3.14, True, '파이썬']
for mix in mix_list:
    print(type(mix), mix)
print('------------------------')

my_list = list('Python') # str -> list
print(type(my_list), my_list)

my_list2 = 'Hello, Python'.split(',') # str -> list
print(my_list2)

# packing 과 unpacking
# packing
my_list3 = ['aa', 'bb']
print(my_list3.index('bb'))
print(my_list3.index('aa'))

# unpacking(수가 일치해야함)
my_list4 = ['dd', 'ff']
my_list3.extend(my_list4)
print(my_list3)

str1, str2 = ['cc', 'dd']
print(str1)
print(str2)