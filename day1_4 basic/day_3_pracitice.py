import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

keyword = input("请输入搜索关键词：")

url = "https://www.so.com/s"
params = {
    "ie": "utf-8",
    "fr": "360sou_newhome",
    "src": "home-sug-store",
    "ssid": "",
    "sp": "ad0",
    "cp": "05800007ad",
    "nlpv": "placeholder_test_zc_61",
    "q": keyword,
}

response = requests.get(url, headers=headers, params=params)

with open(f"360-{keyword}.html", "w", encoding="utf-8") as f:
    f.write(response.text)