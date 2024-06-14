import os
import sys
import subprocess

cwd = os.getcwd()

## resets the local space and download golang in local framework directory and sets it (base framework to accept go code)
print(os.system('go version'))
print(os.system(f'rm -rf {cwd}/go'))
print(os.system('wget https://golang.org/dl/go1.22.4.linux-amd64.tar.gz')) # need to get RE code to grab latest golang version

print(os.system(f'tar -C {cwd} -xzf go1.22.4.linux-amd64.tar.gz'))

os.environ['PATH'] = f'{cwd}/go/bin:' + os.environ['PATH']
os.environ['GOPATH'] = cwd
print(os.system('go version'))

print("finished go lang script acceptance")

def prompt():
    #module= input("include module name you would like to add: ")
    #module2= input("include second module name you would like to add: ")
    #module3= input("include third module name you would like to add: ")
    #subprocess.run(["python3", module])
    #subprocess.run(["python3", module2])
    #subprocess.run(["python3", module3])

    if __name__ == "__main__":
        prompt()