from datetime import datetime

time = datetime.now().strftime('%H:%M:%S')
time2 = '10:33:00'
FMT='%H:%M:%S'

tdelta = datetime.strptime(time2, FMT) - datetime.strptime(time, FMT)

print tdelta