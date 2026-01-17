import logging
from src.page.basepage import basepage
from src.util.locator import login_locator
from dotenv import load_dotenv

load_dotenv()

class loginpage(basepage):
    def __init__(self, page, timeout=9000):
        super().__init__(page, timeout)
    
    def try_login(self):
        self._get_locator(login_locator.kakao_login_button).click()
        logging.info("로그인 페이지 진입 완료")
        