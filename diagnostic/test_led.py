
import sys
sys.path.append('../')

from rgb_led_service import RGBLedService
from time import sleep

RGBLedService.getInstance().set_color(1, 0, 0)
sleep(0.5)
RGBLedService.getInstance().set_color(0, 1, 0)
sleep(0.5)
RGBLedService.getInstance().set_color(0, 0, 1)
sleep(0.5)


