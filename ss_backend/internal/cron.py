from stock_stalker.basic import LOG
from internal.utility.modules.yfinance.fetch import fetchData
from internal.utility.modules.dateutility.datefunc import getDate, is_time_difference_valid
from datetime import datetime


def runCron():
    LOG.info("In CRON func")

    lastest_date_in_db = getDate("SBIN") #TODO: handle this cron to new versions
    today_date = datetime.now().date()

    if(is_time_difference_valid(lastest_date_in_db,today_date=today_date)):
        LOG.info("Condition true, fetching data from ",lastest_date_in_db,"to",today_date)
        fetchData()
