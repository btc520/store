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

def h_content(desc, table1, table2, table3, table4):
    layout = """
    <div class="container">
        <div class="row clearfix">
    		<div class="col-md-12 column">
    		%s
    		</div>
    	</div>
    	
    	<div class="row clearfix">
    		<div class="col-md-6 column">
    		%s
    		</div>
    		<div class="col-md-6 column">
    		%s
    		</div>
	    </div>

    	<div class="row clearfix">
    		<div class="col-md-6 column">
    		%s
    		</div>
    		<div class="col-md-6 column">
    		%s
    		</div>
	    </div>
	    
	</div>
	</div>
    """ % (desc, table1, table2, table3, table4)
    
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
    t.th('52K区间')
    t.th('52K最高')
    t.th('52K最低')
    t.th('今开')
    t.th('市值')
    t.th('30日均量')
    t.th('折溢价')
    
    for i in data:
        #print i
        r = t.tr
        r.td(str(i['SID']))
        r.td(str(i['cname']))
        r.td(str(i['range'])+"%")
        r.td(str(i['52KH']))
        r.td(str(i['52KL']))
        r.td(str(i['jk']))
        r.td(str(i['volumn']))
        r.td(str(i['30avg']))
        r.td(str(i['premium']))
    return str(dtable)


def sort_range(file, file_path, type):
    # sort by: range, 
    ls_dt = csv_readlist(file, file_path)
    range_ls = []
    range_ls_tmp =[]
    n_lsdt = []
    
    for i in ls_dt:
        range_ls_tmp.append(i[type])
    range_ls = sorted(range_ls_tmp)

    for k in range_ls:
        for i in ls_dt:
            if i[type] == k:
                n_lsdt.append(i)
        
    return n_lsdt

def sort_range_f5(lsdt):
    lsdt5 = []
    for i in lsdt[:7]:
        lsdt5.append(i)
    #lsdt.remove([5:-1])
    return lsdt5
    
def html_stock_list(stock_data):
    stock_list = HTML()
    stock_list.h2("持仓一览！")
    t = stock_list.table(border='2px', width ='70%', klass ='table table-bordered')
    t.th('ID')
    t.th('名称')
    t.th('状态')
    t.th('分组')
    t.th('52W-L')
    t.th('52W-P')
    t.th('52K区间')
    t.th('市价')
    t.th('市价/目标价比')
    t.th('目标价')
    t.th('我的价格')
    t.th('份额')
    t.th('市值')
    t.th('仓位')
    t.th('Update')
    
    ratio_list =[]
    
    for i in stock_data:
        ratio_list.append(i['lh_ratio'])
    
    ratio_list_sorted = sorted(ratio_list)
    
    #print ratio_list_sorted
    
    for j in ratio_list_sorted:
        
        for i in stock_data:
            if i['lh_ratio'] == j:
                r = t.tr
                r.td(str(i['code']))
                r.td(str(i['name']))
                r.td(str(i['status']))
                r.td(str(i['group']))
                r.td(str(i['low52week']))
                r.td(str(i['high52week']))
                if i['lh_ratio'] is not "":
                    r.td.b("%.2f %%" % (float(i['lh_ratio'])*100.0))
                else:
                    r.td("")
                r.td(str(i['current']))
                if float(i['target_ratio'])*100 <= 10 and float(i['target_ratio'])*100 !=0:
                    r.td.b("%.2f %%" % (float(i['target_ratio'])*100.0))
                else:
                    r.td("%.2f %%" % (float(i['target_ratio'])*100.0))
                r.td(str(i['target']))
                r.td(str(i['cost']))
                r.td(str(i['share']))
                r.td(str(i['value']))
                r.td("%.2f %%" % (float(i['store'])*100.0))
                r.td("%s(%s)" % (str(i['time']), str(i['update_date'])))
        
    return str(stock_list)
   
    
def html_table_setprice(dir):
    h = HTML()
    h.h3("更新目标价")
    #webform = h.form
    f = h.form(action=dir, method="post")
    
    f.p("Code: ")
    f.input(type="text", name= "code")
    f.br
    
    f.p("Target: ")
    f.input(type="text", name= "target")
    f.br
    
    f.input(type="submit", name= "submit")
    f.br
    return str(h)
    
