
import sys
sys.path.append('../')
from time import sleep

from sonar_service import SonarService

while (True):
    d = SonarService.getInstance().measure()
    print(d)
    
