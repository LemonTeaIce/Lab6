import socket

c = socket.socket()
host = '192.168.240.8'
port = 8888

print('Waiting for connection')
try:
	c.connect((host,port))
except socket.error as e:
	print(str(e))

response = c.recv(1024)
print(response)
while True:
	input = input("Say something:")
	c.send(str.encode(input))
	response =c.recv(1024)
	print(response.decode('utf-8'))

c.close()
