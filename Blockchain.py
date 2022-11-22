import hashlib


class Person():
    def __init__(self, name, family, age, iq, mbti):
        self.name = str(name)
        self.family = str(family)
        self.age = int(age)
        self.iq = int(iq)
        self.mbti = str(mbti)


class Blockchain():
    chain = []
    
    

class Block():
    def __init__(self, data=None,pre_hash = "0" *64):
        self.data = data
        self.pre_hash = pre_hash 

        
    def hash(self):
        update = (f'{self.pre_hash}{self.data}').encode("utf-8")
        return hashlib.sha256(update).hexdigest()
        
   

