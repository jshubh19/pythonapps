from smtplib import *

content= 'example email stuff here'

mail= smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('shubhj4019@gmail.com','password')

mail.sendmail('shubhj4019@gmail.com','ratan89559@gmail.com','hello ratan')

mail.close()
