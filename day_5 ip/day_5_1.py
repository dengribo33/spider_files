import requests
from retrying import retry

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

def read_ip():
    with open('ip.txt', 'r',encoding='utf-8') as f:
        result = f.read()

        ip_list = result.split('\n')[:-1]
        return ip_list

@retry(stop_max_attempt_number=3)
def send_proxies(proxies_dict):
    print(proxies_dict)
    response = requests.get(url, headers=headers, proxies=proxies, timeout=3)
    if response.status_code == 407:
        raise Exception('代理ip无效')


if __name__ == '__main__':
    ip_list = read_ip()

    url = 'http://myip.ipip.net'
    for ip in ip_list:
        proxies = {'http':ip}
        try:
            html = send_proxies(proxies)
            print(f'{ip} is OK')
        except Exception as e:
            print(f'{ip} is not OK')