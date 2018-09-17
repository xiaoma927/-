# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 23:17:47 2018

@author: malt927
"""
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
def getData(n,loadPath = 'E:\\zhiwei_hangzhou.xlsx'):
    startTime = time.time()
    urlList = []
    for i in range(1,n+1):
        ##杭州的职位
        urlList.append('https://search.51job.com/list/080200,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%25E5%25B8%2588,2,' + str(i) + '.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=')
        ##上海的职位
        #urlList.append('http://search.51job.com/list/020000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,' + str(i) + '.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=21&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=')
    List = []
    for url in urlList:
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        html = BeautifulSoup(response.text,features='html.parser')
        datalist = html.find_all('div',class_ = 'el')
        for i in range(16,len(datalist)):
            templist = []
            zhiwei = datalist[i].find('p').find('span').text.strip()
            company = datalist[i].find('span',class_ = 't2').text.strip()
            area = datalist[i].find('span',class_ = 't3').text.strip()
            salary = datalist[i].find('span',class_ = 't4').text.strip()
            updatedate = datalist[i].find('span',class_ = 't5').text.strip()
            templist.append(zhiwei)
            templist.append(company)
            templist.append(area)
            templist.append(salary)
            templist.append(updatedate)
            List.append(templist)
    df = pd.DataFrame(List,columns = [u'职位',u'公司',u'地址',u'工资',u'更新日期'])
    df.to_excel(loadPath)
    endTime = time.time()
    detalTime = endTime - startTime
    print ("程序运行完毕，共用时",detalTime)






