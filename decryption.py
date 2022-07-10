import os
import os.path
from cryptography.fernet import Fernet

files = []

with open('key.key','rb') as thekey:
    decryption_key = thekey.read()

for Root,Folders,Files in os.walk(os.getcwd()):
    for file in Files:
        if file == __file__ or file == 'key.key' or file == 'ransomware.py':
            continue
        if os.path.isfile(file):
            files.append(os.path.join(Root,file))


for file in files:
    with open(file,'rb') as thefile:
        contents = thefile.read()
    decrypted_content = Fernet(decryption_key).decrypt(contents)
    with open(file,'wb') as thefile:
        thefile.write(decrypted_content)

