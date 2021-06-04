import requests
import random
import string

amount = int(input("Amount To Generate: "))

for i in range(amount):
    randomNumbers = random.randint(1, 999999)
    randomLetters = ('').join(random.choices(
        string.ascii_letters, k=25))
    bypass = requests.Session()
    generatePayload = {
        "nickname": f"fake{randomNumbers}"
    }
    header = {
        # random alternative link to get the cookies
        "referer": f"https://tlk.io/{randomLetters}"
    }
    generate = bypass.post("https://tlk.io/api/participant",
                           data=generatePayload, headers=header)
    print(f"Generated Cookie: {i}")
    f = open("cookies.txt", "a")
    info = generate.json()
    for cookie in generate.cookies:
        f.write(f"""
Cookie: _tlkio_session={cookie.value}
Token: {info['token']}
Name: fake{randomNumbers}
""")
    f.close()
