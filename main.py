from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions
import time

# Chrome options to allow the browser to remain open after execution
CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_experimental_option("detach", True)

# Speed thresholds
DOWN_SPEED = "YOUR CONTRACTUAL DOWNLOAD SPEED"  # Minimum expected download speed in Mbps
UP_SPEED = "YOUR CONTRACTUAL UPLOAD SPEED"  # Minimum expected upload speed in Mbps

# Twitter account credentials
TWITTER_EMAIL = "EMAIL FOR TWITTER"
TWITTER_PASSWORD = "TWITTER PASSWORD"
TWITTER_USERNAME = "TWITTER USERNAME"


class Bot:
    def __init__(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(CHROME_OPTIONS)
        self.down = 0  # Variable to store download speed
        self.up = 0  # Variable to store upload speed
        self.post = ''  # Variable to store the post message

    def get_internet_speed(self):
        # Navigate to Speedtest.net
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)  # Wait for the page to load

        # Accept cookies
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

        # Start the speed test
        self.driver.find_element(By.CLASS_NAME, "start-text").click()
        time.sleep(50)  # Wait for the test to complete

        # Retrieve upload and download speeds
        upload = self.driver.find_elements(By.CLASS_NAME, "result-data-large")
        self.up = float(upload[1].text)  # Upload speed
        self.down = float(upload[0].text)  # Download speed

        # Check if the speeds are below the thresholds
        if self.down < DOWN_SPEED or self.up < UP_SPEED:
            # Create a message to post on Twitter
            self.post = f"@JioFiber I am getting broadband speed of {self.down}/{self.up} against the promised speed of {DOWN_SPEED}/{UP_SPEED}"
            self.twitter_post()  # Post the message on Twitter
        else:
            print("Speed matches the promised configurations offered by the provider")

    def twitter_post(self):
        # Navigate to Twitter
        self.driver.get("https://x.com/")
        time.sleep(8)  # Wait for the page to load

        # Click on the tweet button
        self.driver.find_element(By.CSS_SELECTOR,
                                 'button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-2yi16.r-1qi8awa.r-3pj75a'
                                 '.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l').click()
        time.sleep(1)

        # Navigate to the tweet composer
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div['
                                           '3]/div[4]/a/div').click()
        time.sleep(5)

        # Enter email and proceed
        self.driver.find_element(By.NAME, "text").send_keys(TWITTER_EMAIL)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-ywje51.r-184id4b.r'
                                 '-13qz1uu.r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l').click()
        try:
            time.sleep(3)
            # Enter username (if applicable)
            self.driver.find_element(By.NAME, "text").send_keys(TWITTER_USERNAME)
            self.driver.find_element(By.CSS_SELECTOR, "button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r"
                                                      "-19yznuf.r-64el8z.r-1fkl15p.r-1loqt21.r-o7ynqc.r-6416eg.r"
                                                      "-1ny4l3l").click()
        except selenium.common.exceptions.NoSuchElementException:
            pass  # Ignore if the username field is not found
        finally:
            time.sleep(6)
            # Enter password
            self.driver.find_element(By.NAME, "password").send_keys(TWITTER_PASSWORD)

        # Submit login
        self.driver.find_element(By.CSS_SELECTOR, "button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-19yznuf.r"
                                                  "-64el8z.r-1fkl15p.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l").click()
        time.sleep(3)

        # Compose the tweet
        self.driver.find_element(By.CSS_SELECTOR,
                                 'button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-2yi16.r-1qi8awa.r-3pj75a'
                                 '.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l').click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block").send_keys(self.post)
        time.sleep(3)

        # Submit the tweet
        self.driver.find_element(By.CSS_SELECTOR, "button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-1cwvpvk"
                                                  ".r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l").click()


# Instantiate the bot and run the speed test
automated_bot = Bot()
automated_bot.get_internet_speed()

