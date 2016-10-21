import sys
#sys.path.append("..")
sys.path.append('/srv/www/idehe.com/store/code')

from html_handle import index_write
from google_data import slist_handle
from data_handle import data_mhandle_index

ifile = 'index.csv'
ofile = 'index_data.csv'
#today = '20161021'
avg_range = '90'
file_path = "/srv/www/idehe.com/store/stock_data/"
g_path = '/srv/www/idehe.com/store/stock/'

cid_file = 'cid.csv'

slist_handle(cid_file, '2015', '2016', g_path)

data_mhandle_index(ifile, ofile, file_path, g_path, avg_range)

index_write()