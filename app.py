from flask import Flask, render_template, jsonify
from random import randint

app =Flask(__name__)

memes = ['meme1.jpg', 'meme2.jpg', 'meme3.jpg']
randommeme = memes[randint(0,2)]

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/meme/random")
def memerandom():
    return render_template('meme.html', rm=randommeme)

if __name__ == "__main__":
    app.run(debug=True)