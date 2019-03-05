import smtplib
from_addr="shubhj4019@gmail.com"
to_addr="jshubh019@gmail.com"
messgae="hey message send succesfully"
password='Shubhamgmail121'
server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,messgae)
print('success')
server.quit()
