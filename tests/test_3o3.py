from src.page.loginpage import loginpage
from playwright.sync_api import expect
from src.util.locator import login_locator as L

def test_login_scenario(page):
    login = loginpage(page)
    login.try_login()
    expect(page.locator(L.id_input)).to_be_visible()
    expect(page.locator(L.password_input)).to_be_visible()
    expect(page.locator(L.login_button)).to_be_visible()
    expect(page.locator(L.qr_login_button)).to_be_visible()
    
