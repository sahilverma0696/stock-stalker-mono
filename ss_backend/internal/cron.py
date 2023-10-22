import logging
from internal.modules.yfinance import fetch
from internal.views import getDate
from datetime import datetime
from internal.modules.dateutility.datefunc import is_time_difference_valid

logger = logging.getLogger(__name__)


def runCron():
    logger.info("In CRON func")

    lastest_date_in_db = getDate()
    today_date = datetime.now().date()

    if(is_time_difference_valid(lastest_date_in_db,today_date=today_date)):
        logger.info("Condition true, fetching data from ",lastest_date_in_db,"to",today_date)
        fetch.fetchData()
