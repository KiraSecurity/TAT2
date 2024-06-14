# TAT2

 ## an automated immutable framework for CTFs and Bug Bountys
-NET

############# project structure ############# ( current build ) 

 ``` TAT2/
├── backend/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   ├── database/
│   │   └── init_db.py
│   ├── models.py
│   └── api/
│       ├── __init__.py
│       ├── routes.py
│       ├── subdomain_enum.py
│       ├── service_scan.py
│       └── fuzzing.py
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── yarn.lock
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   ├── styles/
│   │   └── App.js
├── modules/
│   ├── Dockerfile
│   ├── universal_sanitizer/
│   │   └── universal_sanitizer.py
│   ├── enumeration/
│   │   ├── amass_module/
│   │   │   └── amass_module.py
│   │   ├── subfinder_module/
│   │   │   └── subfinder_module.py
│   │   ├── nmap_module/
│   │   │   └── nmap_module.py
│   │   ├── masscan_module/
│   │   │   └── masscan_module.py
│   │   ├── hakrawler_module/
│   │   │   └── hakrawler_module.py
│   │   ├── gospider_module/
│   │   │   └── gospider_module.py
│   │   ├── whois_module/
│   │   │   └── whois_module.py
│   │   ├── dnsenum_module/
│   │   │   └── dnsenum_module.py
│   │   └── dnsrecon_module/
│   │       └── dnsrecon_module.py
│   ├── vulnerability_scanning/
│   │   ├── zap_module/
│   │   │   └── zap_module.py
│   │   ├── nikto_module/
│   │   │   └── nikto_module.py
│   │   ├── nessus_module/
│   │   │   └── nessus_module.py
│   │   ├── openvas_module/
│   │   │   └── openvas_module.py
│   │   ├── wpscan_module/
│   │   │   └── wpscan_module.py
│   │   └── joomscan_module/
│   │       └── joomscan_module.py
│   ├── exploitation/
│   │   ├── metasploit_module/
│   │   │   └── metasploit_module.py
│   │   ├── hashcat_module/
│   │   │   └── hashcat_module.py
│   │   ├── john_module/
│   │   │   └── john_module.py
│   │   ├── sqlmap_module/
│   │   │   └── sqlmap_module.py
│   │   └── xsser_module/
│   │       └── xsser_module.py
│   ├── information_gathering/
│   │   ├── twint_module/
│   │   │   └── twint_module.py
│   │   ├── theharvester_module/
│   │   │   └── theharvester_module.py
│   │   └── maltego_module/
│   │       └── maltego_module.py
│   ├── reporting/
│   │   ├── dradis_module/
│   │   │   └── dradis_module.py
│   │   ├── mdreport_module/
│   │   │   └── mdreport_module.py
│   │   └── pdfreport_module/
│   │       └── pdfreport_module.py
│   ├── automation/
│   │   ├── autoenum_module/
│   │   │   └── autoenum_module.py
│   │   └── autoscan_module/
│   │       └── autoscan_module.py
│   └── utility/
│       ├── httprobe_module/
│       │   └── httprobe_module.py
│       ├── crtsh_module/
│       │   └── crtsh_module.py
│       ├── aquatone_module/
│       │   └── aquatone_module.py
│       └── cewl_module/
│           └── cewl_module.py
├── tests/
│   ├── test_app.py
│   └── test_modules.py
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── .gitignore
├── docker-compose.yml
├── LICENSE
├── README.md
└── setup.py

```
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



