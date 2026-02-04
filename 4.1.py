import requests

#Налаштування API
url = "https://youtube138.p.rapidapi.com/videos/search/"
headers = {
    "X-RapidAPI-Key": "2e8c2e29bbmsha7a8798072beaf9p1c7a32jsne02584c2918c",
    "X-RapidAPI-Host": "youtube138.p.rapidapi.com"
}

#GET-запит
params = {"q": "Python programming", "hl": "en", "gl": "US"}
response_get = requests.get(url, headers=headers, params=params)

print("=== GET-запит ===")
print("Статус-код:", response_get.status_code)
print("Заголовки:", response_get.headers)
print("Тіло відповіді:", response_get.json())

#POST-запит
post_url = "https://youtube138.p.rapidapi.com/some-post-endpoint"
post_data = {
    "example_field": "example_value"
}

response_post = requests.post(post_url, headers=headers, json=post_data)

print("\n=== POST-запит ===")
print("Статус-код:", response_post.status_code)
print("Заголовки:", response_post.headers)
print("Тіло відповіді:", response_post.json())
