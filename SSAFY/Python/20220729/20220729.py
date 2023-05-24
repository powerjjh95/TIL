import requests

# 방법 1
# res = requests.get('https://api.agify.io?name=beomkyu')
# # print(type(res.text)) # {"name":"beomkyu","age":36,"count":2}

# data = res.json()
# print(data, type(data)) # {'name': 'beomkyu', 'age': 36, 'count': 2} <class 'dict'>
# print(data.get('name')) # beomkyu

base_url = 'https://api.agify.io/'
params = {
    'name' : 'beomkyu'
}
res = requests.get(base_url, params = params)
data = res.json()
# print(data, type(data)) # {'name': 'beomkyu', 'age': 36, 'count': 2} <class 'dict'>

base_url = 'https://api.agify.io/'
for name in ['alex', 'kyle']:
    params = {
        'name' : name
    }
    res = requests.get(base_url, params = params)
    data = res.json()
    print(data, type(data)) # {'name': 'beomkyu', 'age': 36, 'count': 2} <class 'dict'>