

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
    keyorder = ['subdomain discovery', 'url prober', 'crawler', 'fuzzer', 'bypass']
    chain_lib = sorted(library.items(), key=lambda i: keyorder.index(i[0]))

    print(chain_lib)
    print("\nsuggest chaining order is as follows:" )
    for category, modules in chain_lib:
        for module, info in modules.items():
            i += 1
            module_dict[i] = (category, module)
            print(f"{category}\n{i}  {module}")

    while True:
        choice = input(f'Select the tool you would like to run first, or type 7 to run suggested chain: ')
        if choice.isdigit():
            choice = int(choice)
            if choice == 7:
                choice = 1
                while choice <= len(module_dict):
                    category, selector = module_dict[choice]
                    execute_modules(selector)
                    # Automatically run all URL probers after any crawler
                    if category == "crawler":
                        url_prober_selectors = [mod for cat, mod in module_dict.values() if cat == "url prober"]
                        for url_prober_selector in url_prober_selectors:
                            execute_modules(url_prober_selector)
                    choice += 1
            else:
                category, selector = module_dict[choice]
                execute_modules(selector)
                # Automatically run all URL probers after any crawler
                if category == "crawler":
                    url_prober_selectors = [mod for cat, mod in module_dict.values() if cat == "url prober"]
                    for url_prober_selector in url_prober_selectors:
                        execute_modules(url_prober_selector)
                print("All done here in menu")

