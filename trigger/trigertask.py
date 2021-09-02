import subprocess
import time
run = subprocess.run(' cd /home/cremoso/Git/covid_cg-br/Covid-cg-br/COVID; scrapy crawl covid -o covid.json', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print(run)
