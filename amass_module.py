#Modules should be designed to be independant of one another, include ALL requirements
#Modules also always need to include the cwd variable, and pending required language should include the correlated PATH and language path

#####REQUIRED FOR MODULES######
import os
import sys
import re
cwd = os.getcwd() 
os.environ['PATH'] = f'{cwd}/go/bin:' + os.environ['PATH']
os.environ['GOPATH'] = cwd
#####REQUIRED FOR MODULES######

domain = input("insert SINGLE domain you would like to run" + f'\033[92m Amass Scanner\033[0m'+" on: ")

print(os.system(f'{cwd}/go/bin/go install -v github.com/owasp-amass/amass/v4/...@master'))
os.environ['PATH'] = f'{cwd}/bin:' + os.environ['PATH']

output = os.popen(f'script -q -c "{cwd}/bin/amass enum -d {domain} -timeout 1" amass_output.txt').read()
urls = set(re.findall(r"(?:https?://)?(?:[-\w]+\.)*{}(?:[-\w./?%&=]*)".format(re.escape(domain)), output))

with open('urls.txt', 'w') as f:
    f.write('\n'.join((urls)))

##sanitization##

