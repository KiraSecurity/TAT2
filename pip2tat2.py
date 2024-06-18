import os
import re
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from infra.module_importer import get_modules, categorize_modules

class OutputFileHandler(FileSystemEventHandler):
    def __init__(self, root_domain, library):
        self.root_domain = root_domain
        self.library = library

    def on_modified(self, event):
        if event.src_path.endswith('outputs.txt'):
            print(f"{event.src_path} has been modified")
            subprocess.run(["python3", "parse_output.py"], check=True)
            trigger_modules(self.library)

def trigger_modules(library):
    for category, modules in library.items():
        for module, dependency in modules.items():
            input_dependency = dependency[0]
            if os.path.getsize(f'{input_dependency}.txt') > 0:
                execute_modules(module)

def execute_modules(module_script):
    try:
        subprocess.run(["python3", module_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing {module_script}: {e}")

if __name__ == "__main__":
    root_domain = input("Enter the root domain you are looking for: ")

    library = {}
    loaded_modules = get_modules()
    for module in loaded_modules:
        library = categorize_modules(module, library)

    event_handler = OutputFileHandler(root_domain, library)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        print("Monitoring outputs.txt for changes...")
        while True:
            pass  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
