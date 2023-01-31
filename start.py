from logger import *
import machine
from WiFi import *
import time
import ugit

write_log_emergency('--- STARTING BOOT SEQUENCE --')

try:
    WiFi = connect()
except:
    write_log_emergency('--- FAILED TO CONNECT TO WIFI, RESETTING ---')
    machine.reset()

clear_log()
write_log('Sleeping 10 seconds to allow everything to connect')
time.sleep(10)
write_log('Checking for updates')
ugit.pull_all()
write_log('Boot completed.')