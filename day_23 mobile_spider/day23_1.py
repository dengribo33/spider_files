import requests
from jsonpath import jsonpath

headers = {
  'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 12; SM-S9210 Build/e3c1804.0) automobile/8.3.1 tt-ok/3.12.13.4-tiktok",
  'Accept-Encoding': "gzip",
  'x-vc-bdturing-sdk-version': "3.7.2.cn",
  'sdk-version': "2",
  'passport-sdk-version': "50557",
  'x-ladon': "ZzRZUw==",
  'x-khronos': "1731483987",
  'x-argus': "U1k0Zw==",
  'x-gorgon': "8404d0ca0000259b6f4c737afa053cf1730d4d4c7161a0742164",
  'x-helios': "Ns9Heun6E2A8GsjEuiTiWUiPQT/QMLp9duq3B75aA8BcQprt",
  'x-medusa': "UFk0Z6Sxa52EjuhchXP8FwSWVX9BPAABP4V5jagRAxoMGFvDGlebnA6d/szvZ93JXMafPNG8f7+fLO1q/EAsV6skHYTbJ6m5QNpkVXefR7gl3XD2nY/nWHzKF+8CbAJL6q+aOMFNL0w6m4dpyDfzRopoqizcCWy1ZttMskreu0OM/ZidRZNSq1BfnyvBSTOwvyTwuyOyWLUaMpHR8xd0OM+gXwWCt+WvNGFaySeCJxqzXX7bNrZLeohWBfE30zwH3xiNt0YXTYdVCT/gRt+V58Lx2K74n2uj+LlqkMsAvaMbwO8y0+fjThVhRfQTPHZaEmk4MjBwZxqUu1kPJEIj6bEPQ7bmM56R9UguF3181sTQFHPN/2rXn4v7rfHdUkVX6a2P7u3bQXQWUnjovEDDnO3bOf/cOiXFOFUoWjNqZ5dygpYfKWMHsWjEWDbSgJITkHo4tsyiCszscDrboRteF8K2mJBEvj8d+J+kHKlgOQ/E5BH63Plfv0a7Cz0RFUw1dQ8Xss0OGh2SUnjNcpqSfjiLfZXO2HS5A7b8Tn9PGmGW/mGJIeT1/OFCETNLAFuI1O/KigMr80EXFtcxyehKReaV9LnwgFxN0DQPAQDFxSjjwE176ZUOV8nxTg5ksEnQnAZ4V5giZ0772ux8rS/f5Sp4tQBCOGMMY3iykHTmwPBLY48Q3wrRSIZ7+AYSf3DhW8Bm9G25hsRM1xm7Ljh+X6s7FdHCV1tdFCNmZgiubZX+oYiANW/ryq76stVJgNyE/iyQq7tWc0t6W0EF6MTGGAh6W/CtwZ1oR3v3PWTjTzMA+UIRgACq3TQg74KhFjP9gstNq3IBYLppBqA11D4xNc+maqSkrNFEBSYPqd28TsWBif4qpN4uhSEtZSJVQVX4hKDJWYj6JLzi6jWX+5WXkgAMNGe+7bR+VKlv8eQzKe9CqWw6JZLjH56OhMIgNvKegIr//5+K//+fDHk=",
  'Cookie': "install_id=2936122409227920; ttreq=1$6429a98198316ac12883237d77a010ebd14a5921; passport_csrf_token=ca849441f4b705724bb452219817a696; passport_csrf_token_default=ca849441f4b705724bb452219817a696; odin_tt=c69595b20918b105054ad22201611414992f2ce755344ca32ebd6fef7baa36bfa4da3dd7d9acbf0e7bafdfcef8fec6e0fc2007d329f11f8166d85e9d11b2126b66c6439388d9afbb064f989f7561ea1f"
}
url = "https://api5-normal-sinfonlinea.dcarapi.com/motor/car_page/v6/rank_data"

params = {
  '__method': "jsb.app.fetch",
  'rank_data_type': "11",
  'month': "202410",
  'energy_type': "",
  'price': "0,-1",
  'manufacturer': "",
  'rank_city_name': "全国",
  'market_time': "0",
  'offset': "0",
  'count': "50",
  'scm_version': "1.0.0.2097",
  'is_from_jsb': "1",
  'device_platform': "android",
  'os': "android",
  'ssmix': "a",
  '_rticket': "1731483990238",
  'cdid': "48d56d57-4767-4bcc-b6d5-312cb68ac1b2",
  'channel': "vivo_36_64",
  'aid': "36",
  'app_name': "automobile",
  'version_code': "831",
  'version_name': "8.3.1",
  'manifest_version_code': "831",
  'update_version_code': "8313",
  'ab_client': "a1,c2,e1,f2,g2,f7",
  'ab_group': "3167592,3577237",
  'resolution': "1080*1920",
  'dpi': "280",
  'device_type': "SM-S9210",
  'device_brand': "Samsung",
  'language': "zh",
  'os_api': "32",
  'os_version': "12",
  'ac': "wifi",
  'iid': "2936122409227920",
  'device_id': "2936122409223824",
  'city_name': "广州",
  'gps_city_name': "广州",
  'selected_city_name': "",
  'district_name': "白云",
  'gps_district_name': "白云",
  'rom_version': "32",
  'longi_lati_type': "0",
  'longi_lati_time': "0",
  'content_sort_mode': "0",
  'total_memory': "3.85",
  'cpu_name': "placeholder",
  'app_enter_from': "",
  'overall_score': "11",
  'cpu_score': "11.3498",
  'host_abi': "arm64-v8a"
}

response = requests.get(url, params=params, headers=headers)
json_data = response.json()
# print(json_data)

car_info = jsonpath(json_data, '$.data.list[*]')
# print(car_info)

for car in car_info:
  car_rank = jsonpath(car, '$.rank')[0]
  print(car_rank)

  car_name = jsonpath(car, '$.series_name')[0]
  print(car_name)

  car_brand = jsonpath(car, '$.brand_name')[0]
  print(car_brand)

  car_img = jsonpath(car, '$.image')[0]
  print(car_img)

  car_count = jsonpath(car, '$.count')[0]
  print(f"销量：{car_count}")

  car_max_price = jsonpath(car, '$.max_price')[0]
  car_min_price = jsonpath(car, '$.min_price')[0]
  print(f"最高价：{car_max_price}，最低价：{car_min_price}")

  print("-----------------------------------------------")



