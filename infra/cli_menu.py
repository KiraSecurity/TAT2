import os
import subprocess
import re
def execute_modules(modules):
    print(modules)
    subprocess.run(["python3", modules], check=True)
    subprocess.run(["python3", "parse_output.py"], check=True)

def check_module_dependency(dependency):
    if os.path.exists(dependency):
        print(f'"{dependency} exists"')
        return True
    else:
        print(f"\n{dependency} not found, select another module or continue with single URL")
        
def menu(library):
    i = 0
    module_dict = {}
    print('\n'"Welcome to TAT2!")
    print("Here are the modules you have loaded:"'\n')
    keyorder = ['subdomain discovery', 'url prober', 'crawler', 'fuzzer', 'bypass']
    chain_lib = sorted(library.items(), key=lambda i: keyorder.index(i[0]))

    print(chain_lib)
    print("\nsuggest chaining order is as follows:" )
    for category, modules in chain_lib:
        for module, dependency, in modules.items():
            i += 1
            module_dict[i] = (category, module, dependency)
            print(f"{category}\n{i}  {module}  ")

    while True:
        choice = input(f'\nSelect the tool you would like to run first, or type 7 to run suggested chain: ')
        if choice.isdigit():
            choice = int(choice)
            if choice == 7:
                choice = 1
                while choice <= len(module_dict):
                    category, selector,dependency = module_dict[choice]
                    print(f"\nThe dependency for {selector} is {dependency[0]}\n")
                    if check_module_dependency(dependency[0]):
                        execute_modules(selector)
                    else:
                        dependent = dependency[0]
                        for module, (category, info, output) in module_dict.items():
                           
                            if dependent == output[1]:
                                print(f"\n{info} is suggested to run prior\n") 
                    choice +=1
            else:
                category, selector,dependency = module_dict[choice]
                print(f"The dependency for {selector} is {dependency[0]}")
                if check_module_dependency(dependency[0]):
                    execute_modules(selector)
                    continue
                else:
                    dependent = dependency[0]
                    for module, (category, info, output) in module_dict.items():
                        if dependent == output[1]:
                            print(f"\n {info}is suggested to run prior\n") 

