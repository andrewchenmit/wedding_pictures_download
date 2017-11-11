import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WeddingScraper:
  def __init__(self):
    # Set unconfigurables.
    fp = webdriver.FirefoxProfile('/Users/andrewchen/Library/Application Support/Firefox/Profiles/4ax3g6ys.default')
    self.driver = webdriver.Firefox(fp)
    self.url_template = 'https://www.dropbox.com/scl/fo/7buwlplni0ths389b2hwj/AADsTynZGSIAEce5P3_A4l8Wa/Jennifer%20%26%20Andrew%20(Kate)?dl=0&lst=&preview=A%26J{number}.cr2'
    self.min = 17
    self.max = 846
#    self.max = 3

  def format_number(self, num):
    print 'format_number'
    length = len(str(num))
    num_zero = 4 - length
    return '0' * num_zero + str(num)

  # https://www.dropbox.com/scl/fo/7buwlplni0ths389b2hwj/AADsTynZGSIAEce5P3_A4l8Wa/Jennifer%20%26%20Andrew%20(Kate)?dl=0&lst=&preview=A%26J0002.cr2
  def scrape(self):
    print 'scrape'
    for i in xrange(self.min, self.max + 1):
      print i
      # Load page.
      url = self.url_template.format(
        number = self.format_number(i)
      )
      print url
      self.driver.get(url)
      self.click_download_link()
      self.click_directdownload_link()
      print "start waiting"
      time.sleep(15.0)
      print "done waiting"

  def click_download_link(self):
    print "clicking download link..."

#    try:
#      print "trying"
#      element = WebDriverWait(driver, 15).until(
#        EC.presence_of_element_located((By.ID, 'bubbleDropdownTarget-33')) or EC.presence_of_element_located((By.ID, 'bubbleDropdownTarget-34'))
#      )
#    finally:
#      return

    download_link = self.driver.find_elements_by_css_selector('#bubbleDropdownTarget-33')
    if len(download_link) < 1:
      download_link = self.driver.find_elements_by_css_selector('#bubbleDropdownTarget-34')
    if len(download_link) < 1:
      download_link = self.driver.find_elements_by_css_selector('#bubbleDropdownTarget-32')
    download_link[0].click()

  def click_directdownload_link(self):
    print "clicking direct download link..."
    directdownload_link = self.driver.find_elements_by_css_selector('.bubble-menu-item')
    if len(directdownload_link) < 1:
      directdownload_link = self.driver.find_elements_by_css_selector('.bubble-menu-item')
    if len(directdownload_link) < 1:
      directdownload_link = self.driver.find_elements_by_css_selector('.bubble-menu-item')
    directdownload_link[0].click()

print "Starting..."
scraper = WeddingScraper()
scraper.scrape()
print "...done!"

