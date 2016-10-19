# -*- coding: utf-8 -*- 
from html import HTML

from csv_handle import csv_readlist


def html(html_body):
    html_header ="""
    <!DOCTYPE html>
    <html>
    <head>
    <title>This is my stock manager!</title>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
    <script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
    </head>
    <body>
    %s
    </body>
    </html>""" % (html_body)
    return html_header

def h_content(desc, t1, t2, t3, t4, t5, t6):
    layout = """
    <div class="container">
        <div class="row clearfix">
    		<div class="col-md-12 column">
    		%s
    		</div>
    	</div>
    	
        <div class="row clearfix">
    		<div class="col-md-12 column">
    		%s
    		</div>
    	</div>
    	
        <div class="row clearfix">
    		<div class="col-md-12 column">
    		%s
    		</div>
    	</div>

        <div class="row clearfix">
    		<div class="col-md-12 column">
    		%s
    		</div>
    	</div>

        <div class="row clearfix">
    		<div class="col-md-12 column">
    		%s
    		</div>
    	</div>

        <div class="row clearfix">
    		<div class="col-md-12 column">
    		%s
    		</div>
    	</div>

        <div class="row clearfix">
    		<div class="col-md-12 column">
    		%s
    		</div>
    	</div>
    	
	</div>
	</div>
    """ % (desc, t1, t2, t3, t4, t5, t6)
    
    return layout


def page_desciption():
    page_desc = HTML()
    page_desc.h2("Welcome!")
    l = page_desc.ol
    l.li('This is the store of all my stocks! thanks for visiting!')

    return str(page_desc)

def table(data, title, tdesc):
    dtable = HTML()
    dtable.h3(title)
    
    desc = []
    if tdesc !="":
        desc = tdesc.split("/")
    l = dtable.ol
    for k in desc:
        l.li(k)

    t = dtable.table(border='2px', width ='60%', klass ='table table-bordered')
    t.th('SID')
    t.th('名称')
    t.th('52W区间')
    t.th('52W最高')
    t.th('52W最低')
    t.th('价格')
    t.th('市值')
    t.th('30日均量(总市值)')
    t.th('折溢价')
    t.th('组别')
    t.th('X?')
    
    for i in data:
        #print i
        r = t.tr
        r.td(str(i['SID']))
        r.td(str(i['cname']))
        r.td(str(i['range'])+"%")
        r.td(str(i['52KH']))
        r.td(str(i['52KL']))
        r.td(str(i['current_price']))
        r.td(str(i['volumn']))
        r.td(str(i['30avg']))
        r.td(str(i['premium']))
        r.td(str(i['category']))   
        r.td(str(i['disct']))
    return str(dtable)


def sort_range(file, file_path, type):
    # sort by: range, 
    ls_dt = csv_readlist(file, file_path)
    range_ls = []
    range_ls_tmp =[]
    n_lsdt = []

    for i in ls_dt:
        if i[type][-1].isdigit() == False:
            i[type] = i[type][:-1]
            #print i[type]
        if i[type] == '':
            i[type] = '0.0'
        if i[type] not in range_ls_tmp:
            range_ls_tmp.append(i[type])
    range_ls = sorted(range_ls_tmp)
    print range_ls

    for k in range_ls:
        for i in ls_dt:
            if i[type] == k:
                n_lsdt.append(i)
        
    return n_lsdt

def sort_range_f5(lsdt):
    lsdt5 = []
    for i in lsdt[:11]:
        lsdt5.append(i)
    #lsdt.remove([5:-1])
    return lsdt5

def index_write():
    f = open('/srv/www/idehe.com/store/index.html','w')
    
    file_etf = "ETF_data.csv"
    file_type = "topic_data.csv"
    file_funda = "funda_data.csv"
    file_zhaij = "zhaij_data.csv"
    file_uncategory = "uncategory_data.csv"
    file_index = "index_data.csv"
    
    file_path = '/srv/www/idehe.com/store/stock_data/'
    
    etf_data = sort_range(file_etf, file_path, 'range')
    topic_data = sort_range(file_type, file_path, 'range')
    zhaij_data = sort_range(file_zhaij, file_path, 'premium')
    uncategory_data = sort_range(file_uncategory, file_path, 'range')
    index_data = sort_range(file_index, file_path, 'range')
    
    sfunda_data = sort_range(file_funda, file_path, 'range')
    f5_funda = sort_range_f5(sfunda_data)
    
    
    table_e = table(etf_data, '主要市场ETF', '1年价格排序/')
    #print table_e
    table_t = table(topic_data, '主题ETF', '1年价格排序/')
    table_fa = table(f5_funda, '分级A', "选取隐含收益5%以上，成交量100W以上，1年价格排序/52K不准确：环保，军工股A，网金融/X=分级A合并溢价")
    table_zj = table(zhaij_data, '场内债基', '主要看折溢价，成交量/年化折价')
    table_un = table(uncategory_data, '其他未分类', 'X=封基年化折价')
    table_ind = table(index_data, '指数', '')
    
    desc = page_desciption()
    content = h_content(desc, table_ind, table_e, table_t, table_fa, table_zj, table_un)
    
    h = html(content)
    
    f.writelines(h)
    
        
if __name__ == "__main__":
    index_write()
 
 
 
    