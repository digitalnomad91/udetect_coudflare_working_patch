# Working implementation of a 3rd patch for undetect_chromedriver that is working as of 8/1/2023. 

# Original issue that started several weeks ago:
# https://github.com/FlareSolverr/FlareSolverr/issues/811

# Still waiting on this (seemingly) more robust method to be implemented & released:
# https://github.com/ultrafunkamsterdam/undetected-chromedriver/discussions/1420

# Here is the latest version of flaresolverr with this fix implemented: 
# https://github.com/Dexcelerate/FlareSolverr-udetect-patch/ 

# Note: I haven't tested running it through a new docker image / container, but it should work just fine. I'll include a systemd service implementation for those that want to run it standalone.

# I also put together a small browser extension that can run in Chrome or Firefox that worked well enough to get me through the periods where CF was winning. Will probably be useful for if/when there are no known solutions like right now:
# https://github.com/digitalnomad91/cloudflare-bypass-extension

# Note: Don't forget to pip3 install the packages imported below & then you can run python3 fuck_cloudflare.py and check if it is working.


import time
import logging
import os
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import undetected_chromedriver as uc
from pathlib import Path


logging.basicConfig(level=10)
logger = logging.getLogger('test')

def main():

    browser_executable_path = str('/bin/chromium')
    options = uc.ChromeOptions()
    options.add_argument("--auto-open-devtools-for-tabs")
    
    options.add_argument("--disable-popup-blocking")

    options.headless = True
    options.add_argument( '--headless' )

    options.browser_executable_path=browser_executable_path

    driver = uc.Chrome( options = options)
    logging.getLogger().setLevel(10)

    url = 'http://bscscan.com/contractsVerified'
    driver.get('http://bscscan.com/contractsVerified')
    driver.execute_script(f"window.open('{url}', '_blank')")

    logger.info('current url %s' % driver.current_url)

    try:
        WebDriverWait(driver,15).until(EC.title_contains('moment'))
    except TimeoutException:
        pass

    logger.info('current page source:\n%s' % driver.page_source)

    logger.info('current url %s' % driver.current_url)

    try:
        WebDriverWait(driver,15).until(EC.title_contains('BscScan'))
        logger.info('PASSED CLOUDFLARE!')

    except TimeoutException:
        logger.info('timeout')
        print(driver.current_url)

    logger.info('current page source:\n%s\n' % driver.page_source)


    driver.quit()




if __name__ == "__main__":
    main()
