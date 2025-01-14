from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants
INDEX_SEL = "input#indexno"
DOB_SEL = "input#dob[type='date']"
DOB = "07/01/2004" 
DOB_2 = "09/07/2006"
DOBS = ["07/01/2004", "09/07/2006", "17/07/2005"]
# Use ISO format (yyyy-mm-dd) for type="date" inputs
URL = "https://bcsea.site/result2021"

def init():
    """Initialize the Selenium WebDriver and open the target URL."""
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1080,1024")

    # Provide the path to ChromeDriver
    service = Service("chromedriver.exe")  # Replace with the actual path to your ChromeDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(URL)
    print(f"Page URL: {driver.current_url}")

    return driver

def get_right_index(driver, idx_no, dob_):
    """Fill in the form, submit it, and check for results."""
    try:
        # Wait for the index number input to appear
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, INDEX_SEL)))
        
        # Locate the inputs
        index_input = driver.find_element(By.CSS_SELECTOR, INDEX_SEL)
        dob_input = driver.find_element(By.CSS_SELECTOR, DOB_SEL)
        
        print("Input fields appeared")

        # Fill out the inputs
        index_input.send_keys(str(idx_no))
        dob_input.send_keys(dob_)
        print("Date Filled")

        # Click the submit button
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        print("Submitted")

        # Wait for the results table to appear
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#myTable")))
        print(f"------------------------Result table found! for index {idx_no}")
        return idx_no
    except Exception as e:
        print(f"Result table not found for index {idx_no}")

        return "Wrong"

def main():
    """Main function to iterate through index numbers until the correct one is found."""
    
    run = True
    ind = 12241400430  # Starting index number 589

    while run:
        driver = init()
        val = get_right_index(driver, f"0{ind}", DOB)
        
        if val != "Wrong":
            print(f"Correct Index Found: {val}")
            run = False
        else:
            ind += 1 
            driver.close()# Increment the index number

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
    # 552 - Same DOB but diff person
    # 
    # Start with 430 - 530
    # 553 to 567 to 601 no result
