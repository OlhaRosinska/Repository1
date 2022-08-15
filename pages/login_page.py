from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    scouts_panel_xpath = "//*[text()='Scouts Panel']"
    remind_password_button_xpath = "//*[text()='Remind password']"
    English_button_xpath = "//*[text()='English']"
    Polski_button_xpath = "//*[text()='Polski']"



    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

