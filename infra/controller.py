import os
import sys
import subprocess
import re
import requests
import json

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

menu()