import urequests as requests

## World Time API ##

def timeapi_request():
    url = 'http://worldtimeapi.org/api/timezone/Europe/London'
    try:
        res = requests.get(url)
        jsonResponse = res.json()
        return jsonResponse
    except:
        machine.reset()

def get_day():
    timeapi = timeapi_request()
    day = timeapi['day_of_week']
    return day

def get_datetime():
    timeapi = timeapi_request()
    datetime = timeapi['datetime']
    return datetime