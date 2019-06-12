#!/usr/bin/python
import socket
import sys
import os
import time

serverAddress = ''
while(serverAddress == ''):
	serverAddress = raw_input("Server IP Address: ")
print('Server IP Adrress is set to ' + serverAddress)

serverPort = ''
while(serverPort == ''):
	serverPort = raw_input('Server Port: ')
print('Server Port is set to ' + serverPort)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Connection to ' + serverAddress + ' on port ' + serverPort + '...\n')
s.connect((serverAddress, int(serverPort)))

time.sleep(3)
os.system('CLS' if os.name == 'nt' else 'clear')


handServer = [[0 for x in range(9)] for y in range(9)];
handClient = [[0 for x in range(9)] for y in range(9)];

iCount = 0
while iCount < 7:
	handServer[iCount][0] = int(s.recv(1))
	handServer[iCount][1] = int(s.recv(1))
	handClient[iCount][0] = int(s.recv(1))
	handClient[iCount][1] = int(s.recv(1))
	iCount += 1

iRound = 1;
while (iRound <= 7):

	print "Your hand is:\n"
	print " [" + str(handClient[0][0]) + "][" + str(handClient[0][1]) + "] [" + str(handClient[1][0]) + "][" + str(handClient[1][1]) + "] [" + str(handClient[2][0]) + "][" + str(handClient[2][1]) + "] [" + str(handClient[3][0]) + "][" + str(handClient[3][1]) + "] [" + str(handClient[4][0]) + "][" + str(handClient[4][1]) + "] [" + str(handClient[5][0]) + "][" + str(handClient[5][1]) + "] [" + str(handClient[6][0]) + "][" + str(handClient[6][1]) + "]\n"

	print "Your opponent hand is:\n"
	print " [" + str(handServer[0][0]) + "][" + str(handServer[0][1]) + "] [" + str(handServer[1][0]) + "][" + str(handServer[1][1]) + "] [" + str(handServer[2][0]) + "][" + str(handServer[2][1]) + "] [" + str(handServer[3][0]) + "][" + str(handServer[3][1]) + "] [" + str(handServer[4][0]) + "][" + str(handServer[4][1]) + "] [" + str(handServer[5][0]) + "][" + str(handServer[5][1]) + "] [" + str(handServer[6][0]) + "][" + str(handServer[6][1]) + "]\n\n"

	print "Please wait while your opponent makes his play...\n"
	iChoiceServer = int(s.recv(1))
	print "Your opponent chose to play " + "[" + str(handServer[iChoiceServer][0]) + "][" + str(handServer[iChoiceServer][1]) + "]" + "\n"

        iChoiceClient = -1
        while(iChoiceClient < 1 or iChoiceClient > 7 or handClient[iChoiceClient-1][0] == 0 or (not str(iChoiceClient).isdigit)):
                iChoiceClient = int(input("Choose the number of the item you want to play (1 to 7): "))
        s.send(str(iChoiceClient-1))
        iChoiceClient -= 1
	print "You chose to play [" + str(handClient[iChoiceClient][0]) + "][" + str(handClient[iChoiceClient][1]) + "]\n"

        print "And the winner is..."
	time.sleep(2)

	iWinner = -1
	iWinner = int(s.recv(1))

	if(iWinner == 1):
		print "Your opponent..."

	elif(iWinner == 2):
		print "YOU!"

	elif(iWinner == 3):
		print "EQUALITY..."

        time.sleep(3)
        
        iCount = 0
        while iCount < 7:
                handServer[iCount][0] = int(s.recv(1))
                handServer[iCount][1] = int(s.recv(1))
                handClient[iCount][0] = int(s.recv(1))
                handClient[iCount][1] = int(s.recv(1))
                iCount += 1

	iRound += 1
	os.system('CLS' if os.name == 'nt' else 'clear')


iServerScore = int(s.recv(2))
iClientScore = int(s.recv(2))

print "Your final score is " + str(iClientScore)
print "Your opponent final score is " + str(iServerScore)
time.sleep(10)

s.close()
sys.exit(0)
