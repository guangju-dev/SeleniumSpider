from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# website = 'http://sso.hnlat.com/'
#username为登录网站的用户名
#password为登录网站的密码
#brower_location为driver.exe的具体位置（每个浏览器的driver都不一样）
#website是爬取的网站
#key是要搜索的文章标题
def finddoi(username,password,brower_loaction,key,website):
    browser = webdriver.Edge(brower_loaction)
    browser.get(website)
    #登录网站
    wait = WebDriverWait(browser, 5,0.5)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='username']")))
    username_input = browser.find_element_by_xpath("//input[@id='username']")
    username_input.send_keys(username)
    password_input = browser.find_element_by_xpath("//input[@id='password']")
    password_input.send_keys(password)
    browser.find_element_by_id('base_login_btn').click()
    #搜索关键字
    wait_1 = WebDriverWait(browser, 5, 0.5)
    wait_1.until(EC.presence_of_element_located((By.ID, "easy-input")))
    browser.find_element_by_id('easy-input').send_keys(key)
    browser.find_element_by_xpath("//button[@name = 'val']").click()
    #找到搜索结果里第一个文章并点击
    wait_2 = WebDriverWait(browser, 5, 0.5)
    wait_2.until(EC.presence_of_element_located((By.XPATH, '//a[@class="title"]')))
    lists = browser.find_elements_by_xpath('//a[@class="title"]')
    lists[0].click()
    browser.close()
    #切换到第二个标签页
    handles = browser.window_handles
    browser.switch_to.window(handles[-1])
    #找到该页面中的doi并返回
    wait_3 = WebDriverWait(browser, 5, 0.5)
    wait_3.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'doi')]")))
    doi = browser.find_element_by_xpath("//a[contains(text(),'doi')]")
    # print(doi.text)
    return doi.text
