from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

dt = datetime.now()  

def iso_date():
    std_date = dt.strftime('%Y%m%d')
    return std_date
    