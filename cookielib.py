import os, logging
import logconf

logger = logging.getLogger(__name__)
logger.setLevel(logconf.loggerLevel)

cookies = ""

logger.debug("Opening Cookies")
with open("cookies.txt", "r") as cookiesFile:
    cookies_contents = cookiesFile.read()
    cookies = cookies_contents
    cookiesFile.close()
logger.info("Cookies loaded")