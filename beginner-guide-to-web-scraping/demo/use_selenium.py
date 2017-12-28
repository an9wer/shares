import collections
from selenium import webdriver


def click(element):
    assert hasattr(element, "click")
    element.click()

def display(elements):
    assert isinstance(elements, (collections.Iterable, collections.Iterator))
    for element in elements:
        assert hasattr(element, "text")
        print(element.text)

if __name__ == "__main__":

    # or: driver = webdriver.PhantomJS(executable_path="path/to/phantomjs")
    driver = webdriver.PhantomJS()
    driver.get("http://localhost/source/target-reverse.html")
    fruits = driver.find_elements_by_css_selector("li a")
    button = driver.find_element_by_tag_name("button")

    display(fruits)
    print("-----------------")
    click(button)
    display(fruits)
    print("-----------------")
    click(button)
    display(fruits)
