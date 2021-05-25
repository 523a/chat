from flask import Flask, render_template, request
import requests
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

#english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#trainer = ChatterBotCorpusTrainer(english_bot)
#trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def post_bot_response():
    userText = request.args.get('msg')
    
    #r = requests.post("http://localhost:5555/model", json={"x_init":  'msg'})
    #print(r.status_code)
    #print(dp(userText))
    #return str(r.text[3:-3])
    
    return (dp(userText))

def dp(ph):
    text={'id':'ч','sent': 0,'text':ph,'time':''}
    r = requests.post('http://172.16.0.145:5000/bot', json=text).json()
    #r = requests.post('http://172.16.0.45:5000/bot', json={'id': 'ч','send': 0, 'text': [textm],'time':''}).json()
    
    return (r[-1]['text'])


if __name__ == "__main__":
    app.run()#(host = '0.0.0.0', port=5100)
