import network
import secrets
from logger import *
import time

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets.SSID, secrets.PASSWORD)
    while wlan.isconnected() == False:
         write_log('Waiting for WiFi connection...')
         time.sleep(1)
    ip = wlan.ifconfig()[0]
    write_log(f'Connected to WiFi on {ip}')
    return ip