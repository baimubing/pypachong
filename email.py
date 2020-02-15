import smtplib

from email.mime.text import MIMEText

from_addr = 'xxxxx@qq.com'
#要发送的邮箱
password = '----------------'
#你的授权码数字
smtp_server = 'smtp.qq.com'
# 发信服务器
to_addr = '-----------------@qq.com'
# 收信方邮箱
msg = MIMEText('send by python','plain','utf-8')

server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 465)
# 开启发信服务，这里使用的是加密传输
server.login(from_addr, password) 
# 登录发信邮箱



server.sendmail(from_addr, to_addr, msg.as_string()) 
# 发送邮件
server.quit() 
# 关闭服务器
