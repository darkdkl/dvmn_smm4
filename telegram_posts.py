import telegram

import os

def send_telegram(message=None,image=None):
    chat_id=os.getenv('TELEGRAM_CHANNEL_ID')
    
    bot = telegram.Bot(token=os.getenv('TELEGRAM_TOKEN'))
    
   
    if image and message:
        bot.send_message(chat_id=chat_id, text=message)
        with open(image, 'rb') as img:
            bot.send_photo(chat_id=chat_id, photo=img)
            
    elif image:
        with open(image, 'rb') as img:
            bot.send_photo(chat_id=chat_id, photo=img)
    elif message:
        bot.send_message(chat_id=chat_id, text=message)
    else:
        print('No data found.')

    

if __name__ == "__main__":
    send_telegram(None,None)