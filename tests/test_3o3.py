from src.page.loginpage import loginpage
from playwright.sync_api import Page, expect
from src.util.locator import login_locator as L


def test_landing(page: Page):
    expect(page.locator(L.kakao_login_button)).to_be_visible()


def test_login_scenario(page: Page):
    login = loginpage(page)
    login.try_login()
    expect(page.locator(L.id_input)).to_be_visible()
    expect(page.locator(L.password_input)).to_be_visible()
    expect(page.locator(L.login_button)).to_be_visible()
    expect(page.locator(L.qr_login_button)).to_be_visible()


def test_login_negative(page: Page):
    login = loginpage(page)
    login.try_login_with_testid()
    login._wait_for_load_state()
    expect(page.locator(L.close_button)).to_be_visible()
    
