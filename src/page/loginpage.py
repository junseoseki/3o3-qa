import os
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
        self._get_locator(login_locator.id_input).fill(os.getenv("ID"))
        self._get_locator(login_locator.password_input).fill(os.getenv("PASSWORD"))
        self._get_locator(login_locator.login_button).click()
        self._wait_for_load_state()
        
        # Verify login success by checking we are not on the login page anymore
        # or waiting for a key element of the main app.
        try:
            # Wait for URL to change to the main app domain
            self.page.wait_for_url("**/app.3o3.co.kr/**", timeout=15000)
            logging.info("로그인 성공: 메인 도메인 진입 확인")
        except Exception as e:
            curr_url = self.page.url
            logging.error(f"로그인 후 리다이렉트 실패. 현재 URL: {curr_url}")
            raise Exception(f"Login Verification Failed: Stucked at {curr_url}") from e