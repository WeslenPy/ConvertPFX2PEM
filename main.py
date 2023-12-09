from app.certs.pfx import LoaderPFX


class Convert:
        
    def start(self):
        password = input("Digite a senha do arquivo pfx: ")
        
        pfx = LoaderPFX(password=password)
        
        pfx_data = pfx.load_pfx()
        pfx_decrypt = pfx.decrypt_pfx(pfx_data=pfx_data)
        pfx_to_pem = pfx.generate_pem(decrypt_pfx=pfx_decrypt)
        
        pfx.save(*pfx_to_pem)        
        
        
        
        
if __name__ == "__main__":
    convert  = Convert()
    convert.start()