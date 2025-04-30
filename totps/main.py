import time
from datetime import datetime
my_epoch = datetime(1997, 8, 18)
t_unix = time.time()
t_interval = 30
t_now = t_unix - my_epoch
counter = (t_now - t_unix)/t_interval
print(counter)

