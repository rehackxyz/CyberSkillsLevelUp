import requests
import string
import time

# how can we bypass the GET request block and send the payload to sleep?

CHARSET = string.ascii_letters + string.digits

password = ""
counter =  None # to keep track of character position, change it accordingly
password_len = None # set password length, change it accordingly

while (len(password) != password_len): # if the password we extracted has not reached the length, continue
    for char in CHARSET:
        sleeptime = None # sleep time to measure if valid or invalid, change it accordingly

        payload = f""

        URL = f""

        t1 = time.time()

        # send the request and payload here to induce sleep in the database

        t2 = time.time() 

        diff = t2 - t1

        if (diff >= sleeptime): # if sleep occured then increase character position and add the char to the password
            counter += 1
            password += char
            print(f"[*] Found char {password}")
        else:

            continue

print(f"[*] Found admin password: {password}")           