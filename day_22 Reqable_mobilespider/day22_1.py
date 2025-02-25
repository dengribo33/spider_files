import requests

url = "https://himg.baidu.com/sys/portrait/item/tb.1.1033cc2a.buE3rBWx9JA5Qin9KqgYiw"

params = {
  't': "1705666503"
}

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 12; SM-S9210 Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Safari/537.36Mozilla/5.0 (Linux; Android 12; SM-S9210 Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Safari/537.36 tieba/12.72.1.1 (Linux; Android 12; SM-S9210 Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Safari/537.36Mozilla/5.0 (Linux; Android 12; SM-S9210 Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Safari/537.36 tieba/12.72.1.1 skin/default",
  'Accept': "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
  'Accept-Encoding': "gzip, deflate",
  'X-Requested-With': "com.baidu.tieba",
  'Sec-Fetch-Site': "same-site",
  'Sec-Fetch-Mode': "no-cors",
  'Sec-Fetch-Dest': "image",
  'Referer': "https://tieba.baidu.com/",
  'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
  'Cookie': "CUID=4A9B07AE9E2848D6C8368B344786314E|VX73W2STR; BAIDUCUID=gi-oagu0Saj_82fS_PHi80Oz2iYwi28Kga-D8ga_vu8M9L8pg9vwRHWmA; TBBRAND=; need_cookie_decrypt=1; DNARBBT=pfs9RYuA2iHjC; BAIDUZID=597wp3Jnkt6_ncdJ4hl1eyYHzh8_f891wyxak0dLhGFxuDCf5Nn74938abvcY1niSEcoqFK1Tpr8kEPkDkga0jA; cuid_galaxy2=4A9B07AE9E2848D6C8368B344786314E|VX73W2STR; cuid_gid=; BDUSS=null; BDUSS_BFESS=null; RT=\"z=1&dm=baidu.com&si=a921386e-8212-4356-b3cb-57bc333d428b&ss=m3d19o43&sl=4&tt=c9j&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=dci\"; BAIDUID=56EFD165CCE2FD8699D956B2F6D748D4:FG=1; BAIDUID_BFESS=56EFD165CCE2FD8699D956B2F6D748D4:FG=1"
}

response = requests.get(url, params=params, headers=headers)

with open("美食.jpg", "wb") as f:
    f.write(response.content)