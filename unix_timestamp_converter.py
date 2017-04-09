import pytz
from datetime import datetime
import time

timestamp = int(time.time())

print(timestamp)

tz = pytz.timezone('Europe/Lisbon')
print(datetime.fromtimestamp(1463288494, tz).isoformat())


