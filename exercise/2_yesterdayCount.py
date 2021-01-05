'''
yesterday.txt 파일을 읽어서
YESTERDAY 라는 단어가 몇번 나왔는지 yesterday_lyric.upper().count('YESTERDAY')
Yesterday 라는 단어가 몇번 나왔는지 yesterday_lyric.count('Yesterday')
yesterday 라는 단어가 몇번 나왔는지 yesterday_lyric.lower().count('yesterday')
'''

# mode -r(read), w(write), a(append), rb(read binary), wb(write binary)
# myFile = open('yesterday.txt', 'r')
# yesterday_lyric = myFile.read()
# myFile.close()



with open('yesterday.txt') as file:
    lyric = ''
    while 1:
        line = file.readline()
        if not line:
            break
        lyric = lyric + line.strip() + '\n'
print(lyric)

# file read 를 함수로 선언
def file_read(file_name):
    with open(file_name, 'r') as f:
        lyric = f.read()
        print(lyric)
    return lyric

# 함수 호출
yesterday_lyric = file_read('yesterday.txt')


a = yesterday_lyric.upper().count('YESTERDAY')
b = yesterday_lyric.count('Yesterday')
c = yesterday_lyric.count('yesterday')

print(a,b,c)


