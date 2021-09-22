from typing import List
import requests
from bs4 import BeautifulSoup
import re

url = 'https://pt.indeed.com/jobs?q=python&l='

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

cards = soup.findAll("div", {"class": "job_seen_beacon"})


all_job_offers = []

dias: float = input('Max. job offer time (days) ?')

for card in cards:
    job_name = card.find_next("h2", {"class": "jobTitle"}).get_text()
    job_city = card.find_next("div", {"class": "companyLocation"}).get_text()
    date = card.find_next("span", {"class": "date"}).get_text()

    job_olds = re.findall('[0-9]+', date)

    if(len(job_olds) == 0):
        continue

    if(float(job_olds[0]) <= float(dias)):
        all_job_offers.append(
            {"name": job_name, "age": f'{job_olds[0]} dias', "city": job_city})


for job_offer in all_job_offers:
    print('__________________')
    print(f' Title: {job_offer["name"]} ')
    print(f' Uploaded: {job_offer["age"]} ')
    print(f' City: {job_offer["city"]} ')
