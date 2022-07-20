from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACfc5368cac59784efecd547fd4b864ab5"
# Your Auth Token from twilio.com/console
auth_token  = "abfb922693a4f8bb4ad4f40b1357da77"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15167252741", 
    from_="+18454090492",
    body="hey tall basketball man lol, i see you at Middle School 132 America's School of Heroes working as a camp counselor lol")

print(message.sid)
