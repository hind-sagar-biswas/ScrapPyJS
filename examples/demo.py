if __name__ == '__main__':
    from ScrapPyJS import ScrapPyJS

    scrappy = ScrapPyJS()
    scrappy.set_script("return 'ScrapPy scrapping!'")
    result = scrappy.scrap('https://github.com/', wait=True, wait_for='tag', wait_target='body')
    scrappy.end()
    print(result)