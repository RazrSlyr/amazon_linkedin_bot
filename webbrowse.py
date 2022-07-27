# Import the required modules
from ast import expr_context
from regex import B
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
  
# Main Function
if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')
  
    # Provide login info for your linkedin
    email = "Insert your linked in email here"
    password = "Insert your linked in password here"
    message = "Insert the message you would like to send to people when you try to connect with them"
    # Provide the path of chromedriver present on your system.
    driver = webdriver.Chrome(executable_path="./chromedriver.exe",
                              chrome_options=options)
    driver.set_window_size(1920,1080)

    # Go to linkedin
    driver.get('https://www.linkedin.com/login')
    time.sleep(1)

    # log in to linkedin
    driver.find_element(By.ID, 
        "username").send_keys(email)
    driver.find_element(By.ID, 
        "password").send_keys(password)
    driver.find_elements(By.CLASS_NAME, 
        "btn__primary--large")[0].click()

    # start navigating to links
    links_file = open("./links.txt")
    links = [l.strip() for l in links_file.readlines()]
    for l in links:
        time.sleep(5)
        # go to profile
        driver.get(l)
        connect_button = None
        # look for connect button if present
        try:
            connect_button = driver.find_elements(By.CLASS_NAME,
        "artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.pvs-profile-actions__action")[1]
        except:
            # if there is no connect button, go to next profile
            print("No Connect Button")
            continue
        # open connect window
        connect_button.click()
        time.sleep(0.5)

        # open leave a note window
        try:
            note_button = driver.find_elements(By.CLASS_NAME,
            "artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.ember-view.mr1")[0]
            note_button.click()
            time.sleep(0.5)
        except:
            continue

        # leave a note
        driver.find_element(By.ID, "custom-message").send_keys(message)
        # click send
        send_button = driver.find_elements(By.CLASS_NAME,
        "artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.ml1")[0]
        send_button.click()
        time.sleep(0.5)
 
    # Quits the driver
    driver.close()
    driver.quit()