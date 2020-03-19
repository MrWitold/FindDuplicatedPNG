import os
import hashlib
from fnmatch import fnmatch

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

pattern = "*.jpg"   
files ={}

print("Rozpoczynam skanowanie... \n\n")

for root,dirs,names in os.walk("."):
    for fname in names:
        if fnmatch(fname, pattern):
            path = root + '/' + fname
            key = md5(path)
            if(key in files):
                files[key].add(path)
            else:
                files[key]  =  lista={path}
#print(files)

print("Wyszukiwanie duplikatow... \n\n")

for key in files:
    if len(files[key]) != 1:
        print("___________________")
        print("Duplikat:")
        for id_ in files[key]:
            print(id_)

print("Operacja zakonczona... \n\n")
