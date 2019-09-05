
import sys
sys.path.append('../')
from time import sleep

from digital_sensor_distance_service import DigitalSensorDistanceService

while (True):
    d = DigitalSensorDistanceService.getInstance().measure()
    print(d)
    
