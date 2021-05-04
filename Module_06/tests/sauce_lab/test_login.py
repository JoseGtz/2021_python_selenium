"""Sauce login tests."""
import pytest
from Module_06.src.pages.login import LoginPage
from Module_06.tests.common.test_base import TestBase

LOGIN_DATA = [
    ('standard_user', 'secret_sauce'),
    ('performance_glitch_user', 'secret_sauce'),
    ('problem_user', 'secret_sauce'),
]

ERROR_MSG = 'Epic sadface: Username and password do not match any user in this service'
USER_RQR = 'Epic sadface: Username is required'
LOCKED_MSG = 'Epic sadface: Sorry, this user has been locked out.'


class TestLogin(TestBase):

    @pytest.mark.sanity
    @pytest.mark.login
    @pytest.mark.parametrize('user, password', LOGIN_DATA)
    def test_valid_user(self, user: str, password: str):
        page = LoginPage(self.driver)
        page.open()
        page.login(user, password)

    @pytest.mark.regression
    @pytest.mark.login
    def test_invalid_user(self):
        page = LoginPage(self.driver)
        page.open()
        page.login('standard_user', 'invalid_password')
        error_msg = page.get_error_message()
        assert error_msg is not None, 'Error message should be displayed for invalid login'
        assert error_msg == ERROR_MSG, f'Error message should be {ERROR_MSG}'

    @pytest.mark.regression
    @pytest.mark.login
    def test_no_user(self):
        page = LoginPage(self.driver)
        page.open()
        page.login('', '')
        error_msg = page.get_error_message()
        assert error_msg is not None, 'Error message should be displayed for invalid login'
        assert error_msg == USER_RQR, f'Error message should be {USER_RQR}'

    @pytest.mark.regression
    @pytest.mark.login
    def test_locked_user(self):
        page = LoginPage(self.driver)
        page.open()
        page.login('locked_out_user', 'secret_sauce')
        error_msg = page.get_error_message()
        assert error_msg is not None, "locked message should be displayed for locked account"
        assert error_msg == LOCKED_MSG, f'Error Message should be {LOCKED_MSG}'

    @pytest.mark.regression
    @pytest.mark.login
    def test_logout(self):
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login('standard_user', 'secret_sauce')
        inventory_page.get_menu()
        inventory_page.logout()
        assert page.get_login_btn() is not None, "User was not able to Logout properly"
