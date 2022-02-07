import vk
import datetime

session1 = vk.AuthSession(access_token='70acd10414f653843135537940fd19626c8f92c7797772f627a78b028fa434d7b5e65e5a5f5c07d5f0743')
vk_api = vk.API(session1, v=5.131)
def get_user_status():

    value = vk_api.users.get(user_ids='173396899', fields='last_seen')
    #print(value)  # <- получаешь данные вида [{'id': айди, 'first_name': 'Имя', 'last_name': 'Фамилия', 'last_seen': {'time': 1560796737, 'platform': 7}}]
    for i in range(len(value)):
        time = datetime.datetime.fromtimestamp(value[i]['last_seen']['time'])
        print('{} {} заходил(а) в VK: {}'.format(value[i]['first_name'], value[i]['last_name'], time))

get_user_status()
