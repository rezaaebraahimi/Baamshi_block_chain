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
    
    block.data = [f"{name}", f"{family}", f"{age}", f"{iq}", f"{mbti}"]

    for data in block.data:
        block_data = [block.add_numb(), block.hash(), block.nonce, block.pre_hash]
        block.data += block_data
        blockchain.mine()
        blockchain.add()
        return render_template("hash.html", database=block.data)
    


if __name__ == "__main__":
    app.run(host:="0.0.0.0", port:=int(os.environ.get('PORT', 5000)))
    
