from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scrappy():
    def __init__(self, script=None, browser=None, show=False, debug=False, strict=False):
        """
        Initializes a Scrappy object.

        Parameters:
        - script (str): The JavaScript code to be executed by the web browser.
        - browser (WebDriver): An existing instance of a Selenium WebDriver. [optional - if not provided then creates it's own instan]
        - show (bool): Boolean value indicating whether to show the browser window.
        - debug (bool): Boolean value indicating whether to enable debug mode.
        - strict (bool): Boolean value indicating whether to enable strict mode.
        """
        self.js = script
        self.show = show
        self.debug = debug
        self.strict = strict
        self.browser = browser

        if self.browser is None: self.setup_browser()

    def setup_browser(self):
        """
        Sets up the web browser instance.
        Creates a new instance of a Chrome WebDriver with the specified options.
        """
        chrome_options = Options()
        if not self.show : 
            chrome_options.add_argument("--headless")
        if not self.strict : 
            chrome_options.add_argument("--ssl-protocol=any")
            chrome_options.add_argument("--ignore-ssl-errors=true")
        if not self.debug : 
            chrome_options.add_argument("--log-level=3")
            chrome_options.add_argument("--silent")
        self.browser = webdriver.Chrome(options=chrome_options)

    def set_script(self, script):
        """
        Sets the JavaScript code to be executed by the web browser.

        Parameters:
        - script (str): The JavaScript code to be executed.
        """
        self.js = script

    def scrap(self, url, wait=False, wait_for=None, wait_target=None, wait_time=10):
        """
        Performs web scraping on the specified URL.

        Parameters:
        - url (str): The URL to scrape.
        - wait (bool): Boolean value indicating whether to wait for an element to be present on the page before scraping.
        - wait_for (str): The method to use for locating the element to wait for.
        - wait_target (str): The target value to locate the element to wait for.
        - wait_time (int): The maximum time (in seconds) to wait for the element to be present.

        Returns:
        - result: The result of executing the JavaScript code on the web page.
        """
        if wait_for is None or wait_target is None: wait = False
        else:
            # Mapping wait_for value to corresponding Selenium By method
            match wait_for:
                case 'class':
                    wait_for = By.CLASS_NAME
                case 'id':
                    wait_for = By.ID
                case 'name':
                    wait_for = By.NAME
                case 'tag':
                    wait_for = By.TAG_NAME
                case 'link':
                    wait_for = By.LINK_TEXT
                case 'part_link':
                    wait_for = By.PARTIAL_LINK_TEXT
                case 'css':
                    wait_for = By.CSS_SELECTOR
                case 'xp':
                    wait_for = By.XPATH
        
        self.browser.get(url)

        if wait:
            wait = WebDriverWait(self.browser, wait_time)
            wait.until(EC.presence_of_element_located((wait_for, wait_target)))
            
        try: result = self.browser.execute_script(self.js)
        except: result = False

        return result

    def end(self):
        # Terminates the web browser instance if it exists.
        if self.browser is not None: self.browser.quit()
    