def html_table_filter(dir):
    h = HTML()
    h.h3("过滤分组")
    #webform = h.form
    f = h.form(action=dir, method="post")
    
    f.p("Group: ")
    f.input(type="text", name= "group")
    f.br
    
    f.input(type="submit", name= "submit")
    f.br
    return str(h)
    
def html_table_chg_filter(dir):
    h = HTML()
    h.h3("修改属性")
    #webform = h.form
    f = h.form(action=dir, method="post")

    f.p("Code: ")
    f.input(type="text", name= "code")
    f.br
    
    f.p("Key: ")
    f.input(type="text", name= "key")
    f.br
    
    f.p("Value: ")
    f.input(type="text", name= "value")
    f.br
    
    f.input(type="submit", name= "submit")
    f.br
    return str(h)
    
def html_table_setshare(dir):
    h = HTML()
    h.h3("更新我的库存:  ")
    #webform = h.form
    f = h.form(action=dir, method="post")

    f.p("code: ")
    f.input(type="text", name= "code")
    f.br
    
    f.p("Share： ")
    f.input(type="text", name= "share")
    f.br
    
    f.input(type="submit", name= "submit")
    f.br
    return str(h)
    
def html_table_setcost(dir):
    h = HTML()
    h.h3("更新我的买入价:  ")
    #webform = h.form
    f = h.form(action=dir, method="post")

    f.p("Code: ")
    f.input(type="text", name= "code")
    f.br
    
    f.p("Cost： ")
    f.input(type="text", name= "cost")
    f.br
    
    f.input(type="submit", name= "submit")
    f.br
    return str(h) 
    
def html_table_addnew(dir):
    h = HTML()
    h.h3("添加新的股票： ")
    #webform = h.form
    f = h.form(action=dir, method="post")
    
    f.p("code: ")
    f.input(type="text", name= "code")
    f.br

    f.p("exchange: ")
    f.input(type="text", name= "exchange")
    f.br    

    
    f.input(type="submit", name= "submit")
    f.br

    return str(h)


def html_content_dc(user):
    html_cont = {}
    html_setprice = html_table_setprice(user)
    html_setshare = html_table_setshare(user)
    html_setcost = html_table_setcost(user)
    html_addnew = html_table_addnew(user)
    html_table_filter_str = html_table_filter(user)
    html_table_chg_filter_str = html_table_chg_filter(user)
    html_cont['setprice'] = html_setprice
    html_cont['setshare'] = html_setshare
    html_cont['setcost'] = html_setcost
    html_cont['addnew'] = html_addnew
    html_cont['filter'] = html_table_filter_str
    html_cont['chg_filter'] = html_table_chg_filter_str
    return html_cont

def index_write():
    f = open('/srv/www/idehe.com/store/index.html','w')
    
    file_etf = "ETF_data.csv"
    file_type = "type_data.csv"
    file_funda = "funda_data.csv"
    file_zhaij = "zhaij_data.csv"
    file_path = '/srv/www/idehe.com/store/stock_data/'
    
    etf_data = sort_range(file_etf, file_path, 'range')
    type_data = sort_range(file_type, file_path, 'range')
    sfunda_data = sort_range(file_funda, file_path, 'range')
    zhaij_data = sort_range(file_zhaij, file_path, 'range')
    f5_funda = sort_range_f5(sfunda_data)
    
    table_e = table(etf_data, '主要市场ETF', '1年价格排序/')
    #print table_e
    table_t = table(type_data, '主题ETF', '1年价格排序/')
    table_fa = table(f5_funda, '分级A', "选取隐含收益5%以上/成交量100W以上/1年价格排序/52K最高价有峰值错误点u不准确的：军工股A，网金融，房地产，中行军, 食品，环保A")
    table_zj = table(zhaij_data, '债基', '主要看折溢价/')
    
    desc = page_desciption()
    content = h_content(desc, table_e, table_t, table_fa, table_zj)
    
    h = html(content)
    
    f.writelines(h)
    
        
if __name__ == "__main__":
    index_write()
    