import start
from logger import *
from apitime import *
from ha import *
from rgb import *

while True:
    write_log('Starting request loop')
    day = get_day()
    if (day == 2) or (day == 3) or (day == 4):
        write_log('Running Day - Starting HA Request')
        bin = run_ha()
        write_log(f'Running {bin} into set_rgb_colour')
        set_rgb_colour(bin)
    else:
        write_log(f'Day is {day} so sleeping until next required')
        turn_off()
    clear_log()
    write_log('Sleeping for 300 seconds until next check')
    time.sleep(300)
        