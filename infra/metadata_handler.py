import os

def get_module_category(module):
    all_metadata = []
    with open(module, 'r') as f:
        line = 0
        while line < 2:
            metadata = f.readline().strip()
            if metadata.startswith("#category:") or metadata.startswith("#input dependencies:"):
                all_metadata.append(metadata.split(':')[1].strip())
                line += 1
            else:
                print("incorrect metadata format")
                continue
        return all_metadata

def categorize_modules(module, library):
    metadata = get_module_category(module)
    update_module_library(library, metadata, module)
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

if __name__ == "__main__":
    modules = get_modules()
    library = {}
    for module in modules:
        library = categorize_modules(module, library)
    print(library)
