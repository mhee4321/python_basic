import requests


def translyric_savefile(trans_list, title):
    with open(f'data/{title}_trans.txt', 'w', encoding='utf8') as file:
        file.writelines(trans_list)


# yesterday.txt 가사 파일의 내용을 읽어서 list에 저장
def gettext_savelist(title):
    file_name = f'data/{title}.txt'
    lyric_list = []
    with open(file_name, 'r', encoding='utf8') as file:
        contents = file.read()
        lyric_list = contents.split('\n')
    return lyric_list


def main(title, source, target):
    client_id = "y_8ZbXuSCA2hOCL42m6r"
    client_secret = "Zwm47Ofq71"

    url = "https://openapi.naver.com/v1/papago/n2mt"

    # request header 값 선언
    req_header = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }
    # yesterday.txt 가사 파일의 내용을 읽어서 list에 저장
    lyric_list = gettext_savelist(title)
    print(len(lyric_list))
    # list comprehension
    lyric_list = [lyric for lyric in lyric_list if len(lyric) != 0]
    print(len(lyric_list))

    trans_list = []
    print('>> 번역시작')
    for req_lyric in lyric_list:
        print(req_lyric)
        # request form data 값 선언
        req_data = {
            "source": source,
            "target": target,
            "text": req_lyric
        }
        # papago 서비스 요청, post() 함수 호출
        res = requests.post(url, data=req_data, headers=req_header)

        try:
            trans_lyric = res.json()['message']['result']['translatedText']
        except Exception as exp:
            print(exp)
            print(res.status_code)
        else:
            print(trans_lyric)

        trans_list.append(req_lyric + '\n')
        trans_list.append(trans_lyric + '\n')
        # print(trans_list)

    translyric_savefile(trans_list, title)
    print('>> 번역 종료')


main('shallow', 'en', 'ko')