from cryptography.fernet import Fernet
import os
class Subscrypt:
    def __init__(self, divs=4, salt_length=4) -> None:
        self.salt_length = salt_length
        self.divs = divs
        if not os.path.exists("a_key.key") :
            self.write_key("a_key")
            
        if not os.path.exists("b_key.key"):
            self.write_key("b_key")
    
    def write_key(self, id):
        if id:
            key = Fernet.generate_key()
            with open(id+".key", "wb") as key_file:
                key_file.write(key)
                print("written", id)
        else:
            raise Exception("write key id is empty")
    
    def load_key(self, id):
        if id:
            if id == "a_key":
                return open(id+".key", "rb").read()
            elif id == "b_key":
                return open(id+".key", "rb").read()
        else:
            raise Exception("id is empty")
        
    def salt(self, cache):
        if cache:
            for i in cache:
                if i and cache[i]:
                    if len(cache[i]) >= self.salt_length:
                        _salt = cache[i][:self.salt_length]
                        cache[i] =  cache[i][:1] + _salt + cache[i][1:]
            return cache
        else:
            raise Exception("Cache is empty")
    
    def unsalt(self, data):
        if data:
            if len(data) >= self.salt_length:
                return data[:1]+data[self.salt_length+1:]
            return data
        else:
            raise Exception("Data is empty")
        
    def repack(self, filename):
        if not filename:
            raise Exception("Filename is empty")
        try:
            key1 = self.load_key("a_key")
            f1 = Fernet(key1)
            key2 = self.load_key("b_key")
            f2 = Fernet(key2)
            cache = {}
            config = []
            out = ""
            dirname = filename.split(".")[0]
            with open(filename, "rb") as file:
                data = file.read()
            limit = len(data) // self.divs
            count = 1
            for i in range(self.divs-1):
                _count = f2.encrypt(str(count).encode()).decode()
                cache[_count] = data[i*limit:(i+1)*limit]
                config.append(_count)
                count += 1
            _count = f2.encrypt(str(count).encode()).decode()
            cache[_count] = data[(self.divs-1)*limit:]
            config.append(_count)
            cache = self.salt(cache)
            # print(cache[_count])
            os.mkdir(dirname)
            for i in config:
                with open(dirname+"\\"+i+".enc", "wb") as file:
                    file.write(cache[i])
            config.append(self.divs)
            with open(dirname+"\\"+"license.enc", "wb") as file:
                file.write(f1.encrypt(str(config).encode()))
        except Exception as e:
            print(e)
            raise Exception("Error in encrypting")
    
    def depack(self, filename, divs, licenseFile):
        if not filename:
            raise Exception("Filename is empty")
        if not licenseFile:
            raise Exception("License file is empty")
        try:
            key1 = self.load_key("a_key")
            f1 = Fernet(key1)
            dirname = filename.split(".")[0]+"\\"
            with open(dirname+licenseFile, "rb") as file:
                config = f1.decrypt(file.read()).decode()
                config = config[1:-1].split(", ")
                _divs = int(config[-1])
                if _divs != divs:
                    print("insufficient number of files")
                    return
                config = config[:-1]
            out = b""
            for i in config:
                with open(dirname+i[1:-1]+".enc", "rb") as file:
                    out += self.unsalt(file.read())
            with open(dirname+"out_"+filename, "wb") as file:
                file.write(out)
        except Exception as e:
            print(e)
            print("incorrect license file")

