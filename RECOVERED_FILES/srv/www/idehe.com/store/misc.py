from csv_data import csv_read, csv_write

def add_section(mydata, key, value):
    mydata_lst =  csv_read(mydata)
    for i in mydata_lst:
        i[key] = value
    
    csv_write(mydata_lst, mydata)


if __name__ == "__main__":
    mydata = '/srv/www/idehe.com/store/user/hechao.csv'
    add_section(mydata, "group", "-")
    