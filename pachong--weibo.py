# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:42:20 2018

@author: malt927
"""
import urllib
import base64
import rsa

servertime = 1535460733
nonce = "57E93Q"
rsakv = "1330428213"
pubkey = "EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443"

def get_su(username):
    s_username = urllib.quote(username)
    s_username = base64.encodestring(s_username)
    return s_username[:-1]

def get_sp(password, servertime, nonce, pubkey):
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(password) # 拼接明文加密文件中得到
    rsaPublickey = int(pubkey, 16)
    key = rsa.PublicKey(rsaPublickey, 65537) #创建公钥，10001对应的10进制
    s_password = rsa.encrypt(message, key)  #加密
    s_password = binascii.b2a_hex(s_password)  #将加密信息转换为16进制。
    return s_password

post_parm = {
        "etry":"weibo",
        "gateway":"1",
        "from":"",
        "savestate":"7",
        "useticket":"1",
        "pagerefer":"",
        "vsnf":"1",
        "su": s_username,
        "service":"miniblog",
        "servertime": servertime,
        "nonce": nonce,
        "pwencode":"rsa2",
        "rsakv": rsakv,
        "sp":s_password,
        "sr":"1920*1080",
        "encoding":"UTF-8",
        "prelt":"119",
        "url":"http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack",
        "returntype": "META"
        }

request = urllib2.Request(url=login_URL, data=post_data, headers=post_Header)
result = urllib2.urlopen(request)
text = result.read() # 读取内容
print ("text==>",text)










