from socket import *

serverSocket = socket(AF_UNIX, SOCK_STREAM)
serverSocket.bind("1111")
serverSocket.listen(8)
print 'Server set up done'

connectionSocket, addr = serverSocket.accept()
	
while True :
	sentence = connectionSocket.recv(1024)
	print 'From client:', sentence
	capitalizedSentence = raw_input('Reply: ')
	connectionSocket.send(capitalizedSentence)
connectionSocket.close()
