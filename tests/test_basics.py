import bonobo_selenium as bbsel


def test_basics():
    assert bbsel.browser
    assert bbsel.torbrowser
