from hashlib import sha256


def updatehash(*args):
    hashing_text = ""; h = sha256()
    for arg in args:
        hashing_text += str(arg)
        
    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()


class Block():
    def __init__(self, data=None,number=0, nonce = 0,pre_hash = "0" *64):
        self.data = data
        self.number = number
        self.nonce = nonce
        self.pre_hash = pre_hash    


    def hash(self):
        return updatehash(self.pre_hash,
                          self.number,
                          self.data,
                          self.nonce,
                          )
        
    
    def add_numb(self):
        add_number = self.number + 1
        return add_number


    

class Blockchain():
    difficulty = 3

    
    def __init__(self):
        self.chain = []
        
        
    def add(self, block=Block()):
        self.chain.append(block)
        
        
    def remove(self, block=Block()):
        self.chain.remove(block)
      

    def mine(self,block=Block()):
        try:
            block.pre_hash = (self.chain[-1]).hash()
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
            _pre_hash = self.chain[i].pre_hash
            _current = self.chain[i-1].hash
            if _pre_hash != _current or _current[:self.difficulty] != "0"*self.difficulty: 
                return False   

        return True