print("hello")

import os
from apitime import *

def write_log(message):
    datetime = get_datetime()
    logmessage = datetime + ': ' + message
    with open('log.txt', 'a') as f:
        f.write('\n')
        f.write(logmessage)
        f.close()

def write_log_emergency(message):
    with open('log.txt', 'a') as f:
        f.write('\n')
        f.write(message)
        f.close()        

def clear_log():
    with open('log.txt', 'r') as f:
        lines = len(f.readlines())
        f.close()
    if lines > 200:
        os.remove('log.txt')
        write_log('--- LOG TRUNCATED ---')
