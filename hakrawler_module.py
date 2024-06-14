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
print(os.system(f'{cwd}/go/bin/go install -v github.com/hakluke/hakrawler@latest'))
os.environ['PATH'] = f'{cwd}/bin:' + os.environ['PATH']
try:
    output=os.popen(f'script -q -c "cat abs_urls.txt | {cwd}/bin/hakrawler -subs" hakrawler_output.txt').read()
except:
    #print("no urls.txt file found, please run a subdomain module first or input a domain")
    print("try again") # if no urls.txt is found it hangs, FIX
finally:
    domain = input("insert SINGLE domain you would like to run httprobe scanner on INCLUDE HTTPS: ")
    output = os.popen(f'script -q -c "echo {domain} | {cwd}/bin/hakrawler -subs" hakrawler_output.txt').read()

with open('hak.txt', 'w') as f:
    if output != None: #need to remove any non in-scope domains
        f.write(str(output))