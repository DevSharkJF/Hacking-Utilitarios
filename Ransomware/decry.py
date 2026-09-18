import os
import pyaes

file_name = "ransomware-q75.png.ransomware"
file = open(file_name, "rb")
file_data = file.read()
file.close()

key = b"0143256879fravtr"
aes = pyaes.AESModeOfOperationCTR(key)
decrypto_data = aes.decrypt(file_data)

os.remove(file_name)

new_file = "ransomware-q75.png"
new_file = open(new_file, "wb")
new_file.write(decrypto_data)
new_file.close()