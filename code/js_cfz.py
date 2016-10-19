#! /usr/bin/python
#-*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen
import json
from csv_handle import csv_readlist, csv_writelist

def raw_data(funda_url):
    funda_lst = []
    page = urlopen(funda_url)
    soup = BeautifulSoup(page, "lxml")
    
    soup = soup.p.string # element tag, remove html
    null = ''
    soup = eval(soup)
    rows_str = json.dumps(soup['rows'],indent=1, encoding="UTF-8", ensure_ascii=False)
    #rows_str =unicode.encode(rows_str,'utf-8')
    funda_list=json.loads(rows_str)
    #print type(funda_list[0])
    #print funda_list[0]
    for i in funda_list:
        funda_lst.append(i[u'cell'])
    #for j in funda_lst:
        #print j[u'funda_profit_rt_next']
    #print funda_lst
    return funda_lst

def filter_d(funda_lst):
    nlst = []
    for i in funda_lst:
        temp_dic = {}
        tSID = i[u'fund_id']
        temp_dic['disct'] =  i[u'annual_discount_rt']
        if tSID[0] == '1':
            temp_dic['tSID'] = 'SZ'+tSID
        elif tSID[0] == '5':
            temp_dic['tSID'] = 'SH'+tSID
        nlst.append(temp_dic)
    return nlst
    
def dict_update(file, file_path, nlst):
    old_d = csv_readlist(file, file_path)
    for i in nlst:
        for j in old_d:
            if i['tSID'] == j['SID']:
                j['disct'] = i['disct']
            #print j
    
    #print old_d            
    csv_writelist(file, file_path, old_d)  
                
        
    
if __name__ == "__main__":
    funda_url = 'https://www.jisilu.cn/jisiludata/CloseBondFund.php'
    file = 'zhaij.csv'
    file_path = '/srv/www/idehe.com/store/stock_data/'

    funda_rawdata = raw_data(funda_url)
    nlst = filter_d(funda_rawdata)
    dict_update(file, file_path, nlst)
    
    
    
    
    
    