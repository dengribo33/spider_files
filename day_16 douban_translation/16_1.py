import requests
from jsonpath import jsonpath
import execjs

keyword = input("请输入要翻译的单词：")
# 调用js文件
with open('js_code.js', 'r', encoding='utf-8') as f:
    js = f.read()
js_obj = execjs.compile(js)
sign = js_obj.call('func', keyword)

headers = {
    'acs-token': '1730106420297_1730119679071_KS/vJLH5eo7MTN2TzLu4qv/gDH95zeBzCZc4YX1JemoAsZoFK/wJ6egIG9KHPR5AMU192GJ+CwAVDw5RnCXGA33YHcfOfOQG7g7pwU7eMqiwcR7mKpqFq53E6FXYoCgBRirfNzi8KtHP8Vc2HPFnsZeqc94tWJUGYGahWSL2jhXvV40kZx/jwy0JEjJ5TAo8KcPBIJy2d/CCp4MjiWsKtUaMQtMTLP5Yhpi4+1w/QIe9AZ9UTWDPchkiCfpYnK68OomJB55DWw0JUZcivuNNAGs2H76Zj9chLhwfHx3ACzmSFBa33M1gIefGp3K39Upm6sfxLUekgwzbZoloXoSrYcC2sNCgJucVxdYlTBovaAYSYEJjcv8GcNzfp+FZp6Sk4WN1tt3t8ehPA84V2rgMzN6Ian0quiZb7lzdXrMpCdUK+rKx4P4L5Wl7HHmt37y8jUMrVu9mZgkxBqfPtfFBgKl048EIBwZODfYmyhoVte0=',
    'Cookie': 'BIDUPSID=E93124C435FBAA2029436C95B3EB6118; PSTM=1726235422; BAIDUID=E93124C435FBAA20EC258CF5137FD07A:FG=1; BAIDUID_BFESS=E93124C435FBAA20EC258CF5137FD07A:FG=1; BA_HECTOR=2hah8h2l0haha1a12g0h2lah0dibnj1jhun9m1v; ZFY=eZgLAu2qrzxDWVcXO3Eye73UA5rs4cn9:BtRbsQ9PbfE:C; H_PS_PSSID=60854_60897_60951_61008; BDUSS=0JhUH5hVHRZYktiVmE0cXhJTkNRUVEyRzRrT1NIOWdYWGNiYkdkSm11ajhBa2RuSVFBQUFBJCQAAAAAABAAAAEAAADQDiv7us2wqrXEZGVuZ3JpYm8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPx1H2f8dR9nZ; BDUSS_BFESS=0JhUH5hVHRZYktiVmE0cXhJTkNRUVEyRzRrT1NIOWdYWGNiYkdkSm11ajhBa2RuSVFBQUFBJCQAAAAAABAAAAEAAADQDiv7us2wqrXEZGVuZ3JpYm8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPx1H2f8dR9nZ; RT="z=1&dm=baidu.com&si=2709d522-d2bd-4729-bf16-18fcab57af0b&ss=m2sxvmnm&sl=8&tt=cal&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=4v5d"; smallFlowVersion=old; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1730115369; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1730115369; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_ODg2M2IzOWYwMDIzYjI0YTg4MmQzNzc1MjQwNDVlMWNmZGJiYmQ5MzkzM2UzOWU0YWExMTFiYzYwZjUxMTk0YTFiMjU1NjFhYzkzNWE2NzhmZjUyZWFjNjU4Zjc0MTkxY2RlNzA5NzEzZmMyZTk0NWNkM2U1M2Y3MGNkODJmODUwYjdiMjVkMDdhNThmNjAyYzM5Yzc3YzA0ZDU2ZDU3NDgwZTgwMTMwYjYxNGY3YmU0ZmIxYTFhNGNkZTI0Zjgy',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'


form_data = {
    "from": "auto",
    "to": "auto",
    "query": keyword,
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": sign,
    "token": "e101dc50aa19011a98bd35eb55da1f34",
    "domain": "common",
    "ts": "1730115537105"
}

response = requests.post(url, headers=headers, data=form_data)
# print(response.json())

json_data = response.json()

data = jsonpath(json_data, '$..dst')
print(data)





