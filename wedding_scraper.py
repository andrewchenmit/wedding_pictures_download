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
    #self.url_template = 'https://www.dropbox.com/scl/fo/7buwlplni0ths389b2hwj/AADsTynZGSIAEce5P3_A4l8Wa/Jennifer%20%26%20Andrew%20(Kate)?dl=0&lst=&preview=A%26J{number}.cr2'
    self.url_template = 'https://www.dropbox.com/scl/fo/7buwlplni0ths389b2hwj/AAAKIgBgKfRT9MiZi4yXOEyna/170527-jennifer%2Bandrew?dl=0&preview=170527-AL-{number}.cr2'
    self.url_template2 = 'https://www.dropbox.com/scl/fo/7buwlplni0ths389b2hwj/AAAKIgBgKfRT9MiZi4yXOEyna/170527-jennifer%2Bandrew?dl=0&preview=170527-al-{number}.cr2'
    self.min = 1
    self.max = 1009

  def format_number(self, num):
    print 'format_number'
    return str(num)
    #length = len(str(num))
    #num_zero = 4 - length
    #return '0' * num_zero + str(num)

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
    if len(download_link) <1:
      return
    download_link[0].click()

  def click_directdownload_link(self):
    print "clicking direct download link..."
    directdownload_link = self.driver.find_elements_by_css_selector('.bubble-menu-item')
    if len(directdownload_link) < 1:
      time.sleep(2.0)
      directdownload_link = self.driver.find_elements_by_css_selector('.bubble-menu-item')
    if len(directdownload_link) < 1:
      time.sleep(2.0)
      directdownload_link = self.driver.find_elements_by_css_selector('.bubble-menu-item')
    if len(directdownload_link) < 1:
      return
    directdownload_link[0].click()

print "Starting..."
scraper = WeddingScraper()
scraper.scrape()
print "...done!"

