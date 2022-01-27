from threading import Timer
import time
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL) 
#**********************************************
def msg():
    # print('hi')
    return True

# def run_once():
#     t = Timer(10,msg())
#     t.start() #run is call

# run_once()
# print("waiting ..")
#*********************************************************
class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
        print('Done')
#*****************************************************************
# i = 4
# timer = RepeatTimer(3,msg)
# timer.start()
# time.sleep(i)
# print("4 sec")
# i = i + 2
# time.sleep(i)
# timer.cancel()

# i = 2
# # timer = RepeatTimer(1,msg)
# # timer.start()
# while i < 10:
#     time.sleep(i)
#     print(i)
#     i = i + 2


# timer.cancel()
# run_once()
# time.sleep(4)
# print("4sec pass")
#******************************************************



# i = 0.1
# while i < 2:
#     time.sleep(i)
#     print(i)
#     i = i * 2


# print("hi1")

import random

for i in range(100):
    num = random.randint(0,100)
    # print(num)
    if (num > 50):
        print(num)