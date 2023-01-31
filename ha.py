import secrets
from logger import *

## HA API ##

def get_ha_sensor():
    url = 'http://192.168.1.34:8123/api/states/sensor.next_bin'
    headers = {'Authorization': secrets.authToken}
    write_log(f'Requesting state from {url}')
    try:
        res = requests.get(url, headers=headers)
        jsonResponse = res.json()
        state = jsonResponse["state"]
        write_log(f'State returned from URL is {state}')
    except:
        state = 'error'
    return state

def get_ha_colour(state): 
    if 'black' in state:
        bin = 'black'
        write_log('Request for colour has returned black')
    elif 'green' in state:
        bin = 'green'
        write_log('Request for colour has returned green')
    elif 'purple' in state:
        bin = 'purple'
        write_log('Request for colour has returned purple')
    elif 'error' in state:
        bin = 'error'
        write_log('HA returned an error during the request for colour - temporarily turning off to reduce issues')
        
    write_log('Running brown check')
    if 'brown' in state:
        bin = bin + ' + brown'
        write_log('Request for colour includes additional colour: brown')
        
    return bin

def run_ha():
    sensor = get_ha_sensor()
    bin_colour = get_ha_colour(sensor)
    return bin_colour
        
        