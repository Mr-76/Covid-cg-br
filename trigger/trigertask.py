import subprocess
import time
from datetime import datetime


#a = True
#while True:
 #   time.sleep(20)
 #   data_HJ = datetime.now()
  #  hora = data_HJ.hour
   # minute = data_HJ.minute
    #if hora == 10 and minute == 35:
subprocess.run('cd /home/alarm/GIT/Covid-cg-br/COVID; scrapy crawl covid -o covid.json', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#print(run)

    #   time.sleep(70)
#a = True

