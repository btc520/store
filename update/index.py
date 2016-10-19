import sys
#sys.path.append("..")
sys.path.append('/srv/www/idehe.com/store/code')

from html_handle import index_write

from data_handle import data_mhandle_index

ifile = 'index.csv'
ofile = 'index_data.csv'

file_path = "/srv/www/idehe.com/store/stock_data/"

data_mhandle_index(ifile, ofile, file_path)

index_write()