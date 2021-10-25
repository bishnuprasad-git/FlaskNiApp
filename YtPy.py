from flask import Flask, jsonify
from youtubesearchpython import VideosSearch

app = Flask(__name__)  
 
@app.route('/home')  
def home():  
    return "hello, welcome to our website";  

@app.route('/youtube/<search>')
def sendYtLinks(search):
    videosSearch = VideosSearch(search, limit = 100)
    url=videosSearch.result()
    # print(url)
    return url
  
if __name__ =="__main__":  
    app.run(debug = True)  