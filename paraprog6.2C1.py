import socket

c1 = socket.socket()
host = '192.168.240.8'
port = 8888

print("waiting connection")
try:
	c1.connect((host,port))
except socket.error as e:
	print(str(e))

res = c1.recv(1024)
print(res)
while True:
	input = input("Say Something:")
	c1.send(str.encode(input))
	res =c1.recv(1024)
	print(res.decode('utf-8'))

c1.close()
