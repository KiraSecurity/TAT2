import re

def output_distributor(output):
    absolute_urls = set()
    domains = set()
    endpoints = set()
    js_files = set()
    params = set()

    # Define regex patterns
    url_pattern = re.compile(r"https?://[^\s]+")
    domain_pattern = re.compile(r"(?!https?://)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    endpoint_pattern = re.compile(r"(https?://[^\s]+/[^?#\s]+)")
    js_pattern = re.compile(r"https?://[^\s]+\.js")
    param_pattern = re.compile(r"https?://[^\s]+\?[^\s]+")

    for line in output.splitlines():
        urls = url_pattern.findall(line)
        for url in urls:
            absolute_urls.add(url)
            if js_pattern.match(url):
                js_files.add(url)
            if param_pattern.match(url):
                params.add(url)
            if endpoint_pattern.match(url):
                endpoints.add(url)

        # Find domains that are not part of URLs
        for domain in domain_pattern.findall(line):
            if not any(url.startswith(f"http://{domain}") or url.startswith(f"https://{domain}") for url in absolute_urls):
                domains.add(domain)
                
    # Write to respective files
    with open('absolute_urls.txt', 'a') as f:
        f.write('\n'.join(sorted(absolute_urls)))
    with open('domains.txt', 'a') as f:
        f.write('\n'.join(sorted(domains)))
    with open('endpoints.txt', 'a') as f:
        f.write('\n'.join(sorted(endpoints)))
    with open('js_files.txt', 'a') as f:
        f.write('\n'.join(sorted(js_files)))
    with open('params.txt', 'a') as f:
        f.write('\n'.join(sorted(params)))

# Example usage

