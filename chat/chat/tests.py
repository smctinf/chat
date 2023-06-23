# This file is testing if the everybody in the same room receive a message that was sent. More than this, it's trying to test if other people in different room can see a message in another room.
#The code was not implemented yet.
     
from channels.testing import ChannelsLineServerTestCase
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

class ChatTests(ChannelsLiveServerTestCase):
    serve_static = True #This will emulate StaticLiveServerTestCase

    @classmethod 
    def setUpClass(cls):
        super().setUpClass()
        try:
            cls.driver = webdriver.Chmome()
        except:
            super().tearDownClass()
            raise
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_when_chat_message_posted_then_seen_by_everyone_in_same_room(self):
        try:
            self._enter_chat_room('room_1')

            self._open_new_window()
            self._enter_chat_room('room_1')

            self._switch_to_window(0)
            self._post_message('Hello')
            WebDriverWait(self.driver, 2).until(
                lambda _: 'Hello' in self._chat_log_value, 
                'The message was not received by window 1 from window 1'
            )
            self._switch_to_window(1)
            WebDriverWait(self.driver, 2).until(
                lambda _:'Hello' in self._chat_log_value, 
                'The message was not received by window 2 from window 1'
            )
        finally:
            self._close_all_new_windows()

    def test_when_chat_message_posted_then_not_seen_by_anyone_in_different_room(self):
        try:
            self._enter_chat_room('room_1')

            self._open_new_window()
            self._enter_chat_room('room_2')

            self._switch_to_window(0)
            self._post_message('Hello')
            WebDriverWait(self.driver, 2).until(
                lambda _: 'Hello' in self._chat_log_value, 
                'The message was not received by window 1 from window 1'
            )

            self._switch_to_window(1)
            self._post_message('World!')
            WebDriverWait(self.driver, 2).until(
                lambda _: 'World!' in self._chat_log_value, 
                'The message was not received by window 2 from window 2'
            )
            self.assertTrue(
                'Hello' not in self.chat_log_value,
                'Message was improperly received by window 2 from window 1'
            )
        finally:
            self._close_all_new_windows()
    
    #Utility

    def _enter_chat_room(self):
        self.driver.get(self.live_server_url + '/chat/')
        ActionChains(self.driver).send_keys(room_name, Keys.ENTER).perfom()
        WebDriverWait(self.driver, 2).until(
            lambda _: room_name in self.driver.current_url
        )

    def _open_new_window(self):
        self.driver.execute_script('window_open("about:blank", "_blank)')
        self._switch_to_window(-1)

    def _close_all_new_windows(self):
        while len(self.driver.window_handles) > 1:
            self._switch_to_window(-1)
            self.driver.execute_script("window.close();")
        if len(self.driver.window_handles) == 1:
            self._switch_to_window(0)

    def _switch_to_window(self, window_index):
        self.driver.switch_to.window(self.driver.window_handles[window_index])

    def _post_message(self, message):
        ActionChains(self.driver).send_keys(message, Keys.ENTER).perform()

    @property
    def _chat_log_value(self):
        return self.driver.find_element(
            by = By.CSS_SELECTOR, value="#chat-log"
        ).get_property("value")