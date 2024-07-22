import requests
import sys
from termcolor import colored
import warnings

warnings.filterwarnings('ignore')

url = sys.argv[1]

print('\n\nTarget URI is: \033[0;36m%s'%url)
print(colored("",'white'),end='')

try:
    g = requests.get(url)
    print('\n')
except:
    print('\nAn ',end='')
    print(colored('SSL/TLS error','red'),end='')
    print(' has occured. Please investigate.\n')
    g = requests.get(url, verify=False)
website = g.headers

options = ["X-Frame-Options", "Content-Security-Policy", "Strict-Transport-Security", "X-Content-Type-Options","X-XSS-Protection"]
for new in options:
    if new == "X-XSS-Protection":
        print(colored('%s is present, and has been deprecated.'%new, 'red'))
        print("Its value is: %s\n"%website[new])
    elif new in website:
        print(colored('%s is present.'%new, 'green'))
        print("Its value is: %s\n"%website[new])
    

    else:
        print(colored('%s is not present.\n'%new, 'red'))


