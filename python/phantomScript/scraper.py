import platform
from bs4 import BeautifulSoup
from selenium import webdriver

# PhantomJS files have different externsions
if platform.system() == 'Windows':
    PHANTOMJS_PATH = './phantomjs.ext'
else:
    PHANTOMJS_PATH = './phantomjs'

# here we use PhantomJS
browser = webdriver.PhantomJS(PHANTOMJS_PATH)
#browser = webdriver.FixreFox()
browser.get('http://www.scoreboard.com/en/tennis/atp-singles/us-open-2015/results/')
#browser.get('https://www.ms88po.com/Main/Sports/mSports.aspx')

soup = BeautifulSoup(browser.page_source, "html.parser")
#games = soup.find_all('tr',{'class': 'stage-finished'})

print(soup.prettify())
