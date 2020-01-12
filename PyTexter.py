from twilio.rest import Client 

client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+12016141610',  
                              body='Hello',      
                              to='+1xxxxxxxxxx'
                          ) 
 
print(message.sid)
