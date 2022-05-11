import socket
import os

def client():
    host = '127.0.0.1'
    port = 9987
    files = os.listdir(os.getcwd())

    while True:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        message_temp = input('Input the message: ')
        message = message_temp.split()
        response = ''

        if message[0] == 'exit':
            request_header = 'exit\r\n\r\n'
            client_socket.send(request_header.encode())
            break

        elif len(message) <= 0:
            print("plz try again input the message")
            continue

        elif message[0] == 'GET':
            if len(message) == 1:
                request_header = message[0] + ' /  HTTP/1.1\r\nHost: ' + host + ':' + str(port) + '\r\nAccept-Encoding: identity\r\n\r\n'

            else:
                request_header = message[0] + ' /' + message[1] + ' HTTP/1.1\r\nHost: ' + host + ':' + str(port) + '\r\nAccept-Encoding: identity\r\n\r\n'

        elif message[0] == 'POST':
            if len(message) == 1:
                request_header = message[0] + '\r\n\r\n'

            else:
                if message[1] in files:
                    request_header = message[0] + ' /' + message[1] + ' HTTP/1.1\r\nHost: ' + host + ':' + str(port) + \
                                     '\r\nContent-Type: Multipart/related \r\nContent-Length: ' +  str(os.path.getsize(files[files.index(message[1])])) +  '\r\n\r\n'

                else:
                    request_header = message[0] + ' /' + message[1] + ' HTTP/1.1\r\nHost: ' + host + ':' + str(port) + \
                                     '\r\nContent-Type: Multipart/related \r\nContent-Length: Unknown\r\n\r\n'

        elif message[0] == 'PUT':
            if len(message) == 1:
                request_header = message[0] + '\r\n\r\n'

            elif len(message) == 2:
                if '.txt' in message[1]:
                    request_header = message[0] + ' /' + message[1] + ' HTTP/1.1\r\nContent-Type: txt/plan\r\n\r\n'

                elif '.html' in message[1]:
                    request_header = message[0] + ' /' + message[1] + ' HTTP/1.1\r\nContent-Type: txt/html\r\n\r\n'

                elif '.js' in message[1]:
                    request_header = message[0] + ' /' + message[1] + ' HTTP/1.1\r\nContent-Type: txt/javascript\r\n\r\n'

                elif '.xml' in message[1]:
                    request_header = message[0] + ' /' + message[1] + ' HTTP/1.1\r\nContent-Type: txt/xml\r\n\r\n'

                else:
                    request_header = message[0] + ' /' + message[1] + ' HTTP/1.1\r\nContent-Type: Multipart/related\r\n\r\n'

            elif len(message) == 3:
                if '.txt' in message[1]:
                    request_header = message[0] + ' /' + message[1] + ' /' + message[2] + ' HTTP/1.1\r\nContent-Type: txt/plan\r\n\r\n'

                elif '.html' in message[1]:
                    request_header = message[0] + ' /' + message[1] + ' /' + message[2] + ' HTTP/1.1\r\nContent-Type: txt/html\r\n\r\n'

                elif '.js' in message[1]:
                    request_header = message[0] + ' /' + message[1] + ' /' + message[2] + ' HTTP/1.1\r\nContent-Type: txt/javascript\r\n\r\n'

                elif '.xml' in message[1]:
                    request_header = message[0] + ' /' + message[1] + ' /' + message[2] + ' HTTP/1.1\r\nContent-Type: txt/xml\r\n\r\n'

                else:
                    request_header = message[0] + ' /' + message[1] + ' /' + message[2] + ' HTTP/1.1\r\nContent-Type: Multipart/related\r\n\r\n'

            else:
                request_header = message[0] + '\r\n\r\n'


        elif message[0] == 'DELETE':
            request_header = message[0] + ' /' + message[1] + '\r\n\r\n'

        else:
            #print("plz try again input the message")
            request_header = message[0] + " \r\n\r\n"


        client_socket.send(request_header.encode())
        recv = client_socket.recv(1024)
        response += recv.decode('utf8')

        print (response)
        client_socket.close()

client()