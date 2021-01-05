'''
나이 = 현재년도 - 태어난 년도 +1
태어난 년도를 입력 받음 input()

from 모듈명 import
'''
from datetime import datetime as dt

print('태어난 년도를 입력해주세요.')
a = int(input())
# 현재 년도 datetime 클래스에 선언된 today() 메서드를 호출
age = dt.today().year - a + 1
if 17 <= age < 20:
    print('고등학생입니다.')
elif 20 <= age < 27:
    print('대학생입니다.')
else:
    print('학생이 아닙니다.')