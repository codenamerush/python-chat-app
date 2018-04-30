from socket import *

serverName = 'localhost'
serverPort = "1111"

clientSocket = socket(AF_UNIX, SOCK_STREAM)
clientSocket.connect(serverPort)

while True :
	sentence = raw_input("Message: ")
	clientSocket.send(sentence)
	modifiedSentence = clientSocket.recv(1024)
	print 'From server :', modifiedSentence

clientSocket.close()