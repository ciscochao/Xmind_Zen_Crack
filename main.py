# coding=utf-8
"""
# @Time    : 8/22/19 4:47 PM
# @Author  : F0rGeEk@root
# @Email   : bat250@protonmail.com
# @File    : main.py
# @Software: PyCharm
***********************************************************
███████╗ ██████╗ ██████╗  ██████╗ ███████╗███████╗██╗  ██╗
██╔════╝██╔═████╗██╔══██╗██╔════╝ ██╔════╝██╔════╝██║ ██╔╝
█████╗  ██║██╔██║██████╔╝██║  ███╗█████╗  █████╗  █████╔╝ 
██╔══╝  ████╔╝██║██╔══██╗██║   ██║██╔══╝  ██╔══╝  ██╔═██╗ 
██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗███████╗██║  ██╗
╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
***********************************************************
"""
import os
import time
import platform
import crack

# 通过操作系统判断需要破解文件的路径
app_out_dir = ""
if platform.system().lower() == "darwin":
    app_out_dir = "./XMind ZEN.app/Contents/Resources/app/out/"
else:
    app_out_dir = "./resources/app/out/"

# 需要破解的文件及文件路径
active = os.path.join(app_out_dir, "modal-activateAlert.js")
pdf = os.path.join(app_out_dir, "imgs/pdf-footer-zh-CN.svg")
png = os.path.join(app_out_dir, "imgs/png-watermark-zh-CN.svg")
pri = os.path.join(app_out_dir, "imgs/print-watermark-zh-CN.svg")
new_css = os.path.join(app_out_dir, "new.css")
render_css = os.path.join(app_out_dir, "renderer.css")

# 填充CSS所需代码
add_css = "\n  display: none !important;"
k_word = ".evaluation-text {"
new_code = 'viewBox="0 0 0 0"'

# 破解过程
print('===========开始破解============')
start_time = time.time()
step1 = crack.Crack(active)
step1.del_all()
print('------试用版 请激活按钮已取消！')
step2 = crack.Crack(new_css)
step2.replace_str(k_word, add_css)
step3 = crack.Crack(render_css)
step3.replace_str(k_word, add_css)
step4 = crack.Crack(pri)
step4.replace_str('viewBox="0 0 514 454"', new_code)
step5 = crack.Crack(pdf)
step5.replace_str('viewBox="0 0 263 20"', new_code)
print('------导出PDF文件中水印已取消！')
step6 = crack.Crack(png)
step6.replace_str('viewBox="0 0 190 80"', new_code)
print('------导出PNG文件中水印已取消！')
end_time = time.time()
print("破解用时 %s 秒" % (round(end_time - start_time, 3)))
print('------感谢您的使用！By 【F0rGeEk】')
