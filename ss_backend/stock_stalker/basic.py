# this is a basic file to be included in all of the files
# does contains infra support products which are needed in almost all files 

##logging 
import logging

LOG = logging.getLogger(__name__)

"""
USAGE:
from stock_stalker.basic import LOG

LOG.info("info log statements")

LOG.error("error log statements")
"""
