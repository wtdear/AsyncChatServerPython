import socket
import logging
import logging_system
import threading
from config import SERVER_HOST, SERVER_PORT

server = socket.socket()
server.bind((SERVER_HOST, SERVER_PORT))
server.listen(2)
logging.debug(f"[SERVER] {SERVER_HOST}:{SERVER_PORT} starting...")

# Принимаем первого клиента
client1, addr1 = server.accept()
name1 = client1.recv(1024).decode()
print(f"{name1} connected")

# Принимаем второго клиента  
client2, addr2 = server.accept()
name2 = client2.recv(1024).decode()
print(f"{name2} connected")

# Теперь пересылаем сообщения между ними
def forward(src, dst, name):
    while True:
        msg = src.recv(1024)
        dst.send(f"{name}: {msg}".encode())

# Запускаем потоки для пересылки
threading.Thread(target=forward, args=(client1, client2, name1)).start()
threading.Thread(target=forward, args=(client2, client1, name2)).start()