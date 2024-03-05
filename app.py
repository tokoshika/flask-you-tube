from flask import Flask,render_template,request
from pytube import YouTube
import os


app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/youtube",methods=['GET','POST'])
def download(): 
  

 try:

   user_folder = os.path.expanduser("~")
   folder = os.path.join(user_folder, "Downloads")
      
   name = request.form.get('name') 
   url = name
   print(url)
   yt = YouTube(url)  
   print(yt)
   yt.streams.filter(res='720p', file_extension='mp4').first().download(folder)
   return render_template("index.html",message="Downloaded!!")

 except:
   name = request.form.get('name') 
   url = name
   print(url)
   yt = YouTube(url)  
   return render_template("index.html",message=yt)



if __name__ == "__main__":
  app.run(debug=True) 


