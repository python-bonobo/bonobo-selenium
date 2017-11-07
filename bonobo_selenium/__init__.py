import selenium.webdriver

from bonobo_selenium._version import __version__

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4'


def create_profile(use_tor=False):
    _profile = selenium.webdriver.FirefoxProfile()
    _profile.set_preference("toolkit.startup.max_resumed_crashes", "-1")

    if use_tor:
        # tor connection
        _profile.set_preference('network.proxy.type', 1)
        _profile.set_preference('network.proxy.socks', '127.0.0.1')
        _profile.set_preference('network.proxy.socks_port', 9050)

    # user agent
    _profile.set_preference("general.useragent.override", USER_AGENT)

    return _profile


def create_browser(profile):
    _browser = selenium.webdriver.Firefox(profile)
    # _browser.implicitly_wait(10)
    # _browser.set_page_load_timeout(10)
    return _browser

def create_chrome_browser():
    browser = selenium.webdriver.Chrome()
    return browser


__all__ = [
    'USER_AGENT',
    '__version__',
    'create_browser',
    'create_profile',
]
