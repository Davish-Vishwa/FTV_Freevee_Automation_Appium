from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as Remote
import requests
import pytest
from time import sleep

class Test_FreeveeFTVAutomation():
    @pytest.fixture
    def Web_data_booting(self):
        Device_Cap = {
            "platformName": "Android",
            "appium:deviceName": "Amazon Fire TV Stick",
            "appium:platformVersion": "9",
            "appium:isRealMobile": True,
            }
        self.idriver = webdriver.Remote("http://localhost:4723/wd/hub", Device_Cap)
        self.idriver.press_keycode(20) # D-PAD DOWN to Unlock

        sleep(2)
        Desired_Cap = {
            "platformName": "Android",
            "appium:deviceName": "Amazon Fire TV Stick",
            "appium:platformVersion": "9",
            "appium:isRealMobile": True,
            "appium:appPackage": "com.amazon.imdb.tv.android.app",
            "appium:appActivity": "com.amazon.imdb.tv.android.app.LandingPageActivity"
		}
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", Desired_Cap)
        self.action = ActionChains(self.driver)
        sleep(5)
        CCAccept = self.driver.find_element(by=By.XPATH, value= '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.Button[1]').click()
        sleep(1)
        MyListEduPrompt = self.driver.find_element(by=By.XPATH, value= '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.Button').click()
        sleep(1)
        yield

    def test_FTV_TC1(self, Web_data_booting):
		
        Navigate = self.driver.press_keycode(21) # D-PAD LEFT
        sleep(1)
        EvokeLeftNav = self.driver.back()
        sleep(1)
        Navigate = self.driver.press_keycode(19) # D-PAD UP
        sleep(2)
        self.driver.press_keycode(23) # D-PAD CENTRE

        sleep(5)
        SSA = self.driver.find_element(by=By.XPATH, value= '//android.widget.TextView[@content-desc="a"]').click()
        SSL = self.driver.find_element(by=By.XPATH, value= '//android.widget.TextView[@content-desc="l"]').click()
        SSE = self.driver.find_element(by=By.XPATH, value= '//android.widget.TextView[@content-desc="e"]').click()
        SSX = self.driver.find_element(by=By.XPATH, value= '//android.widget.TextView[@content-desc="x"]').click()

        sleep(2)
		# Move to Search Inline Suggestion
        self.driver.press_keycode(22) # D-PAD Right
        self.driver.press_keycode(22) # D-PAD Right
        self.driver.press_keycode(22) # D-PAD Right
        self.driver.press_keycode(22) # D-PAD Right
        self.driver.press_keycode(22) # D-PAD Right
        self.driver.press_keycode(22) # D-PAD Right
        self.driver.press_keycode(22) # D-PAD Right

        self.driver.press_keycode(23) # D-PAD CENTRE
        sleep(5)
        self.driver.press_keycode(23) # D-PAD CENTRE
        sleep(30)

        self.driver.press_keycode(85) # Play/Pause
        sleep(20)

        self.driver.back()
        self.driver.back()
        self.driver.back()
        self.driver.back()
        self.driver.back()


        self.driver.press_keycode(20) # D-PAD DOWN
        self.driver.press_keycode(20) # D-PAD DOWN
        self.driver.press_keycode(20) # D-PAD DOWN
        self.driver.press_keycode(20) # D-PAD DOWN

        self.driver.press_keycode(23) # D-PAD CENTRE

        print("FTV_TC1 Passed")