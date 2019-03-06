from twilio.rest import Client


account_sid = "ac sid"

auth_token = "here is your twilio auth token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="mobile number",
    from_="+1 858-281-4781 ",
    media_url='https://en.facebookbrand.com/wp-content/uploads/2016/05/FB-fLogo-Blue-broadcast-2.png'
    )

print(message.sid)
