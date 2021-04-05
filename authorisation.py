from selenium import webdriver


GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = GOOGLE_CHROME_PATH


def get_marks(information):
    a = information.split(" ")
    if len(a) != 2:
        return "Неправильно введенные данные, для помощи напишите /help"
    else:
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
        driver.implicitly_wait(5)
        try:
            result = ""
            driver.get("https://grade.sfedu.ru/")
            login = driver.find_element_by_id("loginoauth")
            login.send_keys(a[0])
            submit_button = driver.find_element_by_id("signoauthin_b")
            submit_button.click()
            password = driver.find_element_by_id("passwordInput")
            password.send_keys(a[1])
            password_button = driver.find_element_by_id("submitButton")
            password_button.click()
            confirm_button = driver.find_element_by_id("idBtn_Back")
            confirm_button.click()
            subject_list = driver.find_elements_by_css_selector("tr.disciplineRow > td:nth-child(2) > a:nth-child(1)")
            if not subject_list:
                return "Неправильно введенные данные, для помощи напишите /help"
            else:
                pass
            marks_list = driver.find_elements_by_css_selector("tr.disciplineRow > td:nth-child(5) > span:nth-child(1)")
            for i in range(len(subject_list)):
                result += subject_list[i].text + " - " + marks_list[i].text + "\n"
            return result
        finally:
            driver.quit()
            print("Эмулятор закрыт")
