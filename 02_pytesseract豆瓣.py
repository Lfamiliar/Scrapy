from PIL import Image
import pytesseract
from selenium import webdriver
from lxml import etree
import requests

# 访问网站得到响应
url = "https://www.douban.com/"
driver = webdriver.Chrome()
driver.get(url)

# 把验证码图片下载本地
parseHtml = etree.HTML(driver.page_source)
rList = parseHtml.xpath('')
res = requests.get(rList[0])
res.encoding = "utf-8"
html = res.content
with open("验证码.png","wb") as f:
    f.write(html)
# 把图片-->字符串
image = Image.open("验证码.png")
yzm = pytesseract.image_to_string(image)
# 发送到输入框
driver.find_element_by_XXXX().send_keys(yzm)










