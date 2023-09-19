from selene import browser, be, have

def test_google_search_success(open_browser, setting_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_google_search_fail(open_browser, setting_browser):
    browser.element('[name="q"]').should(be.blank).type('rnqo;ghreoqughqruogh48').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print('Поиск ожидаемо не дает результатов')