# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 22:02:20 2018

@author: malt927
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

url_start = 'https://hz.lianjia.com/ershoufang/'
urlList = []
urlList.append(url_start)

def getHoursePrice(n):
    for i in range(1,n+1):
        urlList.append(url_start + 'pg' + str(i) + '/')
    
    dataList = []
    
    for url in urlList:
        res = requests.get(url)
        soup = BeautifulSoup(res.text,features='html.parser')
        hourseList = soup.find_all('li',class_ = 'clear')
    
        for i in range(len(hourseList)):
            tempList = []
            hourseDetail = hourseList[i].find('div',class_ = 'info clear')
            title = hourseDetail.find('div',class_ = 'title').find('a').text.strip()
            address = hourseDetail.find('div',class_ = 'address').find('a').text.strip()
            detail = hourseDetail.find('div',class_ = 'address').find('div',class_ = 'houseInfo').text.strip()
            flood = hourseDetail.find('div',class_ = 'flood').find('div',class_ = 'positionInfo').text.strip()
            followInfo = hourseDetail.find('div',class_ = 'followInfo').text
            subway = hourseDetail.find('div',class_ = 'tag').find('span',class_ = 'subway')
            taxfree = hourseDetail.find('div',class_ = 'tag').find('span',class_ = 'taxfree')
            haskey = hourseDetail.find('div',class_ = 'tag').find('span',class_ = 'haskey')
            if subway is not None:
                subway = subway.text
            if taxfree is not None:
                taxfree = taxfree.text
            if haskey is not None:
                haskey = haskey.text
            totalprice = hourseDetail.find('div',class_ = 'priceInfo').find('div',class_ = 'totalPrice').text
            unitprice = hourseDetail.find('div',class_ = 'priceInfo').find('div',class_ = 'unitPrice').text
            tempList.append(title)
            tempList.append(address)
            tempList.append(detail)
            tempList.append(flood)
            tempList.append(followInfo)
            tempList.append(subway)
            tempList.append(taxfree)
            tempList.append(haskey)
            tempList.append(totalprice)
            tempList.append(unitprice)
            dataList.append(tempList)
    data = pd.DataFrame(dataList,columns = [u'标题',u'地址',u'房屋详情',u'楼层',u'关注情况',u'地铁',u'税费',u'钥匙',u'总价',u'单价'])
    data.to_excel('E:\\hourse.xlsx')
    print "运行完毕"