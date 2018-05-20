import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver = "smtp.qq.com"
user = "39225102@qq.com"
password = "fmtnopnboeohbhbd"
sender = "39225102@qq.com"
receiver = "115258938@qq.com"
subject = "Python email test"
msg = MIMEText("<html><h1>你好！</h1></html>", "html", "utf-8")
msg[subject] = Header(subject, "utf-8")

smtp = smtplib.SMTP_SSL()
smtp.connect(smtpserver, 465)
print("正在连接")
smtp.login(user, password)
print("登录中")
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()