import smtplib
from_addr="from mail"
to_addr="to mail"
messgae="hey message send succesfully"
password='password here'
server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,messgae)
print('success')
server.quit()
