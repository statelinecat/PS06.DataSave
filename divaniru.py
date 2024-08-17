from selenium import webdriver
import time
import pandas as pd

# Path to your WebDriver executable

browser = webdriver.Firefox()

# Open the webpage
url = 'https://www.divan.ru/category/divany-i-kresla'
browser.get(url)
time.sleep(5)  # Wait for the page to load

products = []
product_elements = browser.find_elements_by_class_name('_Ud0k U4KZV')  # Adjust selector based on actual structure

for product in product_elements:
    name_element = product.find_element_by_class_name('product-name')
    price_element = product.find_element_by_class_name('price')
    link_element = product.find_element_by_class_name('ui-GPFV8')

    products.append({
        'название': name_element.text,
        'цена': price_element.text,
        'ссылка на товар': link_element.get_attribute('href')
    })

df = pd.DataFrame(products)
df.to_csv('products.csv', index=False, encoding='utf-8')

browser.quit()
