# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://jdsports.ca")
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox")
search_bar = driver.find_element("name","q")
search_bar.send_keys("nike")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "nike" in driver.title

add_to_cart_button = driver.find_element("xpath", "/html/body/main/div/div/div/div[2]/div[5]/div/div[1]/div");
# add_to_cart_button = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
add_to_cart_button.click()

time.sleep(5)

two_add_to_cart_button = driver.find_element("xpath", "/html/body/main/div/section/div/div[1]/form/div[1]/div/div[3]/label");
# add_to_cart_button = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
two_add_to_cart_button.click()

time.sleep(5)

three_add_to_cart_button = driver.find_element("xpath", "/html/body/main/div/section/div/div[1]/form/div[2]/div/div[12]/label");
# add_to_cart_button = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
three_add_to_cart_button.click()


# Selecting a laptop from the search results
# laptop_link = driver.find_element_by_css_selector("span[data-component-type='s-product-image'] a")
#shoes_link = driver.find_element("xpath","///*[@id="algolia-hits"]/div/div[1]/div");
# laptop_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
#shoes_link.click()


# Waiting for the laptop details page to load
time.sleep(5)

# Verifying that the correct laptop details page has loaded
# assert "laptop" in driver.title

# Adding the laptop to the cart


# Waiting for the cart to update


# Clicking on no thanks button
no_thanks_button= driver.find_element("xpath","/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div/div")
no_thanks_button.click()
time.sleep(2)

# Verifying that the laptop has been added to the cart
cart_count = driver.find_element("id","nav-cart-count")
assert cart_count.text == "1"

# Closing the webdriver
driver.close()
