#! /usr/bin/python
#-*- encoding: utf-8 -*-

import cookielib, urllib2
from bs4 import BeautifulSoup
from urllib2 import urlopen
import string

def raw_data(sid, url_prefix):
    url = url_prefix+sid
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    # default User-Agent ('Python-urllib/2.6') will *not* work
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'),
        ]
    #open homepage first to get cookie, and then open target URL again to get the target content
    home = opener.open('http://xueqiu.com')
    quote = opener.open(url)
    content = quote.read()
    return content

def data_get(sid):
    url_prefix = "https://xueqiu.com/S/"
    # filter table td data from raw by soup
    rawdata = raw_data(sid, url_prefix)
    soup = BeautifulSoup(rawdata, 'lxml')
    #toptable all td
    toptable = soup.find('table', class_="topTable")
    #table_body = toptable.find('tbody')
    #print type(toptable)
    td_list = toptable.find_all("td")
    sid_dict = {}
    #sid_dict['name'] = sid
    #print len(td_list)
    for i in range(len(td_list)):
        #print i
        head = td_list[i].find(text=True)
        head_num = td_list[i].find('span').text
        sid_dict[head] = head_num
    return sid_dict

def select_data(sdict):
    # english data and select data
    e_data = {}
    e_data['52KH'] = sdict[u'52\u5468\u6700\u9ad8\uff1a'].encode()
    e_data['52KL'] = sdict[u'52\u5468\u6700\u4f4e\uff1a'].encode()
    e_data['volumn'] = sdict[u'\u8d44\u4ea7\u51c0\u503c\uff1a']
    e_data['jk'] = sdict[u'\u4eca\u5f00\uff1a']
    return e_data

    
    
if __name__ == "__main__":
    sid = "SZ160211"
    #raw_data = raw_data(url)
    sid_dict = data_get(sid)
    print sid_dict
    select_data(sid_dict)
    
    
    