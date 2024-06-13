#Modules should be designed to be independant of one another, include ALL requirements
#Modules also always need to include the cwd variable, and pending required language should include the correlated PATH and language path

#####REQUIRED FOR MODULES######
import os
import sys
domain = input("insert domain you would like to run amass scanner on: ")
cwd = os.getcwd() 
os.environ['PATH'] = f'{cwd}/go/bin:' + os.environ['PATH']
os.environ['GOPATH'] = cwd
#####REQUIRED FOR MODULES######
print(os.system(f'{cwd}/go/bin/go install -v github.com/owasp-amass/amass/v4/...@master'))
os.environ['PATH'] = f'{cwd}/bin:' + os.environ['PATH']
print(os.system(f'script -q -c " {cwd}/bin/amass enum -d {domain}" amass_subdomains.txt'))