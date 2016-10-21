# coding: utf-8

from bs4 import BeautifulSoup
from urllib2 import urlopen
from csv_handle import csv_writelist,csv_readlist
import string
from sdate import iso_date
import os 

def url_build(cid, syear, eyear):
    start = 'jan+1+%s' % syear
    end = 'dec+12+%s' % eyear
    url_list = []
 
    url_pg1 = "https://www.google.com/finance/historical?cid=%s&startdate=%s&enddate=%s&num=200&start=0" % (cid, start, end)
    url_pg2 = "https://www.google.com/finance/historical?cid=%s&startdate=%s&enddate=%s&num=200&start=200" % (cid, start, end)
    url_pg3 = "https://www.google.com/finance/historical?cid=%s&startdate=%s&enddate=%s&num=200&start=400" % (cid, start, end)
    url_pg4 = "https://www.google.com/finance/historical?cid=%s&startdate=%s&enddate=%s&num=200&start=600" % (cid, start, end)
    url_list.append(url_pg1)
    url_list.append(url_pg2)
    url_list.append(url_pg3)
    url_list.append(url_pg4)
    return url_list
    
def data_format(date):
    month = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'11',}
    mon_tmp = str(date.split(' ')[0])
    day_tmp = date.split(' ')[1].strip(',')
    year = date.split(' ')[2]
    mon = month[mon_tmp]
    if len(day_tmp) ==2:
        data_f = '%s%s%s' % (year, mon, day_tmp)
    else:
        data_f = '%s%s0%s' % (year, mon, day_tmp)
    return data_f
        
    
def stock_pg_data(url):
    # get this page close value dict
    page = urlopen(str(url))
    soup = BeautifulSoup(page, 'lxml')
    tr_list = soup.find_all('tr')

    tr_new_list = tr_list[5:] 
    pg_data_list = []
    
    for td in tr_new_list:
        data_date = {}
        td_all_list = td.find_all('td')
        s_date = td.find('td', class_='lm').text.encode()[:-1]
        
        data_f = data_format(s_date)
        data_date['date_format'] = data_f
        #print data_f
        data_date['date'] = s_date
        
        s_value_open = td_all_list[1].text
        s_value_close = td_all_list[4].text
        value_open_float = float(string.replace(s_value_open, ',','',1))
        value_close_float = float(string.replace(s_value_close, ',','',1))        
        #print value_close_float
        data_date['open'] = value_open_float
        data_date['close'] = value_close_float
        pg_data_list.append(data_date)

    #print pg_data_list
    return pg_data_list
    
def all_data(cid,syear,eyear):
    all_data = []
    url_list = url_build(cid,syear,eyear)
    pg1_datadict = stock_pg_data(url_list[0])
    pg2_datadict = stock_pg_data(url_list[1])
    
    for i in pg1_datadict:
        all_data.append(i)
    for j in pg2_datadict:
        all_data.append(j)
        
    return all_data

def read_sid(cid):
    cid_sid = csv_readlist('cid.csv', '/srv/www/idehe.com/store/stock/')
    for i in cid_sid:
        if cid == i['CID']:
            sid = i['SID']
    return sid
    
def data_write(cid, path, data):
    sid = read_sid(cid)
    #print data
    file = '%s.csv' % (sid)
    csv_writelist(file, path, data)
    
def slist_handle(cid_file, syear, eyear, path):
    slist_tmp = csv_readlist(cid_file, path)
    slist = []
    for j in slist_tmp:
        slist.append(j['CID'])
        
    for i in slist:
        adata = all_data(i,syear, eyear)
        data_write(i, path, adata)
        
def gfile_check(SID, path):
    file = '%s.csv' % SID
    check_f = '%s%s' % (path,file)
    check = os.path.isfile(check_f) #如果不存在就返回False
    #print check
    return check
    
def data_filter(SID, path, avg_range):
    today = iso_date()
    m_value = []
    file = '%s.csv' % SID
    sdata = csv_readlist(file, path)
    
    date_fl = []
    for i in sdata:
        date_fl.append(int(i['date_format']))
    sorted(date_fl,reverse = True)
    date_filte_range = []
    for j in range(int(avg_range)):
        date_filte_range.append(str(date_fl[j]))
        
    data_fr_open = []
    for k in date_filte_range:
        for i in sdata:
            if i['date_format'] == k:
                #print i['open']
                data_fr_open.append(i['open'])
    #print len(data_fr_open)
    sum_range = 0.00
    for f in data_fr_open:
        
        sum_range +=float(f)
    #print sum_range
    avg_rg = round(sum_range/float(avg_range),1)
    #print avg_rg
        
    HV = 0
    LV = 999999
    for i in sdata:
        if float(i['close']) >= float(HV):
            HV = i['close']
    for j in sdata:
        if float(j['close']) <=float(LV):
            LV = j['close']
    
    m_value =[HV, LV, avg_rg]
    return m_value

    
    
if __name__ == "__main__":
    tmp = 'https://www.google.com/finance/historical?cid=13414271&startdate=jan+1+2015&enddate=dec+31+2016&num=200&start=200'
    cid = '13414271'
    cid_list = ['7521596','13414271']
    cid_file = 'cid.csv'
    syear = 2015
    eyear = 2016
    path = '/srv/www/idehe.com/store/stock/'
    SID = 'SH000001'
    today = '20161021'
    #data_format('jan 1, 2015')
    #adata = all_data(cid,syear, eyear)
    #print adata
    #data_write(cid, path, adata)
    #gfile_check(SID, path)
    
    #slist_handle(cid_file, syear, eyear, path)
    #data_filter(SID, path, today, '90')
    