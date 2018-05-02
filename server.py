from socket import *

serverSocket = socket(AF_UNIX, SOCK_STREAM)
serverSocket.bind("1111")
serverSocket.listen(1)
print 'Server set up done'

while True :
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	print 'From client:', sentence
	capitalizedSentence = raw_input('Reply: ')
	connectionSocket.send(capitalizedSentence)
	serverSocket.listen(8)
connectionSocket.close()