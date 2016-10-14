import sys
sys.path.append("..")
from data_handle import data_mhandle
from html_handle import index_write
funda_ifile = 'zhaij.csv'
funda_ofile = 'zhaij_data.csv'

file_path = "/srv/www/idehe.com/store/stock_data/"

data_mhandle(funda_ifile, funda_ofile, file_path)

index_write()