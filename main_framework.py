from infra.go_setup import setup_go
from infra.metadata_handler import get_modules, categorize_modules
from infra.modules_importer import menu

def deploy_framework():
    setup_go()
    loaded_modules = get_modules()
    library = {}
    for module in loaded_modules:
        library = categorize_modules(module, library)
    menu(library)

if __name__ == "__main__":
    deploy_framework()
