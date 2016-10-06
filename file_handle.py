import os

def find_file(file, user_path):
    # check file exist
    filelist = []

    filelist = os.listdir(user_path)
    if file in filelist:
        return True
    
if __name__ == "__main__":
    user_path = '/srv/www/idehe.com/store/stock_data/'
    file = 'ETF.csv'
    print find_file(file, user_path)
