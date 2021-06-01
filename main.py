from selenium import webdriver
import time

PATH = "C:\Dev\chromedriver.exe"
driver = webdriver.Chrome(PATH)

while True:
    # Check BestBuy
    driver.get("https://www.bestbuy.ca/en-ca/product/playstation-5-console/14962185")
    addToCartButton = driver.find_element_by_class_name("addToCartButton")
    if addToCartButton.is_enabled():
        print("BestBuy: PS5 IN STOCK!!!  @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @")
    else:
        print("BestBuy: PS5 not in stock")

    # Check Amazon
    driver.get("https://www.amazon.ca/PlayStation-5-Console/dp/B08GSC5D9G")
    amazon_spans = driver.find_elements_by_tag_name("span")
    amazon_spans = [x.text for x in amazon_spans]
    if "Currently unavailable." in amazon_spans:
        print("Amazon: PS5 not in stock")
    else:
        print("Amazon: PS5 IN STOCK!!!  @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @")
