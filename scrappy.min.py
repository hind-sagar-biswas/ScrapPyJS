from selenium import webdriver as E
from selenium.webdriver.chrome.options import Options as F
from selenium.webdriver.common.by import By as B
from selenium.webdriver.support.ui import WebDriverWait as I
from selenium.webdriver.support import expected_conditions as J
D=False
C=None
class Scrappy():
	def __init__(A,script=C,browser=C,show=D,debug=D,strict=D):
		A.js=script;A.show=show;A.debug=debug;A.strict=strict;A.browser=browser
		if A.browser is C:A.setup_browser()
	def setup_browser(B):
		A=F()
		if not B.show:A.add_argument('--headless')
		if not B.strict:A.add_argument('--ssl-protocol=any');A.add_argument('--ignore-ssl-errors=true')
		if not B.debug:A.add_argument('--log-level=3');A.add_argument('--silent')
		B.browser=E.Chrome(options=A)
	def set_script(A,script):A.js=script
	def scrap(E,url,wait=D,wait_for=C,wait_target=C,wait_time=10):
		G=wait_target;F=wait;A=wait_for
		if A is C or G is C:F=D
		else:
			match A:
				case'class':A=B.CLASS_NAME
				case'id':A=B.ID
				case'name':A=B.NAME
				case'tag':A=B.TAG_NAME
				case'link':A=B.LINK_TEXT
				case'part_link':A=B.PARTIAL_LINK_TEXT
				case'css':A=B.CSS_SELECTOR
				case'xp':A=B.XPATH
		E.browser.get(url)
		if F:F=I(E.browser,wait_time);F.until(J.presence_of_element_located((A,G)))
		try:H=E.browser.execute_script(E.js)
		except:H=D
		return H
	def end(A):
		if A.browser is not C:A.browser.quit()