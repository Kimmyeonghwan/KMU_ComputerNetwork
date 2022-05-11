import socket
import os

def server():
    host = '172.30.1.29' # 14.54.229.103 실제 이더넷 ip
    port = 9977
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 소켓 생성
    server_socket.bind((host, port))
    server_socket.listen(1)

    files = os.listdir(os.getcwd())
    for i in range(len(files)):
        files[i] = '/' + files[i]
    files_tmp = files[:]

    print('waiting for a client...')
    connect, address = server_socket.accept()
    print('connect the client: ', address)

    request = ''
    while True:
        data = connect.recv(1024)
        request += data.decode('utf8')
        request_data = request.split()

        if '\r\n\r\n' in request:
            break

    print('recevied: ', request)
    if request_data[0] == 'exit':
        connect.send('Close Success'.encode())
        server_socket.close()

    elif request_data[0] == 'GET':
        # GET 명령어를 받을 경우 처리하는 코드
        if request_data[1] in files or request_data[1] == '/':
            request_messgae = '200 OK\r\n\r\n'

        else:
            request_messgae = '404 File not found'



    elif request_data[0] == 'POST':
        # POST 명령어를 받을 경우 처리하는 코드
        if len(request_data) >= 2:
            if (request_data[1] in files_tmp) and (request_data[1] in files):
                '''
                for i in files:
                    if i == request_data[1]:
                        files.append(request_data[1])
                '''
                request_messgae = '200 OK\r\n\r\n'

            elif (request_data[1] in files_tmp) and (request_data[1] not in files):
                request_messgae = '301 Moved Permanently' + '\r\n200 OK'  # 301 Error가 발생하고, redirection 성공했을 경우 가정하여 200 OK GET으로 출력


            elif (request_data[1] not in files_tmp) and (request_data[1] not in files):
                files.append(request_data[1])
                request_messgae = '201 Created'

            else:
                request_messgae = '400 Bad Request'
        else:
            request_messgae = '400 Bad Request'

    elif request_data[0] == 'PUT':
        # PUT 명령어를 받을 경우 처리하는 코드
        if len(request_data) == 1:
            request_messgae = '400 Bad Request'

        elif len(request_data) == 5:
            if request_data[1] in files:
                request_messgae = '201 Created'

        else:
            request_messgae = '400 Bad Request'

    elif request_data[0] == 'DELETE':
        # 실제 서버 환경처럼 POST 명령어를 수행하기 위해 추가한 코드
        print(files)
        if request_data[1] in files:
            files.remove(request_data[1])
            request_messgae = request_data[1] + ' file DELETE Success'
        else:
            request_messgae = '400 Bad Request'
        print(files)

    elif request_data[0] == 'OPTIONS':
        request_messgae = 'HTTP/1.1 200 OK \r\nAllow: GET, POST, DELETE, PUT, OPTIONS'


    else:
        # 서버에서 지원하지 않는 명령어를 받을 경우 처리하는 코드
        request_messgae = '405 Method Not Allowed ({method})'.format(method=request_data[0])
        pass

    connect.send(request_messgae.encode())
    print(request_data)


    server_socket.close()

server()


'''
GET / HTTP/1.1
Host: localhost:9987
Connection: keep-alive
Cache-Control: max-age=0
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
'''