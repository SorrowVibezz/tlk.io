import requests
import string
import random

count = 0

roomCode = input("Room Code: ")
ID = input("Enter Chat ID: ")
msg = input("Enter what message to be sent: ")
amount = int(input("How many bots should join: "))

for i in range(amount):
    bypass = requests.Session()
    randomLetters = ('').join(random.choices(
        string.ascii_letters + string.digits, k=5))
    joinPayload = {
        "nickname": f"raid_{randomLetters}"
    }
    header = {
        "referer": f"https://tlk.io/{roomCode}"
    }
    messagePayload = {
        "body": f"{msg}",
        'expired': 'false'
    }
    joinRequest = bypass.post(
        "https://tlk.io/api/participant", data=joinPayload, headers=header)
    messageRequest = bypass.post(
        f"https://tlk.io/api/chats/{ID}/messages", data=messagePayload, headers=header)

    count += 1
    # print(messageRequest.content)
    print(f"Sent Bots: {count}{amount}")
