import os
import sys
import subprocess
modules=[]
cwd = os.getcwd()

## resets the local space and download golang in local framework directory and sets it (base framework to accept go code)

print(os.system('go version'))
#print(os.system(f'rm -rf {cwd}/go'))
#print(os.system('wget https://golang.org/dl/go1.22.4.linux-amd64.tar.gz')) # need to get RE code to grab latest golang version

#print(os.system(f'tar -C {cwd} -xzf go1.22.4.linux-amd64.tar.gz'))

os.environ['PATH'] = f'{cwd}/go/bin:' + os.environ['PATH']
os.environ['GOPATH'] = cwd
print(os.system('go version'))

print("finished go lang script acceptance")

def prompt():
    
    modules = [file for file in os.listdir() if file.endswith('.tat')]
   
    if not modules:
        print("No .tat files found in the current directory.")
        return
    print("Modules found:", modules)
    i= 0
    for module in modules:
        subprocess.run(["python3", modules[i]])
        i +=1
if __name__ == "__main__":
    prompt()