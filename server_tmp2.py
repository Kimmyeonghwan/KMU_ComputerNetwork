import http.server

HOST = 'localhost'
PORT = 9987

testserver = http.server.HTTPServer((HOST, PORT), http.server.SimpleHTTPRequestHandler)
testserver.serve_forever()



