import socket

HOST = 'localhost'
PORT = 9987

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ?ÜåÏº? ?Éù?Ñ±
server_socket.bind((HOST, PORT))
server_socket.listen()

client_socket, client_address = server_socket.accept()

'''
server_list = []
if server_list not in client_address:
    server_list.append(client_address)
'''

while True:
    data = client_socket.recv(1024)
    request_data = data.decode().split()
    request_method = request_data[0]
    #print(request_method, request_data[1])
    print(data.decode())

    if data.decode() == 'exit':
        break

    elif data:
        #print(request_method)
        client_socket.send(data.encode())

    else:
        print('no message')
        break


client_socket.close()



