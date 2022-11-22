import hashlib


class Person():
    def __init__(self, name, family, age, iq, mbti):
        self.name = str(name)
        self.family = str(family)
        self.age = int(age)
        self.iq = int(iq)
        self.mbti = str(mbti)


class Block():
    number = 0
    def __init__(self, data=None, nonce = 0,pre_hash = "0" *64):
        self.data = data
        self.nonce = nonce
        self.pre_hash = pre_hash 

        
    def hash(self):
        update = (f'{self.pre_hash}{self.number}{self.data}{self.nonce}').encode("utf-8")
        return hashlib.sha256(update).hexdigest()
        
    
    def add_numb(self):
        self.number += 1
        return self.number
   

class Blockchain():
    difficulty = 3
    chain = []
       
    def mine(self,block=Block()):
        try:
            block.pre_hash = Block.hash()
        except IndexError:
            pass
        
        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block)
                break
            else:
                self.remove(block)
                block.nonce +=1
                break
    
    
    def isValid(self):
        for i in range(1,len(self.chain)):
            _pre_hash = Block.hash(self.chain[-1])
            _current = Block.hash(self.chain[len(self.chain)])
            if _pre_hash != _current or _current[:self.difficulty] != "0"*self.difficulty: 
                return False   

        return True