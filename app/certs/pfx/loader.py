from cryptography.hazmat.primitives.serialization.pkcs12 import load_key_and_certificates
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from app.utils.functions.path import find_pfx


class LoaderPFX:
    def __init__(self,password) -> None:
        self.pfx_path = find_pfx()
        self.password = str.encode(password)
    
    
    def load_pfx(self):
        with open(self.pfx_path, 'rb') as pfx_file:
            return pfx_file.read()
        
        
    def decrypt_pfx(self,pfx_data):
        
        result =  load_key_and_certificates(pfx_data,self.password, default_backend())
        return result
    
    def generate_pem(self,decrypt_pfx):
        private_key = decrypt_pfx[0]
        cert = decrypt_pfx[1]
        bag_attributes = decrypt_pfx[2]
        
        # Convert private key to PEM format
        pem_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8')

        # Convert certificate to PEM format
        pem_cert = cert.public_bytes(serialization.Encoding.PEM).decode('utf-8')
        
        return bag_attributes,pem_key, pem_cert
    
    
    def save(self,*args):
        with open("certificate.pem","+ab") as new:
            for arg in args:
                if arg:
                    new.write(str.encode(arg))
                
        return True

