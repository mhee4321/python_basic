# 일반적인 for + append
result = []
for val in range(10):
    if val % 2 == 0:
        result.append(val)
print(result)

# List Comprehensions
result2 = [val for val in range(10) if val % 2 == 0]
print(result2)

my_str1 = "Hello"
my_str2 = "World"

result = [i+j for i in my_str1 for j in my_str2 if not (i == j)]
print(result)

# 2차원 배열 만들기
words = 'Requiring an active virtual environment for pip'.split()
print(words)

my_list = [[w.upper(), w.lower(), w.title(), len(w)] for w in words]
print(type(my_list), my_list)
for word in my_list:
    print(word)



# enumerate 함수 - for loop 를 dict에 저장
for idx, w in enumerate(words):
    print(idx, w)

print(enumerate(words), type(enumerate(words)))
print(list(enumerate(words)))

word_dict = {idx: w for idx, w in enumerate(words, 1)}
print(word_dict)

# zip 함수
my_list1 = [1, 2, 3]
my_list2 = [10, 20, 30]
my_list3 = [100, 200, 300]
print(zip(my_list1, my_list2, my_list3), type(zip(my_list1, my_list2, my_list3)))
print(list(zip(my_list1, my_list2, my_list3)))

for val in zip(my_list1, my_list2, my_list3):
    print(type(val), val, sum(val))

result = [sum(val) for val in zip(my_list1, my_list2, my_list3)]
print(result)

result_dict = {idx: sum(val) for idx, val in enumerate(zip(my_list1, my_list2, my_list3)) }
print(result_dict)

a, b, c = zip(my_list1, my_list2, my_list3)
print(a)
print(b)
print(c)
