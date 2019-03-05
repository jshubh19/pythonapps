from twilio.rest import Client

account_sid = "AC561b21ca46eab7cd51348514510099f1"

auth_token = "aec870ccc4f26e3ea808a46cd289a4fc"

myphone = "+91 8094823877"

TwilioNumber = "+1 858-281-4781 "

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=myphone,
    from_=TwilioNumber,
    body='hey python is here'
)
print (message.sid)
