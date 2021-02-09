import json
import sys
import time
import xlsxwriter
from configparser import ConfigParser

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

# Loading of input data (LinkedIn Urls)
# profiles_urls = []
# for entry in open(config.get('profiles_data', 'input_file_name'), "r"):
#     profiles_urls.append(entry.strip())

if len(profiles_urls) == 0:
    print("Please provide an input.")
    sys.exit(0)


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
print(p.picture)

# Generation of XLS file with profiles data
# output_file_name = config.get('profiles_data', 'output_file_name')
# if config.get('profiles_data', 'append_timestamp').upper() == 'Y':
#     output_file_name_split = output_file_name.split('.')
#     output_file_name = "".join(output_file_name_split[0:-1]) + "_" + str(int(time.time())) + "." + \
#                        output_file_name_split[-1]

# workbook = xlsxwriter.Workbook(output_file_name)
# worksheet = workbook.add_worksheet()

# Headers
# headers = ['Name', 'Email', 'About', 'Picture', 'Skills', 'Jobs']
# for h in range(len(headers)):
#     worksheet.write(0, h, headers[h])

# # Content
# for i in range(len(scraping_results)):

#     scraping_result = scraping_results[i]

#     if scraping_result.is_error():
#         data = ['Error'] * len(headers)
#     else:
#         p = scraping_result.profile
#         data = [
#             p.name,
#             p.email,
#             p.about,
#             p.picture,
#             ",".join(p.skills)
#         ]

#         for job in p.jobs:
#             data.append(json.dumps(job.reprJSON(), cls=ComplexEncoder))

#     for j in range(len(data)):
#         worksheet.write(i + 1, j, data[j])

# workbook.close()

# print("Scraping Ended")
