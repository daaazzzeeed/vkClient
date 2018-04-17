from datetime import datetime #for time comparison
import vk #to send messages

#define login, password and unique app_id
login = 'your_email@yandex.ru'
passw = 'Pass2019'
appId = 'yor_app_id'

#open auth session
vkAuthSession = vk.AuthSession(appId, login, passw, scope='wall,messages')
#form api object you will always call 
api = vk.API(vkAuthSession, v='5.46')

#define a simple loop
while 1:
    #compare current and specified time
    if(datetime.now().strftime('%Y-%m-%d %H:%M') == '2018-04-17 23:50'):
        #send messages
        api.messages.send(user_id=143772776, message='test message') #send to a user
        api.messages.send(peer_id=2000000075, message='test message for a group chat') #send to a group chat
        break #break infinite loop
