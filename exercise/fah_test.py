# 1. import 모듈명
# import exercise.fahrenheit
# 2. import 모듈명 as alias
# import exercise.fahrenheit as fah
# 3.from 모듈명 import 함수명
# from exercise.fahrenheit import transfer
# 4.from 모듈명 import *
from exercise.fahrenheit import *

print('변환하고 싶은 섭씨 온도를 입력해 주세요:')
n = float(input())

# 2번 모듈을 import한 경우
# answer = fah.transfer(n)

answer = transfer(n)
print('화씨 온도는', '%0.2f' % answer , '입니다.')
print(sayHello('파이썬'))