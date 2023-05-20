import json
import logging
import datetime
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ScrapPyJS():
    def __init__(self, script=None, browser=None, show=False, debug=False, strict=False) -> None:
        """
        Initializes a ScrapPy object.

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

        self.save = False
        self.save_file = "scrape-result-$t"
        self.save_file_format = "json"
        self.save_file_location = "./"

        if self.debug: logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        if self.browser is None: self.setup_browser()

    def setup_browser(self) -> None:
        # Sets up the web browser instance.
        # Creates a new instance of a Chrome WebDriver with the specified options.
        
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

    def toggle_save_mode(self):
        # toggles save mode
        self.save = not self.save

    def set_save_info(self, save=False, file_name="scrape-result-$t", file_format="json", location=".") -> None:
        """
        Change save informations.

        Parameters:
        - save (bool): status for save mode.
        - file_name (str): file name for the output file [$t => current time as HHmmss format].
        - file_format (str): file format of the output file.
        - location (str): location of save mode.
        """
        self.save = save
        self.save_file = file_name
        self.save_file_format = file_format
        self.save_file_location = location

    def set_script(self, script) -> None:
        """
        Sets the JavaScript code to be executed by the web browser.

        Parameters:
        - script (str): The JavaScript code to be executed.
        """
        self.js = script

    def save_to_file(self, data):
        # Saves data to file.
        if not isinstance(data, str):
            # Convert non-string data to JSON string
            data = json.dumps(data)

        current_time = datetime.datetime.now().strftime("%H%M%S")
        filename = self.save_file.replace("$t", current_time)
        file_path = f"{self.save_file_location}/{filename}.{self.save_file_format}"

        return_val = data

        try:
            with open(file_path, 'w', encoding='utf-8') as outfile:
                outfile.write(data)
        except Exception:
            logging.error("Failed to write to File")

        return return_val
    
    def get_by_value(self, wait_for):
        # Mapping wait_for value to corresponding Selenium By method
        match wait_for:
            case 'class': return By.CLASS_NAME
            case 'id': return By.ID
            case 'name': return By.NAME
            case 'tag': return By.TAG_NAME
            case 'link': return By.LINK_TEXT
            case 'part_link': return By.PARTIAL_LINK_TEXT
            case 'css': return By.CSS_SELECTOR
            case 'xp': return By.XPATH
            case _: return None

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
        wait_for = self.get_by_value(wait_for)
        if wait_for is None or wait_target is None: wait = False

        self.browser.get(url)

        if wait:
            wait = WebDriverWait(self.browser, wait_time)
            wait.until(EC.presence_of_element_located((wait_for, wait_target)))

        try: result = self.browser.execute_script(self.js)
        except Exception: result = False

        return self.save_to_file(result) if self.save else result
    
    def loop_through(self, url_list, wait=False, wait_for=None, wait_target=None, wait_time=10):
        """
        Performs web scraping on the specified URL list.

        Parameters:
        - url (list): The URL lists to scrape.
        - rest are same as scrape

        Returns:
        - result: A list of the results of executing the JavaScript code on the URLs.
        """
        if not isinstance(url_list, list):
            logging.error("Expected url_list = list() for ScrapPyJS.loop_through()")
            return False
        results = []

        # store the save mode and set save mode to False
        save = self.save
        self.set_save_info(save=False)

        for url in tqdm(url_list):
            result = self.scrap(url, wait, wait_for, wait_target, wait_time)
            results.append(result)

        # reset the save mode 
        self.set_save_info(save=save)

        return self.save_to_file(results) if self.save else results

    def end(self) -> None:
        # Terminates the web browser instance if it exists.
        if self.browser is not None: self.browser.quit()

    def __str__(self) -> str:
        return "ScrapPyJS Object"
    