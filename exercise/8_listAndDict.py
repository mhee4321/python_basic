a = {'id':1, 'name':'hong kildong', 'email':'hong@mail.com', 'hp_num':'010-2343-9870'}
b = {'id':2, 'name':'lee soonsin', 'email':'lee@mail.com', 'hp_num':'010-3333-5555'}
c = {'id':3, 'name':'jang youngsil', 'email':'jang@mail.com', 'hp_num':'010-7777-1234'}
d = {'id':4, 'name':'king sejong', 'email':'king@mail.com', 'hp_num':'010-4567-0987'}

my_list = []
my_list.append(a)
my_list.append(b)
my_list.append(c)
my_list.append(d)
print(my_list)

for person in my_list:
    for k,v in person.items():
        print(f'{k} : {v}')



# users = [{'id':1,'name':'홍길동','email':'hong@mail.com','hp_num':'010-2343-1234'},
#          {'id': 2, 'name': '이순신', 'email': 'lee@mail.com', 'hp_num': '010-3333-5555'}]
# #users[0] = {'id':1,'name':'hong kildong','email':'hong@mail.com','hp_num':'010-2343-1234'}
#
# users.append({'id': 3, 'name': '장영실', 'email': 'jang@mail.com3', 'hp_num': '010-7777-1233'})
# users.append({'id': 4, 'name': '세종대왕', 'email': 'sejong@mail.com3', 'hp_num': '010-4567-1233'})
# print(users)
#
# for user in users:
#     for key in user.keys():
#         print('{} = {} '.format(key, user[key]))
#
# print('items() 사용 ---------------------------------')
# for user in users:
#     for key, value in user.items() :
#         print(f'{key} = {value}')
