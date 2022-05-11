import http.client

HOST = 'localhost'
PORT = 9987

testclient = http.client.HTTPConnection('localhost:9987')
testclient.request("GET", "/")
r1 = testclient.getresponse()
print(r1.status, r1.reason)

testclient.request("GET", "/test.te")
r2 = testclient.getresponse()
print(r2.status, r2.reason)


testclient.request("GET", "/main.py")
r3 = testclient.getresponse()
print(r3.status, r3.reason)


testclient.request("POST", "/main.py")
r4 = testclient.getresponse()
print(r4.status, r4.reason)