import requests 

page = 1
hasNextPage = True 

while hasNextPage:
    endpoint = "http://localhost:8000/products/"
    params = {'page': page}
    data = requests.get(endpoint, params=params).json()
    print(data['next'])
    if not data['next']:
        hasNextPage = False
    page += 1