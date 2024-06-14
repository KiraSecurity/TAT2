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

def get_module_category(module):
    with open(module, 'r') as f:
        metadata = f.readline().strip()
        if metadata.startswith("#category:"):
            return metadata.split(':')[1].strip()
        else:
            return "unknown"

def categoize_modules(modules):
    categories= {}
    for module in modules:
        category=get_module_category(module)
        update_module_library(categories,category,module)
    print(categories)
    return categories

def update_module_library(categories,category,module):
    if category not in categories:
            categories[category]=[module]
            print(categories)
    else:
        categories[category] = [categories[category]]
        categories[category].append(module)
        print(categories)  




def get_modules():
    modules = [file for file in os.listdir() if file.endswith('.tat')]
    if not modules:
        print("No .tat files found in the current directory.")
        return
    print("Modules found:", modules)
    return modules
    

###running modules###
def execute_modules(modules):
    for module in modules:
        subprocess.run(["python3", module], check=True)

def deploy_framework():
    loaded_modules=get_modules()
    categories=categoize_modules(loaded_modules)
    process_flow = [
        "subdomain discovery",
        "url prober",
        "crawler",
        "others"
    ]
    for category in process_flow:
        if category in categories:
            execute_modules(categories[category],)






if __name__ == "__main__":
    deploy_framework()


    #work-flow
    #import modules
    # scan meta-data
    # categorize modules to create execution flow
    # deploy and run
