from subscrypt import Subscrypt

sp = Subscrypt()
sp.repack("sample.jpg")
sp.depack("sample.jpg", 4, "license.enc")