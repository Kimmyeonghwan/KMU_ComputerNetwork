import socket

HOST = 'localhost'
PORT = 9987

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    message = input("Input the message: ")

    if message == 'exit':
        break
    #client_socket.send('HTTP/1.0 200 0K\r\n\r\nHello'.encode('utf-8'))
    client_socket.send(message.encode())
    data = client_socket.recv(1024)
    #print(data)



client_socket.close()