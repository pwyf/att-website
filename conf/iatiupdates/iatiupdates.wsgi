import logging, sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/tracker/IATI-Updates/pyenv/lib/python2.7/site-packages')
sys.path.insert(0, '/home/tracker/IATI-Updates')
from iatiupdates import app as application
