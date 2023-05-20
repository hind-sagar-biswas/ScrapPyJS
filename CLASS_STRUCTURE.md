# ScrapPyJS Class Structure

## Constructor

`ScrapPyJS.__init__(script=None, browser=None, show=False, debug=False, strict=False)`

The constructor initializes a `ScrapPyJS` object with the following parameters:

- `script` (optional): The JavaScript code to be executed by the web browser.
- `browser` (optional): An existing instance of a Selenium WebDriver. If not provided, a new instance will be created using Chrome.
- `show` (optional): Boolean value indicating whether to show the browser window. *Default => `False`.*
- `debug` (optional): Boolean value indicating whether to enable debug mode. *Default => `False`.*
- `strict` (optional): Boolean value indicating whether to enable strict mode. *Default => `False`.*

## Properties

- `save`: Boolean value indicating whether to enable save mode. *Value is `False`*.
- `save_file`: File name for the output file. *Value is `"scrape-result-$t"`*.
- `save_file_format`: File format of the output file. *Value is `"txt"`*.
- `save_file_location`: Location of the output file. *Value is `"./"`*.

## Methods

### Required methods

`ScrapPyJS.setup_browser()`

This method sets up the web browser instance. It creates a new instance of a Chrome WebDriver with the specified options based on the constructor parameters.

`ScrapPyJS.set_script(script)`

This method sets the JavaScript code to be executed by the web browser.

- `script`: The JavaScript code to be executed.

`ScrapPyJS.scrap(url, wait=False, wait_for=None, wait_target=None, wait_time=10)`

This method performs web scraping on the specified URL.

- `url`: The URL to scrape.
- `wait` (optional): Boolean value indicating whether to wait for an element to be present on the page before scraping. *Default => `False`.*
- `wait_for` (optional): The method to use for locating the element to wait for. Possible values are `'class'`, `'id'`, `'name'`, `'tag'`, `'link'`, `'part_link'`, `'css'`, or `'xp'`. *Default => `None`.*
- `wait_target` (optional): The target value to locate the element to wait for. *Default => `None`.*
- `wait_time` (optional): The maximum time (in seconds) to wait for the element to be present. *Default => `10`.*

Returns the result of executing the JavaScript code on the web page.

`ScrapPyJS.loop_through(url_list, wait=False, wait_for=None, wait_target=None, wait_time=10)`

This method performs web scraping on all URL list.

- `url_list`: The URL targets to scrape.
- `wait` (optional): Boolean value indicating whether to wait for an element to be present on the page before scraping. *Default => `False`.*
- `wait_for` (optional): The method to use for locating the element to wait for. Possible values are `'class'`, `'id'`, `'name'`, `'tag'`, `'link'`, `'part_link'`, `'css'`, or `'xp'`. *Default => `None`.*
- `wait_target` (optional): The target value to locate the element to wait for. *Default => `None`.*
- `wait_time` (optional): The maximum time (in seconds) to wait for the element to be present. *Default => `10`.*

Returns the result of executing the JavaScript code on all the urls as a list.

`ScrapPyJS.end()`

This method terminates the web browser instance if it exists.

### Optional Methods

`ScrapPyJS.toggle_save_mode()`

This method toggles the save mode [Default mode: False]

`ScrapPyJS.set_save_info(save=False, file_name="scrape-result-$t", file_format="json", location=".")`

This method updates/sets save file/location informations along with save mode.

- `save`: Boolean value indicating whether to enable save mode. *Default => `False`*.
- `save_file`: File name for the output file. *Default => `"scrape-result-$t"`*.
- `save_file_format`: File format of the output file. *Default => `"txt"`*.
- `save_file_location`: Location of the output file. *Default => `"./"`*.
