#coding=utf-8
'''
@author: Administrator
'''
from splinter.browser import Browser

    
b=Browser(driver_name="chrome")

url="https://kyfw.12306.cn/otn/leftTicket/init"
    
b.visit(url)

b.find_by_text(u"登录").click()

b.fill("loginUserDTO.user_name","lf8509")

b.fill("userDTO.password","lf850913")



print(b.cookies.all())


b.cookies.add({"_jc_save_fromStation":"%u5E7F%u5DDE%2CGZQ"})
b.cookies.add({"_jc_save_toStation":"%u957F%u6C99%2CCSQ"})
b.cookies.add({"_jc_save_fromDate":"2016-01-18"})

b.cookies.all()


b.reload()


b.find_by_text(u'查询').click()