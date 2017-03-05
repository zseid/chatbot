import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import lib.the_dictionary as TheD
import time
from lib.the_dictionary import check_dict

class FacebookTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_fblogin(self):
        driver = self.driver
        driver.get("http://www.facebook.com")
        self.assertIn("Facebook", driver.title)
        login_email = driver.find_element_by_name('email')
        login_pass = driver.find_element_by_id('pass')
        login_email.send_keys("USERNAME")
        login_pass.send_keys('PASSWORD')
        login_pass.send_keys(Keys.RETURN)
        self.fbinit()
        while True:
            self.cmpmsg()

        def tearDown(self):
            self.driver.close()
            
    def fbinit(self):
        driver = self.driver
        try:
            is_present = EC.presence_of_element_located((By.ID, 'left_nav_section_nodes'))
            WebDriverWait(driver, 5).until(is_present)
            driver.get("https://www.facebook.com/messages/t/CHANGEME") # CHANGE THIS
            chatbox = driver.find_element_by_class_name('_5rpu')
            print("Chat Located.")
        except NoSuchElementException:
            print ("Nothing found.")

    def cmpmsg(self):
        current_time = (time.time() / 60) / 60
        driver = self.driver
        msgbox = driver.find_element_by_class_name('_5rpu')
        # find elements
        last_chatelem = driver.find_elements_by_xpath('.//span[@class = "_3oh- _58nk"]')[-1] # pull the most recent message in the chat
        what_chatelem = driver.find_elements_by_xpath('.//span[@class = "_3oh- _58nk"]')[-2]
        # convert to texts
        whatmsg = what_chatelem.text
        lastmsg = last_chatelem.text # convert the message element to a text & string
        if lastmsg.lower() in TheD.check_dict:
            msgbox.send_keys(TheD.check_dict[lastmsg.lower()])
            msgbox.send_keys(Keys.RETURN)
            print ("\nInput Received:",lastmsg, "At", current_time)
            print ("Respone Sent: ",TheD.check_dict[lastmsg.lower()])
        elif lastmsg.lower() == "what" or lastmsg.lower() == "wat":
            msgbox.send_keys(whatmsg)
            msgbox.send_keys(Keys.RETURN)
            print ("\nWat Received.")
            print("Response sent: ",whatmsg)
        else:
            return

if __name__ == "__main__":
    unittest.main()

