from socket import *
import signal
import sys
import time # for sleep
import errno # for handle error from settimeout function 
serverPort = 50000
serverName = 'localhost'
signal.signal(signal.SIGINT, signal.SIG_DFL) 

#***************************************************************************************
def checkReply(message): #base on the message from server, return the appropriate outcome
    read = message.split()
    if(read[0] == '530'):
        print("\nInvalid operands, send an error status code of 530. \n- Operands not integer numbers (positive and/or negative).\n- Division by zero (0).")
    elif(read[0] == '520'):
        print('\nInvalid OC (i.e. not +, -, *, or /), send an error status code of 520.')
    elif(read[0] == '200'):
        print('\n' + read[1])
#***************************************************************************************

f = open(sys.argv[1], "r")
for i in range(7):
    d = 0.1 #default/reset default wait time is 0.1 sec

    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = f.readline()

    while(True):
        clientSocket.sendto(message.encode(), (serverName, serverPort)) #keep sending after the wait time, so this line has to be in the while loop!!!!
        clientSocket.settimeout(d)
        try: # have to use the try except method to handle the set timeout error
            modifiedMessage,serverAddress = clientSocket.recvfrom(1024)
            if not modifiedMessage:
                print("connection closed")
                clientSocket.close()
            else:
                respond = modifiedMessage.decode()
                checkReply(respond)
                break
        except error as e: #handle the error from settimeout
            if e.args[0] == errno.EWOULDBLOCK: 
                print ('EWOULDBLOCK')
                time.sleep(1)           # short delay, no tight loops
            else:
                if(d > 2):
                    print('The server is DEAD.')
                    break
                print(d) #testing to see the wait time
        d = d * 2 #reset wait time


clientSocket.close()
f.close()
