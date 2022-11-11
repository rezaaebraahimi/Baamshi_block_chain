from hashlib import sha256 

def updatehash(*args):
    hashing_text = ""; h = sha256()
    for arg in args:
        hashing_text += str(arg)
        
    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()

        

class Block():
    data = None
    hash = None
    nonce = 0
    pre_hash = "0" * 64
    
    
    def __init__(self, data, number=0):
        self.data = data
        self.number = number
    
    
    def hash(self):
        return updatehash(self.pre_hash,
                          self.number,
                          self.data,
                          self.nonce)
     
    
    def __str__(self):
        return str("Block Number: %s\nHash: %s\nPreHash: %s\nData: %s\nNonce: %s\n"
                 %(self.number, self.hash(), self.pre_hash, self.data, self.nonce))

    

class Blockchain():
    difficulty = 0
    
    
    def __init__(self, chain=[]):
        self.chain = chain
     
        
    def add(self, block):
        self.chain.append(block)
        
        
    def remove(self, block):
        self.chain.remove(block)
      

    def mine(self,block):
        try:
            block.pre_hash = self.chain[-1].hash()
        except IndexError:
            pass
        
        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block)
                break
            else:
                block.nonce +=1
    
    
    def isValid(self):
        for i in range(1,len(self.chain)):
            _pre_hash = self.chain[i].pre_hash
            _current = self.chain[i-1].hash
            if _pre_hash != _current or _current[:self.difficulty] != "0"*self.difficulty: 
                return False   

        return True
    

class Main():
    def __init__(self, _name, _family, _age):
        self._name   = _name
        self._family = _family
        self._age    = _age
        
        blockchain   = Blockchain()
        
        _name   = input("Name: ")
        _family = input("Family: ")
        _age    = input("Age: ")
        
        database     = [{"Name": _name,
                         "Family": _family,
                         "Age": _age
                       }]
        
        num = 0
        for data in database:
            num += 1
            blockchain.mine(Block(data,num))
        
        if blockchain.isValid() == True:   
            for block in blockchain.chain:
                print(block)    



if __name__ == "__main__":  
    Main(_name='',_family='', _age="")