import requests

base_url = 'http://localhost:8002'

def get_api(api, id):
    r = requests.get(f'{base_url}/{api}/{id}')
    return r.status_code, r.json()

def post_api(api, data):
    r = requests.post(f'{base_url}/{api}/', json=data)
    return r.status_code, r.json()

def put_api(api, id, data):
    r = requests.put(f'{base_url}/{api}/{id}', json=data)
    return r.status_code, r.json()

def delete_api(api, id):
    r = requests.delete(f'{base_url}/{api}/{id}')
    return r.status_code, r.json()
