import os
import re

# Ask for the root domain
root_domain = input("Enter the root domain you are looking for: ")

# Define the function to parse the output and categorize it
def parse_and_categorize_output(output_file, root_domain):
    try:
        with open(output_file, 'r') as f:
            content = f.read()

        # Regex for finding URLs (without http or https) containing the root domain
        urls = set(re.findall(rf"(?<!\w)(?:[-\w]+\.)*{re.escape(root_domain)}(?:[-\w./?%&=]*)", content))

        # Regex for finding absolute URLs (with http or https) containing the root domain
        absolute_urls = set(re.findall(rf"https?://[^\s/$.?#].[^\s]*{re.escape(root_domain)}[^\s]*", content))

        # Regex for finding endpoints with parameters containing the root domain
        endpoints_with_parameters = set(re.findall(rf"https?://[^\s]+\?[^\s]*{re.escape(root_domain)}[^\s]*", content))

        # Regex for finding .js endpoints containing the root domain
        js_endpoints = set(re.findall(rf"https?://[^\s]+\.js[^\s]*{re.escape(root_domain)}[^\s]*", content))

        # Regex for finding status codes along with their URLs containing the root domain
        status_code_pattern = re.compile(rf"(https?://[^\s/$.?#].[^\s]*{re.escape(root_domain)}[^\s]*)\s*\[?(\d{3})\]?\s*")
        status_codes_with_urls = set(status_code_pattern.findall(content))

        # Write each category to a separate file
        with open('urls.txt', 'a') as f:
            f.write('\n'.join(urls) + '\n')

        with open('absolute_urls.txt', 'a') as f:
            f.write('\n'.join(absolute_urls) + '\n')

        with open('endpoints_with_parameters.txt', 'a') as f:
            f.write('\n'.join(endpoints_with_parameters) + '\n')

        with open('js_endpoints.txt', 'a') as f:
            f.write('\n'.join(js_endpoints) + '\n')

        with open('status_codes.txt', 'a') as f:
            for url, status_code in status_codes_with_urls:
                f.write(f"{url} {status_code}\n")

        # Clear the content of the output file
        with open(output_file, 'w') as f:
            f.truncate(0)

    except FileNotFoundError:
        print(f"Error: {output_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Path to the output file from the module
output_file = 'outputs.txt'

# Call the function to parse and categorize the output
parse_and_categorize_output(output_file, root_domain)
