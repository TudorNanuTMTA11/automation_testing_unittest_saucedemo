from selenium import webdriver



class Browser:
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--ignore-certificate-error")
    options.add_argument("--ignore-ssl-errors")
    chrome = webdriver.Chrome(options=options)


    def maximise_windows(self):
        self.chrome.maximize_window()

    def close_browser(self):
        self.chrome.quit()