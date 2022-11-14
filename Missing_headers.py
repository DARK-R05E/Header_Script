import requests
import sys
from termcolor import colored
import warnings

warnings.filterwarnings('ignore') 
url = sys.argv[1] 

try:
    g = requests.get(url)
except:
    print('ssl error but we still check:)')
    g = requests.get(url, verify=False)
	
website = g.headers

options = ["X-Frame-Options", "Content-Security-Policy", "Strict-Transport-Security", "X-XSS-Protection", "X-Content-Type-Options"]
for new in options:
    if new in website:
        print(colored('%s is present.\n'%new, 'green'))
    else:
        print(colored('%s is not present.\n'%new, 'red'))

