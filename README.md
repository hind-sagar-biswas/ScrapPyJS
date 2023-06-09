# ScrapPyJS

![Project Language](https://img.shields.io/static/v1?label=language&message=python&color=blue)
![Project Type](https://img.shields.io/static/v1?label=type&message=package&color=red)
[![PyPI project](https://img.shields.io/static/v1?label=PyPI&message=ScrapPyJS&color=blue)](https://pypi.org/project/ScrapPyJS/)
![Current Version](https://img.shields.io/static/v1?label=current-version&message=v1.1.0&color=lightgrey)
![Stable Version](https://img.shields.io/static/v1?label=stable-version&message=v1.1.0&color=brightgreen)
![Maintained](https://img.shields.io/static/v1?label=maintained&message=yes&color=green)
![Ask Me Anything](https://img.shields.io/static/v1?label=ask-me&message=anything&color=green)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

The `ScrapPyJS` class provides functionality for web scraping using Selenium were you can Scrap data via running JS script directly from python.

## Installing

```terminal
pip install ScrapPyJS
```

## How to Use

### Including and Initiating

```python
from ScrapPyJS import ScrapPyJS

# initiate ScrapPyJS
scrappy = ScrapPyJS()

# set js script
JS_SCRIPT = "return 'ScrapPy scrapping!'"
scrappy.set_script(JS_SCRIPT)

# rest of the code goes here...

# close ScrapPyJS
scrappy.end()
```

### Simple way

1. Use the `scrap` method to scrape a webpage:

    ```python
    result = scrappy.scrap(url, wait=True, wait_for='id', wait_target='elementId')
    ```

2. Retrieve the result of the scraping operation:

    ```python
    print(result)
    ```

### Loop through list of URLs

1. Set up a list of target URLs

    ```python
    URLS = [
        'https://url1.com/',
        'https://url2.com/homepage/',
        'https://url2.com/about',
    ]
    ```

2. Use the `loop_through` method to scrape through the target webpages webpage:

    ```python
    # The result value will be a list if save mode is on, else a JSON string
    result = scrappy.scrap(url, wait=True, wait_for='id', wait_target='elementId')
    ```

3. Retrieve the result of the scraping operation:

    ```python
    print(result)
    ```

### Save results to a file

#### Activate save mode

1. Via toggle:

    ```python
    scrappy.toggle_save_mode()
    ```

    Here, the save mode which is set to `False` by Default is toggled to `True`. So the save file informations are default.

2. Via `set_save_info` method:

    ```python
    scrappy.set_save_info(save=True)
    ```

    Here, we directly set save mode to `True` leaving other infos to default.

#### Configure save mode

1. Via `set_save_info` method:

    ```python
    FILE_NAME = "output"
    FILE_FORMAT = "json"
    SAVE_LOCATION = "path/to/file/"

    scrappy.toggle_save_mode(save=True, file_name=FILE_NAME, file_format=FILE_FORMAT, location=SAVE_LOCATION)
    ```

Please note that you will need to have the necessary `Selenium` and `WebDriver` dependencies installed to use this code.

## Documentation

The necessary informations on the ScrapPyJS class is available in `.\CLASS_STRUCTURE.md`

## License

This code has been licensed under `MIT` open source copyleft license.

## Author

**NAME:** *Hind Sagar Biswas*

**Website:** [coderaptors.epizy.com](http://coderaptors.epizy.com/)

[![Author Facebook](https://img.shields.io/static/v1?label=facebook&message=hindsagar.biswas&style=social&logo=facebook)](https://m.facebook.com/hindsagar.biswas)
