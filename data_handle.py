#! /usr/bin/python
#-*- encoding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')


from csv_handle import csv_readlist, csv_writelist
from xq_handle import data_get, select_data

def grab_data(ifile, file_path):
    is_lis_dic = csv_readlist(ifile, file_path)
    for i in is_lis_dic:
        sdict = data_get(i['SID'])
        fine_data = select_data(sdict)
        i.update(fine_data)
    return is_lis_dic

def cal_data(is_lis_dic):
    for i in is_lis_dic:
        #print type(i['jk'])
        cal_tmp = (float(i['jk'])-float(i['52KL']))/(float(i['52KH'])-float(i['52KL']))
        i['range'] = round(cal_tmp*100,2)
    return is_lis_dic

def data_save(ofile, file_path, data):
    csv_writelist(ofile, file_path, data)
    
if __name__ == "__main__":
    ifile_type = "type.csv"
    ofile_type = "type_data.csv"
    ifile_etf = "ETF.csv"
    ofile_etf = "ETF_data.csv"
    file_path = "/srv/www/idehe.com/store/stock_data/"
    
    #type
    grabed_data_type = grab_data(ifile_type, file_path)
    caled_data_type = cal_data(grabed_data_type)
    data_save(ofile_type, file_path, caled_data_type)

    #etf
    grabed_data_etf = grab_data(ifile_etf, file_path)
    caled_data_etf = cal_data(grabed_data_etf)
    data_save(ofile_etf, file_path, caled_data_etf) 