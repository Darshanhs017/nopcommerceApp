from selenium import webdriver
import pytest
@pytest.fixture()
def setup(request):
    driver=webdriver.Chrome()
    return driver

