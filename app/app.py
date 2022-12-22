import base64
import time
import os
from dotenv import load_dotenv
from log.logger import get_logger
import json

from flask import Flask,render_template,request, jsonify, redirect, url_for
from flask.helpers import make_response

from prediction import AdelePrediction

load_dotenv(dotenv_path='./.env')
logger = get_logger('./app/log/adele-ndp/weed.log',level='info')
adele = AdelePrediction()

app = Flask(__name__)


def save_and_decode_image(request, logger):
    if 'file' not in request.files:
        file = request.get_json('file')
        if file:
            encoded_img = file['file'].split(',')[-1]
            base64_img = base64.b64decode(encoded_img)
            print('Decoded base64 image')
        else:
            print('Decode failed')
    else:
        file = request.files['file']
        print('Read image file')
        if file.filename == '':
            print('No filename')
    file_name = str(time.time())+'.jpg'
    if file:
        if isinstance(file,dict):
            with open(f'./upload/{file_name}', 'wb') as f:
                f.write(base64_img)
        else:
            file.save(os.path.join('./upload',file_name))
        logger.info(f'save image to ./upload/{file_name}')
    image_path = './upload/'+file_name
    return image_path


@app.route('/prediction',methods=['POST'])
def get_prediction():
    file_name = save_and_decode_image(request,logger)
    result = adele.prediction(file_name)
    return make_response(result);


@app.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'GET':
        return render_template('result.html',img=None)
    else:
        if 'take_photo' in request.files or 'upload_photo' in request.files:
            if request.files['upload_photo'].filename == '':
                f = request.files['take_photo']
            else:
                f = request.files['upload_photo']
            # f.save('./image.jpg')
            # data = open('./image.jpg', 'rb').read()
            image_string = base64.b64encode(f.read())
            data_base64 = image_string.decode()
            # os.remove('./image.jpg')

        img_base64 = 'data:image/jpeg;base64,' + data_base64

        return render_template('result.html',img=img_base64)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        print(request.files['file'])
        f = request.files['file']
        # f.save('./image.jpg')
        # data = open('./image.jpg', 'rb').read()
        image_string = base64.b64encode(f.read())
        data_base64 = image_string.decode()
        
    html = '<img src="data:image/jpeg;base64,' + data_base64 + '">'

    return html


@app.route('/blog',methods=['GET'])
def blog():
    article = request.args.get('article')
    print(article)    
    if article is None:
        return render_template('blog.html')
    else:
        data = {}
        with open('./app/static/data/def_and_pets.json') as json_file:
            data = json.load(json_file)
        if article in data:
            data = data[article]
        else:
            data = None
        return render_template('blog_details.html',data=data)


@app.route('/blog-legel-cannabisTH',methods=['GET'])
def blog_legel_cannabis():
    return render_template('blog_legel_weed.html')


@app.route('/blog-cannabis-medical',methods=['GET'])
def blog_cannabis_medical():
    return render_template('blog_weed_for_medical.html');


@app.route('/blog-cannabis-research',methods=['GET'])
def blog_cannabis_research():
    return render_template('blog_weed_for_research.html');


@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')
