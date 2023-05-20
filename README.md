# ScrapPyJS Class

The `ScrapPyJS` class provides functionality for web scraping using Selenium were you can Scrap data via running JS script directly from python.

## Installing

```terminal
pip install ScrapPyJS
```

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
