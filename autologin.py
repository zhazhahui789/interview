from selenium import webdriver
import time
import datetime
import re
import subprocess


def create_repo(name):

    #创建浏览器实体
    driver = webdriver.Firefox(executable_path=r'E:\examples\login_createcodelib\venv\selenium\webdriver\geckodriver-v0.21.0-win64\geckodriver.exe')
    #打开github网站
    driver.get('https://github.com/login')
    #最大化窗口
    driver.maximize_window()
    #输入用户名
    driver.find_element_by_id("login_field").send_keys("zhazhahui789")
    #输入密码
    driver.find_element_by_id("password").send_keys("bb666264")
    #点击登录
    driver.find_element_by_name("commit").click()
    #等待3秒
    time.sleep(3)
    #获取登录后窗口的句柄
    handle = driver.window_handles
    # driver.save_screenshot('1.png')
    #切换窗口
    driver.switch_to.window(handle[-1])
    time.sleep(3)
    #点击创建代码库图标
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/div/div[1]/div/div[1]/h3/a").click()

    handle = driver.window_handles
    driver.switch_to.window(handle[-1])
    driver.find_element_by_id("repository_name").send_keys(name)
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/form/div[3]/button").click()
    handle = driver.window_handles
    driver.switch_to.window(handle[-1])
    """<input id="empty-setup-clone-url" readonly="" spellcheck="false" class="form-control input-sm input-monospace rounded-0 width-full js-git-clone-help-field" value="https://github.com/zhazhahui789/myproject.git" aria-label="Clone URL" type="text">"""
    html = driver.page_source
    https = re.findall('<input id="empty-setup-clone-url".*?(https://github.com/zhazhahui789/.*?git).*?type="text">',html,re.S)
    driver.quit()
    print(https)
    return https[0]
def upload(url):
    date = datetime.datetime.today().isoformat()[0:10]
    init = subprocess.run(["git", "init"])
    gcren = subprocess.run(["git", "config", "--global", "credential.helper", "store"])
    gadd = subprocess.run(["git", "add","." ])
    gcom = subprocess.run(["git", "commit", "-m" + date])
    # grm = subprocess.run(["git","remote","rm","origin"])
    # gremote = subprocess.run(["git", "remote", "add", "origin", url])
    # gpull = subprocess.run(["git","pull","origin","master","--allow-unrelated-histories"])
    gpush = subprocess.run(["git", "push", "-u", "origin", "master"])
def main():
    target_name = input("请输入创建库的名字：")
    target_url = create_repo(target_name)
    upload(target_url)



if __name__ == '__main__':
    main()