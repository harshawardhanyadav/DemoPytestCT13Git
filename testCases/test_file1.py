import time
from operator import truediv

import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

class Test_py:

    @pytest.mark.sanity
    def test_sum_001(self):
        a = 3
        b = 5
        sum = a + b
        print(sum)
        if sum == 8:
            print("test sum 001 is passed")
            assert True

        else:
            print("test sum 001 is failed")
            assert False

    @pytest.mark.sanity
    def test_mul_002(self):
        a = 3
        b = 5
        mul = a * b
        print(mul)
        if mul == 15:
            print("Test_mul_002 is passed ")
            assert True


        else:
            print("Test_mul_002 is failed ")
            assert False

    @pytest.mark.skip
    def test_sum_003(self):
        a = 3
        b = 5
        sum = a + b
        print(sum)
        if sum == 16:
            print("test_sum_003 is passed")
            assert True

        else:
            print("test_sum_003 is failed")
            assert False

    @pytest.mark.sanity
    def test_Google(self):
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.chrome(options=chrome_options)
        driver.get("https://www.google.com/")
        logo = driver.find_element(By.CLASS_NAME,"lnXdpd").is_displayed()
        print(logo)
        if logo == True:
            driver.close()
            assert True     # test Case status is passed
        else:
            driver.close()
            assert False    # test case status is failed





