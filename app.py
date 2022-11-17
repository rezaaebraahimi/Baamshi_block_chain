from flask import Flask, render_template, request
from hashlib import sha256
import os


app = Flask(__name__)   


def updatehash(*args):
    hashing_text = ""; h = sha256()
    for arg in args:
        hashing_text += str(arg)
        
    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()


class Block():

    def __init__(self, data=[],number = 0, nonce = 0,pre_hash = 0 *64):
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
        
    
    def __str__(self):
        return str("\nHash: %s \nNonce: %s \nNumber: %s \nData: %s"
                 %( self.hash(), self.nonce, self.add_numb(), self.data))

    

class Blockchain():
    difficulty = 0
    
    
    def __init__(self ):
        self.chain = []
     
        
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



@app.route("/")
@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/result',methods=['POST', 'GET'])
def result():
    blockchain = Blockchain()
    block = Block()
    output = request.form.to_dict()
    name = output["name"]
    family = output["family"]
    age = output["age"]
    iq = output["iq"]
    mbti = output["mbti"]

    database = [f"\nNickname: {name} \nLastname: {family}  \nAge: {age} \nIQ Score: {iq} \nMBTI: {mbti}"]
    
    blc = [""]
    
    for data in database:
        num = block.add_numb()
        blockchain.mine(Block(data, num))
        blockchain.add(Block(data, num))
    for _block in blockchain.chain:
        blc = Block(data, num).__str__()
        return render_template("index.html", blc=blc)
    


if __name__ == "__main__":
    app.run(host:="0.0.0.0", port:=int(os.environ.get('PORT', 5000)))
    
