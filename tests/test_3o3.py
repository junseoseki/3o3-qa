from src.page.loginpage import loginpage
from playwright.sync_api import Page, expect
from src.util.locator import login_locator as L


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
    expect(page.get_by_text("카카오계정 혹은 비밀번호가 일치하지 않습니다. 입력한 내용을 다시 확인해 주세요")).to_be_visible()
