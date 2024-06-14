#Modules should be designed to be independant of one another, include ALL requirements
#Modules also always need to include the cwd variable, and pending required language should include the correlated PATH and language path

#####REQUIRED FOR MODULES######
import os
import sys
#domain = input("insert SINGLE domain you would like to run hakrawler scanner on: ")
cwd = os.getcwd() 
os.environ['PATH'] = f'{cwd}/go/bin:' + os.environ['PATH']
os.environ['GOPATH'] = cwd
#####REQUIRED FOR MODULES######
print(os.system(f'{cwd}/go/bin/go install -v github.com/tomnomnom/httprobe@latest'))
os.environ['PATH'] = f'{cwd}/bin:' + os.environ['PATH']

output = os.popen(f'script -q -c "cat urls.txt | {cwd}/bin/httprobe"').read()

with open('abs_urls.txt', 'w') as f:
    for url in output:
        f.write(str(url))