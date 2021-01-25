from flask import Flask, render_template, request,jsonify
from flask_sqlalchemy import SQLAlchemy
import os,pytesseract
from cv2 import cv2
from PIL import Image
from voice import text_to_speech

#pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract'

app = Flask(__name__)

"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
db = SQLAlchemy(app)

class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)
"""

UPLOAD_FOLDER = os.path.basename('./static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

text=''

@app.route("/")
def main():
	return render_template('main.html')


@app.route("/upload", methods=['POST', 'GET'])
def upload():
    global text
    img = request.files['pic']
        
    """
    new_image = Images(name=img.filename, data=img.read())
    db.session.add(new_image)
    db.session.commit()

    return "Saved " + img.filename + " to the Database"
    """

    f = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
    img.save(f)
    saved_image = UPLOAD_FOLDER+"/"+img.filename
    image = cv2.imread(saved_image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    preprocess = request.form["preprocess"]
    if  preprocess == "thresh":
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


    elif preprocess == "blur":
        gray = cv2.medianBlur(gray, 3)
   

    filename = "images/{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    text1 = pytesseract.image_to_string(Image.open(filename))
    print(text1)
    print(type(text1))
    #text2=text.append(text1)
    text += text1 
    print(type(text))
    #print(str(text2))

    return render_template('text.html', text=text, filename=saved_image)

@app.route("/speech", methods=['POST', 'GET'])
def speech():
    if request.method == 'POST':
        #text = request.form['text']
        gender = request.form['voices']
        text_to_speech(text, gender)
        return render_template('speech.html')

if __name__ == '__main__':
	app.run(debug=True)
