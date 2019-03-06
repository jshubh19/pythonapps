from twilio.rest import Client

account_sid = ""

auth_token = ""

myphone = "+91 80*********"

TwilioNumber = "+1 **********"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=myphone,
    from_=TwilioNumber,
    body='hey python is here'
)
print (message.sid)
