import os, requests, time
from time import sleep

password = 123456789

while (True):
    cmd = os.popen('ipconfig')
    ip_info = cmd.read()
    ip_info = ip_info.replace('\n', '<br>')
    cmd.close()

    ip_info = '更新时间：' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '<br><br>' + ip_info

    url = 'http://127.0.0.1:12345'
    data = {'password': password, 'ip_info': ip_info}
    try:
        res = requests.post(url, data = data)
        print(res.text)
    except Exception as e:
        print('出错：', e)

    # 一分钟更新一次
    sleep(60)
