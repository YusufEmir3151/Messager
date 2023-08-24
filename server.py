import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))
server_socket.listen()

print("Sunucu dinliyor...")
client_socket, client_address = server_socket.accept()
print(f"{client_address} bağlandı.")

while True:
    message = client_socket.recv(1024).decode()
    print("İstemci:", message)
    response = input("Cevap: ")
    client_socket.send(response.encode())
