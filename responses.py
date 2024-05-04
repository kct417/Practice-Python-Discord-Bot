import random

def handle_response(message) -> str:
    p_message = message.lower()
    message_arr = message.split()
    
    welcome = ['hi', 'hey', 'hello']
    
    if p_message in welcome:
        return 'Hey there!'
    
    if p_message == 'roll':
        return str(random.randint(1, 6))
    
    if message_arr[0] == 'roll' and message_arr[1].isdigit() and len(message_arr) == 2:
        return str(random.randint(1, int(message_arr[1])))
    
    if message_arr[0] == 'roll' and message_arr[1].isdigit() and message_arr[2].isdigit():
        return str(random.randint(int(message_arr[1]), int(message_arr[2])))
