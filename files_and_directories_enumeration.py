import requests
import sys


class FindFilesDirectories:
    def __init__(self, target_url):
        self.url = target_url
        self.check_url()

    def request(self, url):
        try:
            return requests.get(url="http://"+url, timeout=3)
        except requests.exceptions.ConnectionError:
            pass

    def check_url(self):
        response = self.request(self.url)
        if response and response.status_code == 200:
            print("[+] URL Validation complete")
            self.get_subdomains()
        else:
            print("[-] Could not establish connection with the given target URL")
            sys.exit()

    def get_subdomains(self):
        with open("files_directories.txt", "r") as wordlist:
            for each_word in wordlist:
                test_url = f"{self.url}/{each_word.strip()}"
                response = self.request(test_url)
                if response:
                    print("[+] Discovered files & directories ==> " + test_url)


files_and_directories = FindFilesDirectories("[Target URL]")
