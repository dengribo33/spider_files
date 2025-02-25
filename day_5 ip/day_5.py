import requests
from retrying import retry

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

def read_ip_addr():
    with open('ip.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    # print(text)
    ip_list = text.split('\n')[:-1]
    return ip_list

@retry(stop_max_attempt_number=3)
def send_request(proxies_dict):
    print(proxies_dict)
    response = requests.get(url, headers=headers, proxies=proxies_dict, timeout=3)
    if response.status_code == 407:
        raise Exception('代理IP无效')


if __name__ == '__main__':
    ip_list = read_ip_addr()

    for ip in ip_list:
        url = 'http://myip.ipip.net'
        proxies = {'http': ip}
        try:
            send_request(proxies)
        except Exception as e:
            print(e)
