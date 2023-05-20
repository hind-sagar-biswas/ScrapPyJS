# ScrapPyJS Class

The `ScrapPyJS` class provides functionality for web scraping using Selenium were you can Scrap data via running JS script directly from python.

## Installing

```terminal
pip install ScrapPyJS
```

## Constructor

`__init__(script=None, browser=None, show=False, debug=False, strict=False)`

The constructor initializes a `ScrapPyJS` object with the following parameters:

- `script` (optional): The JavaScript code to be executed by the web browser.
- `browser` (optional): An existing instance of a Selenium WebDriver. If not provided, a new instance will be created using Chrome.
- `show` (optional): Boolean value indicating whether to show the browser window. Default is `False`.
- `debug` (optional): Boolean value indicating whether to enable debug mode. Default is `False`.
- `strict` (optional): Boolean value indicating whether to enable strict mode. Default is `False`.

## Methods

`ScrapPyJS.setup_browser()`

This method sets up the web browser instance. It creates a new instance of a Chrome WebDriver with the specified options based on the constructor parameters.

`ScrapPyJS.set_script(script)`

This method sets the JavaScript code to be executed by the web browser.

- `script`: The JavaScript code to be executed.

`ScrapPyJS.scrap(url, wait=False, wait_for=None, wait_target=None, wait_time=10)`

This method performs web scraping on the specified URL.

- `url`: The URL to scrape.
- `wait` (optional): Boolean value indicating whether to wait for an element to be present on the page before scraping. Default is `False`.
- `wait_for` (optional): The method to use for locating the element to wait for. Possible values are `'class'`, `'id'`, `'name'`, `'tag'`, `'link'`, `'part_link'`, `'css'`, or `'xp'`. Default is `None`.
- `wait_target` (optional): The target value to locate the element to wait for. Default is `None`.
- `wait_time` (optional): The maximum time (in seconds) to wait for the element to be present. Default is `10`.

Returns the result of executing the JavaScript code on the web page.

`ScrapPyJS.end()`

This method terminates the web browser instance if it exists.

## How to Use

1. Import the ScrapPyJS:

    ```python
    from ScrapPy import ScrapPy
    ```

2. Create an instance of the ScrapPyJS class:

    ```python
    scrappy = ScrapPyJS()
    ```

3. Set JS script as string to return a value from the website

    ```python
    scrappy.set_script("return 'ScrapPy scrapping!'")
    ```

4. Use the scrap method to scrape a webpage:

    ```python
    result = scrappy.scrap(url, wait=True, wait_for='id', wait_target='elementId')
    ```

5. Retrieve the result of the scraping operation:

    ```python
    print(result)
    ```

6. Terminate the web browser instance when finished:

    ```python
    scrappy.end()
    ```

Please note that you will need to have the necessary `Selenium` and `WebDriver` dependencies installed to use this code.
