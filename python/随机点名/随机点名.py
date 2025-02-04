from flask import Flask
import random
app = Flask("随机点名")
list = ['Daniel','Lei','kunkun']
@app.route("/")
def index():
    return "幸运嘉宾：" + random.choice(list)
app.run()
