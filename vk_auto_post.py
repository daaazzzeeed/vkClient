from datetime import datetime
import vk

login = 'petumit@yandex.ru'
passw = 'Fsociety2019'
appId = '5580473'

vkAuthSession = vk.AuthSession(appId, login, passw, scope='wall,messages')
api = vk.API(vkAuthSession, v='5.46')

while 1:
    if(datetime.now().strftime('%Y-%m-%d %H:%M') == '2018-04-17 23:50'):
        api.messages.send(user_id=143772776, message='алалалалал')
        # api.messages.send(peer_id=2000000075, message='я первый к Готальской')
        break
