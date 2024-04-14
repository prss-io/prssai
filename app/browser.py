# os
import urllib
import random
from random import randint
from time import sleep
from colorist import Color
from bs4 import BeautifulSoup

# Setup Selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

class Browser:
  def __init__(self, chrome_host, chrome_port, search_follow_links):
    self.chrome_host = chrome_host
    self.chrome_port = chrome_port
    self.search_follow_links = search_follow_links
    self.options = webdriver.ChromeOptions()
    self.options.add_argument('--ignore-ssl-errors=yes')
    self.options.add_argument('--ignore-certificate-errors')
    self.saved_urls = []

  def echo(self, content: str):
    print(f"{Color.GREEN} Browser | {Color.OFF}{Color.WHITE}{content}{Color.OFF}")

  def navigate(self, url: str):
    self.echo("Connecting Chrome")
    driver = webdriver.Remote(command_executor=f'http://{self.chrome_host}:{self.chrome_port}/wd/hub', options=self.options)
    #self.echo("Chrome Connected")

    # maximize the window size
    driver.maximize_window()

    # navigate to site
    self.echo(f"Navigate: {url}")
    driver.get(url)

    # wait for ready state
    self.echo("Wait for ready state")
    try:
      WebDriverWait(driver, 30).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
    except TimeoutException as err:
      raise TimeoutError("Page not loaded") from err
    sleep(randint(2,5))
    
    # get source
    source = driver.page_source

    # close browser
    driver.close()
    driver.quit()

    # return
    return source

  def search(self, queryOrUrl: str):
    #self.echo(f"Search: {queryOrUrl}")
    sleep(randint(1,5))

    # proceed with searching
    if "//" in queryOrUrl:
      if queryOrUrl.startswith("//"):
        url = 'https:'+queryOrUrl
      else:
        url = queryOrUrl
    else:
      #url = f"https://www.google.com/search?hl=en&q={queryOrUrl}"
      url = f"https://html.duckduckgo.com/html?q={queryOrUrl}"

    htmlData = self.navigate(url)
    soup = BeautifulSoup(htmlData, "html.parser")
    
    # create reference websites
    if not self.saved_urls:
      links = soup.select('a[href*="//"]:not([href*="google"])')
      for link in links:
        unescaped_link = urllib.parse.unquote(link.get("href"), encoding='utf-8', errors='replace')
        if not "?uddg=https://duckduckgo.com" in unescaped_link:
          #self.echo(f"Link saved: {unescaped_link}")
          self.saved_urls.append(unescaped_link)
        else:
          self.echo("Skipped DDG link")

    # follow reference
    if self.search_follow_links and not queryOrUrl in self.saved_urls:
      self.echo(f"Follow links is enabled. Going to one of the search results")
      return self.search(random.choice(self.saved_urls))
    else:
      elems = soup.select("h1, h3, p, .result__body, div[style=\"-webkit-line-clamp:2\"]")
      text = ""
      for elem in elems:
        text += elem.get_text().replace('\n', ' ').replace('\r', '') + ". "

    return text