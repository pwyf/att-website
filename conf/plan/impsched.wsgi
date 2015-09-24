import logging, sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/tracker/IATI-Implementation-Schedules/pyenv/lib/python2.7/site-packages')
sys.path.insert(0, '/home/tracker/IATI-Implementation-Schedules')
from impschedules import app as application
