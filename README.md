# TAT2
an automated immutable framework for CTFs and Bug Bountys

## goal is for anybody to deploy the framework with the modules of their choice and they will deploy succesfully

### dependencies preventing immutability

for modules they should be a directory with main code as well as requireed imports and specified version numbers

module output (txt file currently, possibly database tags). Biggest current issue is modules have to be loaded in a specified order because they are retreiving input from hard-coded input file.

module dependency for inputs (eg. httprobe module requires http/s protocol to be added to url, should be accounted for that not all subdomain finders will add those)

Modules will also need to mark their tools executing language, all modules are writen in python but the tool might be in GO, need to be compiled, etc. 

module groups and work-flow requirements (sub-domain enumerators, fuzzers, etc.)

possibly including permanant modules such as sub-domain enumeration, but with replace and add capbility to account for tool preference

required language librarys like go, rust, etc. need to all be included in a module creation template, which will have required variables to ensure compatability

need to create a standard module output sanitzation script so all modules can expect the same exact input formats

noted versioning for tools, eg. hakrawler 2.7.1 runs on TAT2 V1 so when V1 is deployed it will only use tool versions previously validated





example of required template for go-lang tools: 

#####REQUIRED FOR MODULES######
import os
import sys
#domain = input("insert SINGLE domain you would like to run hakrawler scanner on: ")
cwd = os.getcwd() 
os.environ['PATH'] = f'{cwd}/go/bin:' + os.environ['PATH']
os.environ['GOPATH'] = cwd
#####REQUIRED FOR MODULES######

## other ideas
having framework on deployment allow selection of tools from prompt so once executed the framework will reachout to the repo and retreieve the modules selected to prevent bloatware from unused modules



