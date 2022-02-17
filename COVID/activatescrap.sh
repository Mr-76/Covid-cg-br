#!/bin/bash
cd /home/shadow/GIT/Covid-cg-br/COVID
scrapy crawl covid -o covid.json
cp covid.json backup_de_dados/

