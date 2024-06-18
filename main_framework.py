from infra.go_setup import setup_go
from infra.module_importer import get_modules, categorize_modules
from infra.cli_menu import menu
def deploy_framework():
    ##deploys golang binary for local framework
    #setup_go()
    library = {}
    loaded_modules = get_modules()
    for module in loaded_modules:
        library = categorize_modules(module, library)
  
    #print(library)
    menu(library)



if __name__ == "__main__":
    deploy_framework()
