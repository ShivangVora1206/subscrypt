from subscrypt import Subscrypt

sp = Subscrypt()
sp.encrypt("sample.jpg")
sp.decrypt("sample.jpg", 4, "license.enc")