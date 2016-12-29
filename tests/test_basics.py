import bonobo_selenium


def test_basics():
    assert bonobo_selenium.browser
    assert bonobo_selenium.torbrowser
