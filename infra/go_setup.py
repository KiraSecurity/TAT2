import os
import re
import requests
import subprocess

def get_latest_go_version():
    response = requests.get('https://golang.org/dl/')
    latest_version = re.search(r'go([0-9.]+)\.linux-amd64\.tar\.gz', response.text)
    if latest_version:
        return latest_version.group(1)
    else:
        raise Exception("Unable to find the latest Go version.")

def setup_go():
    cwd = os.getcwd()
    print("Setting up Go environment...")

    if os.path.exists(os.path.join(cwd, 'bins', 'go')):
        subprocess.run(['rm', '-rf', os.path.join(cwd, 'bins', 'go')], check=True)

    latest_go_version = get_latest_go_version()
    print(f"Latest Go version: {latest_go_version}")

    if not os.path.exists(os.path.join(cwd, 'bins')):
        os.makedirs(os.path.join(cwd, 'bins'))

    download_url = f'https://golang.org/dl/go{latest_go_version}.linux-amd64.tar.gz'
    subprocess.run(['wget', download_url, '-P', os.path.join(cwd, 'bins')], check=True)
    subprocess.run(['tar', '-C', os.path.join(cwd, 'bins'), '-xzf', os.path.join(cwd, 'bins', f'go{latest_go_version}.linux-amd64.tar.gz')], check=True)

    os.environ['PATH'] = os.path.join(cwd, 'bins', 'go', 'bin') + ':' + os.environ['PATH']
    os.environ['GOPATH'] = os.path.join(cwd, 'bins')
    subprocess.run(['go', 'version'], check=True)

    print("Go environment setup complete.")

if __name__ == "__main__":
    setup_go()
