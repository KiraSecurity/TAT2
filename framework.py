import os
import sys
import subprocess
import re
import requests
cwd = os.getcwd()

## resets the local space and download golang in local framework directory and sets it (base framework to accept go code)

import os
import re
import requests

def get_latest_go_version():
    response = requests.get('https://golang.org/dl/')
    latest_version = re.search(r'go([0-9.]+)\.linux-amd64\.tar\.gz', response.text)
    if latest_version:
        return latest_version.group(1)
    else:
        raise Exception("Unable to find the latest Go version.")

def setup_go():
    cwd = os.getcwd()

    print(os.system('go version'))
    print(os.system(f'rm -rf {cwd}/bins/go'))

    latest_go_version = get_latest_go_version()
    print(f"Latest Go version: {latest_go_version}")

    if not os.path.exists(f'{cwd}/bins'):
        os.makedirs(f'{cwd}/bins')

    download_url = f'https://golang.org/dl/go{latest_go_version}.linux-amd64.tar.gz'
    print(os.system(f'wget {download_url} -P {cwd}/bins'))

    print(os.system(f'tar -C {cwd}/bins -xzf {cwd}/bins/go{latest_go_version}.linux-amd64.tar.gz'))

    os.environ['PATH'] = f'{cwd}/bins/go/bin:' + os.environ['PATH']
    os.environ['GOPATH'] = f'{cwd}/bins'
    print(os.system('go version'))

print("finished go lang script acceptance")

def get_module_category(module):
    all_metadata=[]
    with open(module, 'r') as f:
        line=0
        while line < 2:
            metadata = f.readline().strip()
            if metadata.startswith("#category:") or metadata.startswith("#input dependencies:"):
                all_metadata.append(metadata.split(':')[1].strip())
                #print(all_metadata)
                line +=1
            else:

                print("incorrect metadata format")
                continue

        return all_metadata

def categoize_modules(module,library):
    #module_info={}
    
    metadata=get_module_category(module)
    update_module_library(library,metadata,module)
    return library

def update_module_library(library, metadata, module):
    category = metadata[0]
    info = metadata[1]

    if category not in library:
        library[category] = {module: info}
        print(f"Created new category '{category}' with module '{module}'")
    else:
        library[category][module] = info
        print(f"Added module info for '{module}' in category '{category}'")

    return library
      




def get_modules():
    modules = []
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith('.tat'):
                modules.append(os.path.join(root, file))
                
    if not modules:
        print("No .tat files found in the current directory.")
        return
    
    print("Modules found:", modules)
    return modules

###running modules###
def execute_modules(modules):
        print(modules)
        subprocess.run(["python3", modules], check=True)




def menu(library):
    i=0
    module_dict={}
    print('\n'"welcome to TAT2!")
    print("here are the modules you have loaded:"'\n')
    for category in library:
    # Print the first module and its value in the category
        for module, info in library[category].items():
            i+=1
            module_dict[i]=module
            print(f"\033[92m {i} {module}\033[0m")

    print(module_dict)
    while True:
        choice=input("select the tool you would like to run first: ")
        if choice.isdigit():
            choice = int(choice)
            #choice=input("select the tool you would like to run first: ")
            selector=module_dict[choice]
            selector = str(selector)
            execute_modules(selector)
            print("all done here in menu")
    

def deploy_framework():
    setup_go()
    loaded_modules=get_modules()
    library ={}
    for module in loaded_modules:
        library=categoize_modules(module,library)
    menu(library)

    process_flow = [
        "subdomain discovery",
        "url prober",
        "crawler",
        "others"
    ]
    # for category in process_flow:
    #     if category in library:
    #         execute_modules(library[category],)


if __name__ == "__main__":
    deploy_framework()


    #work-flow
    #import modules
    # scan meta-data
    # categorize modules to create execution flow
    # deploy and run
