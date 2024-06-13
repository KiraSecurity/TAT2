import os
import sys
cwd = os.getcwd() 
os.environ['PATH'] = f'{cwd}/go/bin:' + os.environ['PATH']
os.environ['GOPATH'] = cwd
print(os.system(f'{cwd}/go/bin/go install -v github.com/owasp-amass/amass/v4/...@master'))
os.environ['PATH'] = f'{cwd}/bin:' + os.environ['PATH']
print(os.system(f'{cwd}/bin/amass enum -d facebook.com'))