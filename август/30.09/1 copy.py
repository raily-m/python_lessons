import requests #библиотека http запроса

url = "https://www.google.com/search"

params = {
    "q":"Что покушать на ужин"
}

headers = {

    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
}

response = requests.get(url, params, headers = headers)

print(f"Код ответа: {response.status_code}")


# print(f"Заголовки: ")
# for key, value in response.headers.items():
#     print(f"{key}:{value}")


# print(f"Тело страницы: {response.content}")

print(f"Тело страницы: {response.text}")

with open("google.html", "w", encoding = "utf-8") as fl:
    fl.write(response.text)
