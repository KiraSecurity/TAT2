#Modules should be designed to be independant of one another, include ALL requirements
#Modules also always need to include the cwd variable, and pending required language should include the correlated PATH and language path

#####REQUIRED FOR MODULES######
import os
import sys
import re
#domain = input("insert SINGLE domain you would like to run hakrawler scanner on: ")
cwd = os.getcwd() 
os.environ['PATH'] = f'{cwd}/go/bin:' + os.environ['PATH']
os.environ['GOPATH'] = cwd
#####REQUIRED FOR MODULES######
os.system(f'{cwd}/go/bin/go install -v github.com/tomnomnom/httprobe@latest')
os.environ['PATH'] = f'{cwd}/bin:' + os.environ['PATH']
try:
    output = print(os.popen(f'script -q -c "cat urls.txt | {cwd}/bin/httprobe"').read())
except:
    #print("no urls.txt file found, please run a subdomain module first or input a domain")
    print("try again") # if no urls.txt is found it hangs, FIX
finally:
    domain = input("insert SINGLE domain you would like to run httprobe scanner on: ")
    domain = re.sub(r'^https?://', '', domain)
    output = os.popen(f'script -q -c "echo {domain} | {cwd}/bin/httprobe"').read()

with open('abs_urls.txt', 'w') as f:
    for url in output:
        f.write(str(url))