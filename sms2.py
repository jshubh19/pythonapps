from twilio.rest import Client


account_sid = "AC561b21ca46eab7cd51348514510099f1"

auth_token = "aec870ccc4f26e3ea808a46cd289a4fc"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918094823877",
    from_="+1 858-281-4781 ",
    media_url='https://en.facebookbrand.com/wp-content/uploads/2016/05/FB-fLogo-Blue-broadcast-2.png'
    )

print(message.sid)
