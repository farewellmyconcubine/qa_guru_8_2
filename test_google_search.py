from selene import browser, be, have

def test_google_search_success():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_google_search_fail():
    browser.element('[name="q"]').should(be.blank).type('rnqo;ghreoqughqruogh48').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print('Поиск ожидаемо не дает результатов')