from flask import Flask, render_template, jsonify
from random import randint, random
import threading

app =Flask(__name__)

memes = ['meme1.jpg', 'meme2.jpg', 'meme3.jpg']
randommeme = memes[randint(0,2)]
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/meme/random")
def memerandom():
    randommeme = memes[randint(0,2)]
    
    return f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <img src="\static\img\{randommeme}" alt="" />
    <p>{randommeme}</p>
  </body>
</html>

    """

if __name__ == "__main__":
    app.run(debug=True)