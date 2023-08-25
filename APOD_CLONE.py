import requests
import json


#Note: You have to pass in key into url using the ?api_key= ___ format
api_key = "api_key" #personal key changed in github version for privacy
url = "https://api.nasa.gov/planetary/apod?api_key=insert_apikey"

response = requests.get(url)

apod_dict = json.dumps(response.json(), indent=4, )

print(apod_dict)

#This turns the json into a python dict
apod_dict = json.loads(apod_dict)

#print(apod_dict) -- commented out
image = apod_dict["hdurl"]
date = apod_dict["date"]
title = apod_dict["title"]
#copyright = apod_dict["copyright"]
explanation = apod_dict["explanation"]


#HTML stuff
# Opening the existing HTML file. I had to put html template into templates folder. I guess Flask defaults to templates folder.
#Since I put it in the folder, I specified path in open()
Func = open("templates/home.html","w")
  
# Adding input data to the HTML file. I concatonate url since I have stored as a string in a variable.
Func.write("<html>\n")
Func.write("<h1><center>Astronomy Picture of the Day</center></h1>\n")
Func.write("<body><center>Discover the cosmos! Each day a different image or photograph of our fascinating universe is featured, along with a brief explanation written by a professional astronomer.</center></body>\n")
#date
Func.write("<center>" + date + "</center>")
#image
Func.write("<p style='text-align:center;'><image src = " + image + " width = '1024' height = '821' /n></p>\n")
Func.write("<br>\n")
#title
Func.write("<center" + title + "</center>\n")
#copyright
#Func.write("<center>Image & Copyright: " + copyright + "</center>\n")
Func.write("<br>\n")
Func.write("<strong><center>Explanation: </strong>" + explanation + "</center>\n")
Func.write("<br>\n")
Func.write("</html>\n")

# Saving the data into the HTML file
Func.close()



#Flask Stuff. Used render_tempalte thing. Still not sure what it is
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def apod_json_file():
    return render_template("home.html")
if __name__ == '__main__':
    app.run()