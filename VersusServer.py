#!/usr/bin/python
import socket
import sys
import os
import random
import time

serverAddress = ''
while(serverAddress == ''):
	serverAddress = raw_input("Server IP Address: ")
print('Server IP Address is set to ' + serverAddress)

serverPort = ''
while(serverPort == ''):
	serverPort = raw_input("Server Port: ")
print('Server Port is set to ' + serverPort)

print("Awaiting connection...")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((serverAddress, int(serverPort)))
s.listen(10)

c, addr = s.accept()
print("* Got connection from " + str(addr) + "\n")

time.sleep(3)
os.system('CLS' if os.name == 'nt' else 'clear')


handServer = [[0 for x in range(9)] for y in range(9)];
handClient = [[0 for x in range(9)] for y in range(9)];

iCount = 0;
while iCount < 7:
 	handServer[iCount][0] = random.randint(1, 9)
 	handClient[iCount][0] = random.randint(1, 9)
 	handServer[iCount][1] = random.randint(1, 9)
 	handClient[iCount][1] = random.randint(1, 9)
	iCount += 1

iCount = 0
while iCount < 7:
	c.send(str(handServer[iCount][0]))
	c.send(str(handServer[iCount][1]))
	c.send(str(handClient[iCount][0]))
	c.send(str(handClient[iCount][1]))
	iCount += 1

iServerScore = 0
iClientScore = 0

iRound = 1;
while (iRound <= 7):

	print "Your hand is:\n"
	print " [" + str(handServer[0][0]) + "][" + str(handServer[0][1]) + "] [" + str(handServer[1][0]) + "][" + str(handServer[1][1]) + "] [" + str(handServer[2][0]) + "][" + str(handServer[2][1]) + "] [" + str(handServer[3][0]) + "][" + str(handServer[3][1]) + "] [" + str(handServer[4][0]) + "][" + str(handServer[4][1]) + "] [" + str(handServer[5][0]) + "][" + str(handServer[5][1]) + "] [" + str(handServer[6][0]) + "][" + str(handServer[6][1]) + "]\n"

	print "Your opponent hand is:\n"
	print " [" + str(handClient[0][0]) + "][" + str(handClient[0][1]) + "] [" + str(handClient[1][0]) + "][" + str(handClient[1][1]) + "] [" + str(handClient[2][0]) + "][" + str(handClient[2][1]) + "] [" + str(handClient[3][0]) + "][" + str(handClient[3][1]) + "] [" + str(handClient[4][0]) + "][" + str(handClient[4][1]) + "] [" + str(handClient[5][0]) + "][" + str(handClient[5][1]) + "] [" + str(handClient[6][0]) + "][" + str(handClient[6][1]) + "]\n\n"

	iChoiceServer = -1
	while(iChoiceServer < 1 or iChoiceServer > 7 or handServer[iChoiceServer-1][0] == 0 or (not str(iChoiceServer).isdigit)):
		iChoiceServer = int(input("Choose the number of the item you want to play (1 to 7): "))
	c.send(str(iChoiceServer-1))
	iChoiceServer -= 1
	print "You chose to play [" + str(handServer[iChoiceServer][0]) + "][" + str(handServer[iChoiceServer][1]) + "]\n"

	iChoiceClient = int(c.recv(1))
	print "Your opponent chose to play [" + str(handClient[iChoiceClient][0]) + "][" + str(handClient[iChoiceClient][1]) + "]\n"
	
	randomServer = random.randint(0, int(handServer[iChoiceServer][0]))
	randomClient = random.randint(0, int(handServer[iChoiceClient][0]))

	print "And the winner is... "
	time.sleep(2)

	iWinner = -1

	if(randomServer > randomClient):
		iWinner = 1
		print "YOU!"
		iServerScore += handServer[iChoiceServer][1]
    
	elif(randomServer < randomClient):
		iWinner = 2
		print "Your opponent..."
		iClientScore += handClient[iChoiceClient][1]

	elif(randomServer == randomClient):
		iWinner = 3
		print "EQUALITY..."

	c.send(str(iWinner))

	time.sleep(3)

	handServer[iChoiceServer][0] = 0
	handServer[iChoiceServer][1] = 0
	handClient[iChoiceClient][0] = 0
	handClient[iChoiceClient][1] = 0

	iCount = 0
	while iCount < 7:
		c.send(str(handServer[iCount][0]))
		c.send(str(handServer[iCount][1]))
		c.send(str(handClient[iCount][0]))
		c.send(str(handClient[iCount][1]))
		iCount += 1

	iRound += 1
	os.system('CLS' if os.name == 'nt' else 'clear')

sServerScore = str(iServerScore)
if(len(str(iServerScore)) == 1):
	sServerScore = "0" + str(iServerScore)
c.send(sServerScore)

sClientScore = str(iClientScore)
if(len(str(iClientScore)) == 1):
	sClientScore = "0" + str(iClientScore)
c.send(sClientScore)

print "Your final score is " + str(iServerScore)
print "Your opponent final score is " + str(iClientScore)
time.sleep(10)
os.system('CLS' if os.name == 'nt' else 'clear')

c.close()
s.close()
sys.exit(0)

