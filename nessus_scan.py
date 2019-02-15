#coding=utf-8
## __author__ = "Fidcer" ##

import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def login_create():
    # 登录成功则返回token，否则返回空
    token = ''
    # 调用/session接口
    url = "https://localhost:8834/session"
    # nessus的用户名密码作为post的payload
    data = {
        'username': 'admin',
        'password': 'admin'
    }
    # 发送请求
    respon = requests.post(url, data=data, verify=False)
    # 如果请求成功则返回token值
    if respon.status_code == 200:
        # 返回值是一个json字符串，用json.loads解析成字典取值
        token = json.loads(respon.text)['token']
        #print(token)
    return token

def get_scans_list():

    # 返回结果
    result = ''
    # 首先获取一下token
    token = login_create()
    #print(token)
    if token != '':
        # 调用/folders接口
        url = "https://localhost:8834/scans"
        # 组装一个请求的头,把刚刚拿到的token放入请求头
        header = {'X-Cookie': 'token={token};'.format(token=token),
                  'Content-type': 'application/json',
                  'Accept': 'text/plain'}
        respon = requests.get(url, headers=header, verify=False)
        # 请求成功，则返回结果，否则返回空值
        if respon.status_code == 200:
            result = json.loads(respon.text)
            print(result)
    return result


def get_scan_id(scanname):
    # 任务ID
    scan_id = 0
    # 获取任务列表
    scans_list = get_scans_list()['scans']
    if scans_list != '':
        # 遍历任务列表
        for scan in scans_list:
            # 判断是否是指定的任务
            if scan['name'] == scanname:
                scan_id = scan['id']
                break
    # 如果未找到，则返回0
    return scan_id

# iplist为扫描目标IP的列表
def scan_luanch(iplist):

    # header信息在全局变量中，之后的实例中将不再重复
    # 调用/scans/{scan_id}/launch
    url = 'https://localhost:8834/scans/{scan_id}/launch'.format(scan_id=get_scan_id('default'))
    # 扫描目标放在请求的payload里
    data = {
        'alt_targets': iplist
    }
    # 发送请求
    respon = requests.post(url,data=data, verify=False)
    # 是否请求成功
    print(respon.text)
    if respon.status_code == 200:
        return True
    else:
        return False
scan_luanch(['1.1.1.0', '1.1.1.1'])
