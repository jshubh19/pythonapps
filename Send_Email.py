from smtplib import *

content= 'example email stuff here'

mail= smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('abc@mail.com','password')

mail.sendmail('abc@mail.com','bcd@gmail.com','hello ratan')

mail.close()
