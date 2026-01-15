import socket
import logging
import logging_system
from threading import Thread
from datetime import datetime
from config import SERVER_HOST, SERVER_PORT

client_socket = socket.socket()

# Connection
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}")
client_socket.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")

# User Data
name = input("Enter your name: ")
client_socket.send(name.encode())
interlocutor_name = input("Enter interlocutor name ( Who do you want to write to? ): ")
client_socket.send(interlocutor_name.encode())
logging.debug(f"[Client] create connection with name - {name}")
logging.debug(f"[Client] {name} starts chat with {interlocutor_name}")

# Функция приема сообщений
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"\n{message}")
                print("You: ", end="", flush=True)  # чтобы не ломать ввод
        except:
            print("\n[-] Connection lost")
            break

# Запускаем прием сообщений в фоне
receive_thread = Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

message = input()
client_socket.send(message.encode())