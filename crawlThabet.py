from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



# Kết nối Service
service = Service("D:\Python\Selenium\msedgedriver.exe")
option = webdriver.EdgeOptions()
browser = webdriver.Chrome(service=service, options=option)

# Truy cập Web
browser.get("https://www.tjb15.net/index.aspx")
sleep(2)

# Login
txtUser = browser.find_element(by=By.ID, value="txtUser")
txtUser.send_keys("0862200944")
sleep(2)

txtPass = browser.find_element(by=By.ID, value="txtPassword")
txtPass.send_keys("longnam1")
sleep(1)
txtPass.send_keys(Keys.ENTER)
sleep(3)

# Chọn chơi xổ số
txtXoso = browser.find_element(by=By.CLASS_NAME, value="btn_colorBanner")
txtXoso.click()
sleep(2)

txtXoso2 = browser.find_element(by=By.ID, value="aColor")
txtXoso2.click()
sleep(3)

# Xử lý iframe vào click vào trò chơi
browser.switch_to.frame(0)
browser.find_element(by=By.XPATH, value="/html/body/form/div[3]/div[2]/div[4]/div[1]").click()
sleep(2)

# Xử lý popUp và click vào xem kết quả
handles = []
handles = browser.window_handles
browser.switch_to.window(handles[1])
sleep(7)
browser.find_element(by=By.XPATH, value="/html/body/form/div[8]/div[1]/div/ul/li[2]/a").click()
browser.close()
sleep(3)

# Xử lý popUp và click chọn xem 18 lô tô bét
handles = browser.window_handles
browser.switch_to.window(handles[1])
sleep(3)
browser.find_element(by=By.ID, value="divLeftMenu_221").click()
sleep(3)

# Click tìm kiếm lấy đầy đủ các kỳ trong ngày
browser.find_element(by=By.ID, value="pnSearch").click()
sleep(2)
browser.find_element(by=By.ID, value="btnPpSearch").click()
thoiGian = browser.find_element(by=By.CLASS_NAME, value="res_date") # Lấy thêm thông tin thời gian (ngày tháng)
sleep(10)

# Lấy danh sách các kỳ
list_Ky = browser.find_elements(by=By.CLASS_NAME, value="vnLitemBox")

# Mở file dataThabet để ghi giải đặc biệt lại
toDay = thoiGian.text.split(" ") # Tách lấy ngày
ghi = open("D:/Ku/2.0/2.10/duLieuThaBet/" + toDay[0] + ".txt", 'w')
# lặp trong tất cả các kỳ
dem = 0
for ky in list_Ky:
    dem += 1
    if dem > 101:
        break # chỉ lấy 100 giải gần nhất để training model
    else:
        soKy = ky.find_element(by=By.CLASS_NAME, value="res_item")
        dacBiet = ky.find_element(by=By.CLASS_NAME, value="drawResults")
        #print("Số kỳ: ", soKy.text, " | ", dacBiet.text)
        ghi.write(str(dacBiet.text) + "\n")

browser.close()
ghi.close()



