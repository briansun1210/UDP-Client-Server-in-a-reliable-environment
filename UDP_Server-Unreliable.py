
from socket import *
import signal
import time # for sleep
import random # random number for p
import sys
serverPort = 50000

#***********************************************************
def doMath(message): #function that do the math
    read = message.split()
    answer = 0
    if(read[0] == '+'):
        answer = int(read[1]) + int(read[2])
    elif(read[0] == '-'):
        answer = int(read[1]) - int(read[2])
    elif(read[0] == '*'):
        answer = int(read[1]) * int(read[2])
    elif(read[0] == '/'):
        answer = int(read[1]) / int(read[2])

    return answer
#********************************************************
def checkNumOp(message): #check number of operater, this function is for my checkValidMessage function
    countOp = 0
    for i in message: 
        if(i == '*' or i == '/' or i == '+' or i == '-'):
            countOp += 1
    return countOp
#***********************************************************
def checkValidMessage(sentence): #check if the messaage is valid
    read = sentence.split()
    errorType = 200 

    #check if the message is empty or space, if yes return 520 error
    if(len(sentence) == 0 or sentence[0] == ' '):
        errorType = 520

    #check first place operater, 
    if(errorType == 200 and sentence[0] == "*" or sentence[0] == "/" or sentence[0] == "+" or sentence[0]  == "-"): 
        errorType = 200
    else:
        errorType = 520

    if(errorType == 200):
        for i in sentence:
            if(i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z' or i == '.'): #check if there are letters
                errorType = 530
                break

    #if no char, check if there too many operaters
    if(errorType == 200 and checkNumOp(sentence) > 1): 
        errorType = 530
    elif(errorType == 200 and len(read) != 3): #check if too many numbers
        errorType = 530
    elif(errorType == 200 and read[0] == '/' and read[2] == '0'):    #check devide 0
        errorType = 530

    return errorType

#*******************************************************************

signal.signal(signal.SIGINT, signal.SIG_DFL) 
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("the UDP server is ready to receive\n")

while (True):
    num = random.randint(0,100) 
    p = float(sys.argv[1])
    message, clientAddress = serverSocket.recvfrom(1024) #1024 is buffer size
    sentence = message.decode()
    errorType = checkValidMessage(sentence)

    if(num > (p * 100)):
        if(errorType == 530):
            serverSocket.sendto(bytes("530 -1", "utf-8"), clientAddress)
        elif(errorType == 520):
            serverSocket.sendto(bytes("520 -1", "utf-8"), clientAddress)
        elif(errorType == 200):
            result = "200 " + str(doMath(sentence))
            serverSocket.sendto(result.encode(), clientAddress)
        else:
            serverSocket.sendto(bytes("special error", "utf-8"), clientAddress)
    else: #testing, make sure server ignore
        print("ignore")
        print(num)

