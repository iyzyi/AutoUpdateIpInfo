import os, requests
from time import sleep

password = 123456789

while (True):
    cmd = os.popen('ipconfig')
    ip_info = cmd.read()
    ip_info = ip_info.replace('\n', '<br>')
    cmd.close()

    url = 'http://127.0.0.1:12345'
    data = {'password': password, 'ip_info': ip_info}
    res = requests.post(url, data = data)
    print(res.text)

    # 一分钟更新一次
    sleep(60)