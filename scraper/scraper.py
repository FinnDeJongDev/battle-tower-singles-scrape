from bs4 import BeautifulSoup
import requests
import re
import json

base_url = 'https://www.serebii.net'
trainer_list_url = f'{base_url}/brilliantdiamondshiningpearl/battletower.shtml'
pathname_trainers_url = '/brilliantdiamondshiningpearl/battletower/singles/'
shtml_url = '.shtml'

page = requests.get(trainer_list_url);

soup = BeautifulSoup(page.text, 'html.parser')

trainer_options = soup.find_all('option', value = re.compile("/brilliantdiamondshiningpearl/battletower/singles/"))

trainer_list = [ name.text.strip() for name in trainer_options]

trainer_url_list = [ ]
for trainer in trainer_list:
  if trainer.find("-") != -1:
    split_trainer_by_dash = trainer.split('-')
    trainer_name = split_trainer_by_dash[0].split()[0]
    trainer_level = split_trainer_by_dash[-1]
    trainer_url_list.append(base_url + pathname_trainers_url + (trainer_name + '-' + trainer_level.strip()).replace(" ", "").lower() + shtml_url)
  else:
    trainer_url_list.append(base_url + pathname_trainers_url + trainer.split()[0].lower() + shtml_url)

print(len(trainer_url_list))

# for url_trainer in trainer_url_list:
#   trainer_page = requests.get(url_trainer)
#   print(BeautifulSoup(trainer_page.text, 'html.parser'))