
def route_message(message_type, message):  
    if message_type == 'email':  
        print(f"Sending email: {message}")  
    elif message_type == 'sms':  
        print(f"Sending SMS: {message}")  
    else:  
        print("Unknown message type!")  

 
route_message('email', 'Welcome to our service!')  
route_message('sms', 'Your order has been shipped!')
