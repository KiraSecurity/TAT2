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
intel=os.popen(f'script -q -c "cat abs_urls.txt | {cwd}/bin/hakrawler -subs" hakrawler_output.txt').read()

with open('hak.txt', 'w') as f:
    if intel != None:
        f.write(str(intel))