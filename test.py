import json
import os
import sys
import time
from configparser import ConfigParser
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import model_from_json
import cv2
import json
import numpy as np
import urllib
import warnings
import time

warnings.filterwarnings("ignore")

from Scraper import Scraper
import argparse

parser  = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=True,
                    help = "Enter the linkedin url of the user")

args = vars(parser.parse_args())
profiles_urls = [args['url']]
# Loading of configurations
from utils import ComplexEncoder

config = ConfigParser()
config.read('config.ini')

# Setting the execution mode
headless_option = len(sys.argv) >= 2 and sys.argv[1].upper() == 'HEADLESS'

if len(profiles_urls) == 0:
    print("Please provide an input.")
    sys.exit(0)
t = time.time()

# Launch Scraper
s = Scraper(
    linkedin_username=config.get('linkedin', 'username'),
    linkedin_password=config.get('linkedin', 'password'),
    profiles_urls=profiles_urls,
    headless=headless_option
)

s.start()

s.join()

scraping_results = s.results
p = scraping_results[0].profile
url = p.picture
about = p.about
print(about)

with open('ipv2.json', 'r') as json_file:
    # j = json.loads(json_file)
    model = model_from_json(json_file.read())

# print(model.summary())
model.load_weights('ipv2.h5')

url_response = urllib.request.urlopen(url)
img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
img = cv2.imdecode(img_array, -1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (208, 208), cv2.INTER_CUBIC)
img = np.array(img)

img = np.expand_dims(img, axis = 0)
print(img.shape)

personality_traits = ['Extraversion', 'Agreeableness', 'Conscientiousness', 'Neurotisicm', 'Openness']
y = model.predict(img)

output_dir = './output'
op_file = str(args["url"]) + "_" + str(t) + ".txt"
with open(os.path.join(output_dir, op_file), "a") as f:
    for i in range(len(personality_traits)):
        print(f"{personality_traits[i]} ----------> {y[0][i]*100}%")
        f.write(f"{personality_traits[i]} ----------> {y[0][i]*100}%")