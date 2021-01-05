'''
문자열 관련 내용들
'''
# escape 문자
greet = 'Hello' *4+ '\n'
end = '\tGood \'Bye\' !!'
end2 = "\t Good 'Morning' !!"
print(greet + end + end2)

# bool 타입과 str 타입
is_flag = False
my_str = 'True'
print(type(is_flag), type(my_str))
if not is_flag:
    print(my_str)

# 문자열 인덱스(오프셋)
greeting = 'hello world'
print('문자열 길이 {}, 0번째 인덱스 값은 {}'.format(len(greeting), greeting[0]))
print('0번째 인덱스 값은 {1}, 문자열 길이 {0}'.format(len(greeting), greeting[0]))
# c언어 스타일
print('파이썬 %s' % greeting)
print('문자열 길이 %i' % len(greeting))
# 3.6 버전이후
print(f'문자열 길이 {len(greeting)}, 1번째 인덱스 값은 {greeting[1]}')

# 문자열 인덱스 슬라이싱
print(f'greeting[0:5] =  {greeting[0:5]}')
print(f'greeting[6:11] = {greeting[6:11]}')
print(f'greeting[6:] = {greeting[6:]}')
print(f'greeting[:5] = {greeting[:5]}')
print(greeting[::2])


# 음수값의 인덱스
print(f'greeting[-1:] = {greeting[-1:]}')
print(f'greeting[-2:] = {greeting[-2:]}')
# 문자열이 역순으로 바뀐
print(f'greeting[::-1] = {greeting[::-1]}')

# 문자열 여러가지 함수들
word = 'Good manufacturing Practice Good'
print(f'대문자로 변환 = {word.upper()}')
result = word.upper()
print(word, '  ', result)
print(f'소문자로 변환 = {word.lower()}')
print(word.title())
print(word.find('G'))
print(word.rfind('G'))
print(word.count('G'))
# 공백을 기준으로 배열로 나눠줌
word_list = word.split()
print(word_list, type(word_list))
word2 = 'Good/manufacturing/Practice/Good'
print(word2.split('/'))
# strip => 공백제거
word3 = ' hello python '
print(len(word3), len(word3.strip()), word3.strip())
print(len(word3.rstrip()), word3.rstrip())

print(word.startswith('G'))
print(word.endswith('G'))

for val in word:
    print(val, word.count(val))

print(word_list)
for w in word_list:
    print(w)