from subscrypt import Subscrypt

sp = Subscrypt()
sp.frag("sample.jpg")
sp.defrag("sample.jpg", 4, "license.enc")