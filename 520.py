# -*- coding: utf-8 -*-


import qrcode
import webbrowser

# 生成二维码
data = "https://acuteboy0.github.io/"
img = qrcode.make(data)

# 保存二维码图片
img.save("my_qrcode.png")

# 显示二维码图片
img.show()

# 打开浏览器扫描二维码
webbrowser.open("my_qrcode.png")


