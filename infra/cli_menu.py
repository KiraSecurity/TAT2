import os
import subprocess

def execute_modules(modules):
    print(modules)
    subprocess.run(["python3", modules], check=True)

def menu(library):
    i = 0
    module_dict = {}
    print('\n'"Welcome to TAT2!")
    print("Here are the modules you have loaded:"'\n')
    keyorder = ['subdomain discovery', 'url prober', 'crawler','fuzzer','bypass']
    chain_lib=sorted(library.items(), key=lambda i:keyorder.index(i[0]))
# Iterate through the sorted categories
    print(chain_lib)
    print("\nsuggest chaining order is as follows:" )
    for category, modules in chain_lib:
        for module, info in modules.items():
            i += 1
            module_dict[i] = module
            print(f"{category}\n{i}  {module}")

    #print(module_dict)
    while True:
        total=len(module_dict)+1
        choice = input(f'"Select the tool you would like to run first, or type {total} to run suggested chain: "')
        if choice.isdigit():
            if choice == total:
                choice = 1
                for module in module_dict:
                    while choice <= len(module_dict):
                        choice = int(choice)
                        selector = module_dict[choice]
                        selector = str(selector)
                        execute_modules(selector)
                        choice +=1

            else:
                choice = int(choice)
                selector = module_dict[choice]
                selector = str(selector)
                execute_modules(selector)
                print("All done here in menu")


