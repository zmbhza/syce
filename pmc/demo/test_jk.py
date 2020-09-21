import xlrd
from email.mime.text import MIMEText
import smtplib
msg = MIMEText('hell1o')
msg["Subject"] = 'cao'
msg['From'] = '847160625@qq.com'
msg['To'] = 'zhaodongshuai@zhaolaobao.com'
fron_addr = '847160625@qq.com'
pwd = 'bkvqmglgvrblbcai'
smtp_server = 'smtp.qq.com'
to_addr = 'zhaodongshuai@zhaolaobao.com'
try:
    server = smtplib.SMTP_SSL(smtp_server,465,timeout=2)
    server.login(fron_addr,pwd)
    server.sendmail(fron_addr,[to_addr],msg.as_string())
    server.quit()
    print('ok')
except Exception as e:
    print('Faild:%s' % e)