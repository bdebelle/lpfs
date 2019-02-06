"""
logging demo 1
Logging Levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""
# what we've been doing
# print("this is a test using a print statement")

#default module from python library
import logging
#Logging Threshold is anything above the Warning (warning/error/critical)
# logging.warning("warning message")
# logging.info("info message")
# logging.error("error message")


# Sets threshold at DEBUG so all errors logged in new file test.log
logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.warning("warning message")
logging.info("info message")
logging.error("error message")