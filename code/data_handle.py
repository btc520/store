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

def data_range(is_lis_dic):
    for i in is_lis_dic:
        #print type(i['jk'])
        cal_tmp = (float(i['jk'])-float(i['52KL']))/(float(i['52KH'])-float(i['52KL']))
        i['range'] = round(cal_tmp*100,2)
    return is_lis_dic
    

def data_mhandle(infile, outfile, file_path):
    grabed_data = grab_data(infile, file_path)
    data_ranged = data_range(grabed_data)
    csv_writelist(outfile, file_path, data_ranged)
    
if __name__ == "__main__":
    type_ifile = "type.csv"
    type_ofile = "type_data.csv"
    zhaij_ifile = "zhaij.csv"
    zhaij_ofile = "zhaij_data.csv"
    etf_ifile = "ETF.csv"
    etf_ofile = "ETF_data.csv"
    funda_ifile = 'funda.csv'
    funda_ofile = 'funda_data.csv'
    
    file_path = "/srv/www/idehe.com/store/stock_data/"
    
    data_mhandle(zhaij_ifile, zhaij_ofile, file_path)   #zhaij
    data_mhandle(type_ifile, type_ofile, file_path)   #type
    #data_mhandle(etf_ifile, etf_ofile, file_path)   #etf
    #data_mhandle(funda_ifile, funda_ofile, file_path)   #funda
    
    