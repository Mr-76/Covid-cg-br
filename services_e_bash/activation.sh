#!/bin/bash
cd /home/alarm/GIT/Covid-cg-br/COVID
scrapy crawl covid -o covid.json
cp covid.json backup_de_dados
