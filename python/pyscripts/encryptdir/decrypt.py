from ast import Raise
from logging import raiseExceptions
import os

master = str(open('/Users/user/.masterkey.txt', 'r').readline())

def decrypt():
    dir_path = input("directory path to decrypt: ")
    path = r'{}'.format(dir_path)
    file_list = []

    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root,file))

    if os.path.exists('/Volumes/volume/.key.py'):
        key = str(open('/Volumes/volume/.key.py','r').readline())
        if key == master:
            upkey = int(''.join((x for x in key if not x.isalpha())))
            for image_path in file_list:
                path = image_path
                fin = open(path, 'rb')
                image = fin.read()
                fin.close()
                    
                image = bytearray(image)
                
                # performing XOR operation on each value of bytearray
                for index, values in enumerate(image):
                    image[index] = values ^ upkey%30
            

                fin = open(path, 'wb')
                    

                fin.write(image)
                fin.close()
            print('Decryption Done...')
        else:
            raiseExceptions('child key does not match its master')
    else:
        raiseExceptions('key not detected')

decrypt()
