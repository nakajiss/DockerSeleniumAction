import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import allure

@allure.title('Проверка доступности всех страниц кабинета')
@allure.severity(severity_level="critical")

def test_Cabinet_onlinesim ():
    driver = WebDriver(executable_path='/bin/chromedriver')
    driver.set_window_position(0, 0)
    driver.set_window_size(1300, 900)
    action = ActionChains(driver)

    with allure.step("Auth as Tester"):
        driver.get('https://onlinesim.ru/tester_auth?key=gkW_Q_3s3vvCp5Q')
    with allure.step("Check SMS Cabinet page"):
        driver.set_page_load_timeout(10)
        while True:
            try:
                driver.get('https://onlinesim.ru/v2/receive/sms')
            except TimeoutException:
                print
                "Timeout, retrying..."
                continue
            else:
                break
        def CheckTittleSMS (driver):

            tittle = driver.title
            return tittle == "Прием SMS"
        WebDriverWait(driver, 5, 0.5).until(CheckTittleSMS)

    with allure.step("Check Rent Cabinet page"):
        driver.find_element_by_xpath('//i[@class="glyphicon glyphicon-hourglass"]').click()
        def CheckTittleRent (driver):
            tittle = driver.title
            return tittle == "Аренда номера"
        WebDriverWait(driver, 5, 0.5).until(CheckTittleRent)

    with allure.step("Check Proxy Cabinet page"):
        driver.find_element_by_xpath('//i[@class="glyphicon glyphicon-cloud"]').click()
        def CheckTittleProxy(driver):
            tittle = driver.title
            return tittle == "Мобильные прокси"
        WebDriverWait(driver, 5, 0.5).until(CheckTittleProxy)

    with allure.step("Check Cashout Cabinet page"):
        driver.find_element_by_xpath('//i[@class ="glyphicon glyphicon-euro"]').click()
        def CheckTittleCashout(driver):
            tittle = driver.title
            return tittle == "Вывод средств"
        WebDriverWait(driver, 5, 0.5).until(CheckTittleCashout)

    with allure.step("Check Pay Cabinet page"):
        driver.find_element_by_xpath('//i[@class="icon-wallet"]').click()
        def CheckTittlePay(driver):
            tittle = driver.title
            return tittle == "Оплата"
        WebDriverWait(driver, 5, 0.5).until(CheckTittlePay)

    with allure.step("Check Pay Tickets page"):
        driver.find_element_by_xpath('//i[@class="icon-question7"]').click()
        def CheckTittleTickets(driver):
            tittle = driver.title
            return tittle == "Обращения"
        WebDriverWait(driver, 5, 0.5).until(CheckTittleTickets)

    with allure.step("Check Profile Cabinet page"):
        driver.find_element_by_xpath('//i[@class="icon-cog"]').click()
        def CheckTittleProfile(driver):
            tittle = driver.title
            return tittle == "Обращения"
        WebDriverWait(driver, 5, 0.5).until(CheckTittleProfile)
    #Check SMS order
    with allure.step("Count time icons and click order SMS"):
        driver.find_element_by_xpath('//i[@class ="icon-bubbles4"]').click()
        def getCounter():
            counter = len(driver.find_elements_by_xpath('//i[@class="f-ms glyphicon  glyphicon-time"]'))
            return counter
        def CheckElement(driver):
            elements = driver.find_elements_by_xpath('//span[text()="Другие сайты"][@class="service-item-text"]')
            return len(elements) == 1
        WebDriverWait(driver, 5, 0.5).until(CheckElement)
        element = driver.find_element_by_xpath('//span[text()="Другие сайты"]')
        action.move_to_element(element).perform()
        driver.find_element_by_xpath('//button[@class="btn service-buy-btn pull-right btn-c-buy blue"][@style="height: 36px;"]').click()
    with allure.step("Click refresh and check new number"):
        driver.find_element_by_xpath('//button[@class="btn btn-default btn-ref loader-icon"]').click()
        def CheckCounter(driver, counter):
            counterFinal = len(driver.find_elements_by_xpath('//i[@class="f-ms glyphicon  glyphicon-time"]'))
            counterFinal == counter + 1
        getCounter()

    #Check Rent Order
    with allure.step("Count time icons and click order RENT"):
        driver.find_element_by_xpath('//i[@class="glyphicon glyphicon-hourglass"]').click()
        def getCounterRent():
            counter = len(driver.find_elements_by_xpath('//button[@class="btn badge badge-warning font-big"]'))
            return counter
        def CheckElement(driver):
            elements = driver.find_elements_by_xpath('//span[text()="1 день"]')
            return len(elements) == 1
        WebDriverWait(driver, 5, 0.5).until(CheckElement)
        element = driver.find_element_by_xpath('//span[text()="1 день"]')
        action.move_to_element(element).perform()
        driver.find_element_by_xpath('//button[@class="btn service-buy-btn pull-right btn-c-buy blue"][@style=""]').click()
    with allure.step("Check new number"):
        def CheckCounterRent(driver, counter):
            counterFinalRent = len(driver.find_elements_by_xpath('//button[@class="btn badge badge-warning font-big"]'))
            counterFinalRent == counter + 1
        getCounterRent()
        driver.close()








