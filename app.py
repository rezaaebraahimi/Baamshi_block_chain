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



class Person():
    def __init__(self, name, family, age, iq, mbti):
        self.name = name
        self.family = family
        self.age = int(age)
        self.iq = int(iq)
        self.mbti = mbti
    


low_iq = list(range(40, 70, 1))
average_iq = list(range(70, 120, 1))
hi_iq = list(range(120, 161, 1))


istj = ["Business Analyst or Supply Chain Manager", "Dentist", "Accountant"]
infj = ["Scientist or Author", "Psychologist", "Consultant or Librarian"]
intj = ["Financial Advisor or Musician", "Marketing Manager or Physiotherapist", "Photographer or Editor or Teacher"]
enfj = ["Art Director or Sales Manager", "Public Relations Manager or Human Resources Manager", "Education Consultant"]
istp = ["Forensic Scientist or Technician and Technical Specialist", "Engineer or Inspector" ,"Skilled Construction Worker"]
esfj = ["Medical Researcher or Psychologist", "Office Manager or Technical Support Specialist", "Museum"]
infp = ["Artist or Copyrighter", "Human Resources Manager or Mental Health Specialist", "Photographer or Physiotherapist"]
esfp = ["Sales Representative or Professional Comedian", "Event Planner or Beauty Specialist","Aircraft Stewardess or Tour Leader"]
enfp = ["Musician or Manufacturing Manager","Reporter or Editor" ,"Primary School Teacher or Personal Instructor or Social Worker"]
estp = ["Creative Director or Construction Manager","Paramedicect or Project Coordinator","Firefighters"]
estj = ["Judge Court or Financial Manager" ,"Hotel Manager or Real Estate Agent","Sports Trainer"]
entj = ["Astronomy or Business manager","Mechanical Engineer or Judge Court","Public Relations Specialist or Construction Manager"]
intp = ["Composer or Web Developer","Producer or Marketing Consultant","Author"]
isfj = ["Administrative Manager or Bank Employee","Photographer or Office Manager","Elementary Teacher or Accountant"]
entp = ["Creative Director or Financial Planner","System Analyst or Lawyer","Operations Specialist"]
isfp = ["Social Network Manager or Archaeologist","Glasses Maker or Veterinarian","Librarian or Occupational Therapist"]


