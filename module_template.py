#category: *include category
#input dependencies: *input single word dependency, eg domain, hash, full url
#language: go

#####REQUIRED FOR MODULES######
import os
import sys
import re
cwd = os.getcwd() 
name = "input tool name"
#####REQUIRED FOR MODULES######
go_bin_path = f'{cwd}/bins/go/bin'
name_bin_path = f'{cwd}/modules/enumeration/{name}/bin'  # Ensure this points to a directory for binaries
# Create the directory if it doesn't exist
os.makedirs(name_bin_path, exist_ok=True)
# Set environment variables
os.environ['PATH'] = f'{go_bin_path}:{name_bin_path}:' + os.environ['PATH']
os.environ['GOPATH'] = cwd
os.environ['GOBIN'] = name_bin_path

domain = input("\ninsert SINGLE domain you would like to run" + f'\033[92m name tool\033[0m'+" on: ")

print(os.system(f'{cwd}/bins/go/bin/go install -v "###github repo link###"'))
try:
    output = os.popen(f'script -q -c "{name_bin_path}/{name} ###input full tool command ###" {name}_output.txt').read()
except Exception as e:
    print("name failed to execute")

with open('{name}.txt', 'w') as f:
    if output != None:
        f.write('\n'.join((output)))

##sanitization##

