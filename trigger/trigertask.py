import subprocess
import time
from datetime import datetime



while True:

    data_HJ = datetime.now()
    hora = data_HJ.hour
    minute = data_HJ.minute
    if hora == 20 and minute == 27:
        run = subprocess.run(' cd /home/cremoso/Git/covid_cg-br/Covid-cg-br/COVID; scrapy crawl covid -o covid.json', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(run)

        time.sleep(70)


