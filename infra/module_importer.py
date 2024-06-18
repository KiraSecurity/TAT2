import os

def get_module_metadata(module):
    all_metadata = []
    with open(module, 'r') as f:
        line = 0
        while line < 3:
            metadata = f.readline().strip()
            if metadata.startswith("#category:") or metadata.startswith("#input dependencies:") or metadata.startswith("#output:"):
                all_metadata.append(metadata.split(':')[1].strip())
                line += 1
                #print(metadata)
            else:
                print("incorrect metadata format")
                continue
        return all_metadata

def categorize_modules(module, library):
    metadata = get_module_metadata(module)
    update_module_library(library, metadata, module)
    return library

def update_module_library(library, metadata, module):
    category = metadata[0]
    dependency = metadata[1]
    output = metadata[2]
    if category not in library:
        library[category] = {module: [dependency, output]}
        print(f"Created new category '{category}' with module '{module}'\n")
    else:
        library[category][module] =  [dependency, output]
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


