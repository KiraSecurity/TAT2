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
    for category in library:
        for module, info in library[category].items():
            i += 1
            module_dict[i] = module
            print(f"\033[92m {i} {module}\033[0m")

    print(module_dict)
    while True:
        choice = input("Select the tool you would like to run first: ")
        if choice.isdigit():
            choice = int(choice)
            selector = module_dict[choice]
            selector = str(selector)
            execute_modules(selector)
            print("All done here in menu")

if __name__ == "__main__":
    from metadata_handler import get_modules, categorize_modules

    loaded_modules = get_modules()
    library = {}
    for module in loaded_modules:
        library = categorize_modules(module, library)
    menu(library)