@app.route("/")
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    #blockchain = Blockchain()
    block = Block()
    person = Person(name = output["name"],
                    family = output["family"],
                    age = int(output["age"]),
                    iq = int(output["iq"]),
                    mbti = output["mbti"].lower())

    if person.iq in low_iq:
        iq_level = "Your IQ  Level is LOW!!!"
    elif person.iq in average_iq:
        iq_level = "Your IQ  Level is Average!"
    elif person.iq in hi_iq:
        iq_level = "Your IQ  Level is High!"
    else:
        iq_level = "Your IQ Level is not in human range!"

    if person.mbti == "istj" and person.iq in low_iq:
        job_offer = istj[2]
    elif person.mbti == "istj" and person.iq in average_iq:
        job_offer = istj[1]
    elif person.mbti == "istj" and person.iq in hi_iq:
        job_offer = istj[0]
    elif person.mbti == "infj" and person.iq in low_iq:
        job_offer = infj[2]
    elif person.mbti == "infj" and person.iq in average_iq:
        job_offer = infj[1]
    elif person.mbti == "infj" and person.iq in hi_iq:
        job_offer = infj[0]
    elif person.mbti == "intj" and person.iq in low_iq:
        job_offer = intj[2]
    elif person.mbti == "intj" and person.iq in average_iq:
        job_offer = intj[1]
    elif person.mbti == "intj" and person.iq in hi_iq:
        job_offer = intj[0]
    elif person.mbti == "enfj" and person.iq in low_iq:
        job_offer = enfj[2]
    elif person.mbti == "enfj" and person.iq in average_iq:
        job_offer = enfj[1]
    elif person.mbti == "enfj" and person.iq in hi_iq:
        job_offer = enfj[0]
    elif person.mbti == "istp" and person.iq in low_iq:
        job_offer = istp[2]
    elif person.mbti == "istp" and person.iq in average_iq:
        job_offer = istp[1]
    elif person.mbti == "istp" and person.iq in hi_iq:
        job_offer = istp[0]
    elif person.mbti == "esfj" and person.iq in low_iq:
        job_offer = esfj[2]
    elif person.mbti == "esfj" and person.iq in average_iq:
        job_offer = esfj[1]
    elif person.mbti == "esfj" and person.iq in hi_iq:
        job_offer = esfj[0]
    elif person.mbti == "infp" and person.iq in low_iq:
        job_offer = infp[2]
    elif person.mbti == "infp" and person.iq in average_iq:
        job_offer = infp[1]
    elif person.mbti == "infp" and person.iq in hi_iq:
        job_offer = infp[0]
    elif person.mbti == "esfp" and person.iq in low_iq:
        job_offer = esfp[2]
    elif person.mbti == "esfp" and person.iq in average_iq:
        job_offer = esfp[1]
    elif person.mbti == "esfp" and person.iq in hi_iq:
        job_offer = esfp[0]
    elif person.mbti == "enfp" and person.iq in low_iq:
        job_offer = enfp[2]
    elif person.mbti == "enfp" and person.iq in average_iq:
        job_offer = enfp[1]
    elif person.mbti == "enfp" and person.iq in hi_iq:
        job_offer = enfp[0]
    elif person.mbti == "estp" and person.iq in low_iq:
        job_offer = estp[2]
    elif person.mbti == "estp" and person.iq in average_iq:
        job_offer = estp[1]
    elif person.mbti == "estp" and person.iq in hi_iq:
        job_offer = estp[0]
    elif person.mbti == "estj" and person.iq in low_iq:
        job_offer = estj[2]
    elif person.mbti == "estj" and person.iq in average_iq:
        job_offer = estj[1]
    elif person.mbti == "estj" and person.iq in hi_iq:
        job_offer = estj[0]
    elif person.mbti == "entj" and person.iq in low_iq:
        job_offer = entj[2]
    elif person.mbti == "entj" and person.iq in average_iq:
        job_offer = entj[1]
    elif person.mbti == "entj" and person.iq in hi_iq:
        job_offer = entj[0]
    elif person.mbti == "intp" and person.iq in low_iq:
        job_offer = intp[2]
    elif person.mbti == "intp" and person.iq in average_iq:
        job_offer = intp[1]
    elif person.mbti == "intp" and person.iq in hi_iq:
        job_offer = intp[0]
    elif person.mbti == "isfj" and person.iq in low_iq:
        job_offer = isfj[2]
    elif person.mbti == "isfj" and person.iq in average_iq:
        job_offer = isfj[1]
    elif person.mbti == "isfj" and person.iq in hi_iq:
        job_offer = isfj[0]
    elif person.mbti == "entp" and person.iq in low_iq:
        job_offer = entp[2]
    elif person.mbti == "entp" and person.iq in average_iq:
        job_offer = entp[1]
    elif person.mbti == "entp" and person.iq in hi_iq:
        job_offer = entp[0]
    elif person.mbti == "isfp" and person.iq in low_iq:
        job_offer = isfp[2]
    elif person.mbti == "isfp" and person.iq in average_iq:
        job_offer = isfp[1]
    elif person.mbti == "isfp" and person.iq in hi_iq:
        job_offer = isfp[0]
    else:
        job_offer = "Your mbti isn't true, please Try Again!"

    
    block.data = [f"{person.name}",
                  f"{person.family}",
                  f"{person.age}",
                  f"{person.iq}",
                  f"{person.mbti}"]

    for data in block.data:
        block_data = [block.hash()]
        block.data += block_data
        return render_template("result.html", database=block.data,iq_level=iq_level,job_offer=job_offer)
    


if __name__ == "__main__":
    app.run(host:="0.0.0.0", port:=int(os.environ.get('PORT', 5000)))
    
