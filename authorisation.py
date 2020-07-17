from selenium import webdriver
import time

path = 'geckodriver.exe'
opt = webdriver.FirefoxOptions()
opt.headless = True
driver = webdriver.Firefox(executable_path=path, options=opt)


def get_marks(username, passw):
    try:
        result = ""
        driver.get("https://grade.sfedu.ru/")
        login = driver.find_element_by_id("loginopenid")
        login.send_keys(username)
        submit_button = driver.find_element_by_id("signopenidin_b")
        submit_button.click()
        time.sleep(2)
        password = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/table/tbody/tr[1]/td/input")
        password.send_keys(passw)
        password_button = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/table/tbody/tr[2]/td/input[1]")
        password_button.click()
        time.sleep(2)
        subject_list = driver.find_elements_by_css_selector("tr.disciplineRow > td:nth-child(2) > a:nth-child(1)")
        if not subject_list:
            return "Неправильно введенные данные"
        else:
            pass
        marks_list = driver.find_elements_by_css_selector("tr.disciplineRow > td:nth-child(5) > span:nth-child(1)")
        for i in range(len(subject_list)):
            result += subject_list[i].text + " - " + marks_list[i].text + ", "
        return result
    finally:
        driver.quit()
        print("Эмулятор закрыт")
