import requests

url = input()
port = int(input())
a = int(input())
b = int(input())

response = requests.get(f"{url}:{port}", params={"a": a, "b": b})
print(*sorted(response.json()["result"]))
print(response.json()["check"])
