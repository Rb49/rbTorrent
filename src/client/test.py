import requests

params = {
    "action": "login",
    "username": "admin",
    "token": "Y3liZXI=",
    "hash": "fba682d4aad8c0583aa454ef16c53fefc707889a"
}

res = requests.post("http://127.0.0.1:5555", json=params)
print(res.text)
