import vk
import config
import json

passw = config.vkPassw
login = config.vkLogin
appId = config.appId
myId = config.myId

vkAuthSession = vk.AuthSession(appId, login, passw, scope='wall, messages')
api = vk.API(vkAuthSession, v='5.69')


def parseJson(json_string, field1, field2):
    try:
        parsed_string = json.loads(json_string)
        substring = str(parsed_string[field1]).replace('[', '')
        substring = substring.replace(']', '')
        substring = substring.replace("'", '"')
        json_dict = json.loads(substring)
        return str(json_dict[field2])
    except (json.JSONDecodeError, TypeError):
        print('Error occurred')


def getFriends():
    resp3 = api.friends.get(user_id=myId, order='name', count='1000', offset='0', fields='name', name_case='nom')
    usersJsonList = resp3['items']
    config.count = 0
    for item in usersJsonList:
        name = str(item['first_name']) + ' ' + str(item['last_name'])
        user_id = str(item['id'])
        config.count += 1
        config.friends_dict.update({name: user_id})


def get_users(user_id):
    return api.users.get(user_ids=user_id)

getFriends()
print('q чтобы выйти\ng получить последнее сообщение\nm отправить сообщение\nf список друзей' )

while 1:
    try:
        req = input()
        if req == 'q':
            break
        elif req == 'g':
            resp = api.messages.get(count='1')
            resp = str(resp).replace("'", '"')
            us_id = parseJson(resp, 'items', 'user_id')
            resp2 = get_users(us_id)
            resp2 = str(resp2).replace("'", '"')
            resp2 = resp2.replace('[','')
            resp2 = resp2.replace(']','')
            resp2 = json.loads(resp2)
            print('Сообщение : ' + parseJson(resp, 'items', 'body') + ' от : ' + resp2['first_name'] + ' ' + resp2['last_name'])
        elif req == 'm':
            print('введите текст : ')
            text_msg = input()
            print('введите имя пользователя')
            name_user = input()
            print('Сообщение ' + '[' + text_msg + '] будет отправлено ' + '[' + name_user + ']')
            print('Отправить? y/n')
            decision = input()
            if decision == 'y':
                userId = config.friends_dict.get(name_user)
                api.messages.send(user_id=userId, message=text_msg)
                print('Отправлено')
            elif decision == 'n':
                print('Сообщение не будет отправлено')
        elif req == 'f':
            for item in config.friends_dict:
                print(item)
            print('Количество друзей : ' + str(config.count))

    except KeyboardInterrupt:
        print('input interrupted')
        break
