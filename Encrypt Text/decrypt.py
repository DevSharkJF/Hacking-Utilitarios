import os
from cryptography.fernet import Fernet
# py -m pip install cryptography

with open("passw.key", "rb") as key:
    secretkey = key.read()

files = []
for file in os.listdir():
    if file == "ransomware.py" or file == "passw.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

for file in files:
    with open(file, "rb") as archives:
        content = archives.read()
    content_decrypted = Fernet(secretkey).decrypt(content)
    with open(file, "wb") as archives:
        archives.write(content_decrypted)

print(files)