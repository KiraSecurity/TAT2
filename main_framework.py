from infra.go_setup import setup_go
from infra.module_importer import get_modules, categorize_modules
from infra.cli_menu import menu
import subprocess

def deploy_framework(non_interactive=False):
    setup_go()
    library = {}
    loaded_modules = get_modules()
    for module in loaded_modules:
        library = categorize_modules(module, library)
  
    if non_interactive:
        subprocess.run(["python3", "pip2tat2.py"], check=True)
    else:
        menu(library)

if __name__ == "__main__":
    import sys
    non_interactive = '--non-interactive' in sys.argv
    deploy_framework(non_interactive)
