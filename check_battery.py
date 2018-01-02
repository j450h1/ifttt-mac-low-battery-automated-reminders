import sys
from ifttt import *

number = sys.stdin.readlines()[0]
#print(number)
#type = type(number)
#print(typetype))
number = int(number)

if number < 15 and number > 0:
    #Send IFTTT text message
    #print(number)
    message = 'Battery is at {0}%. Recharge!'.format(number)
    print(message)
    IFTTT_notification(message)
