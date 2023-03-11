# -*- coding:utf-8 -*-
from flask import Flask,request,jsonify
from flask_cors import *
import os
from urllib.parse import urljoin
import uuid

app = Flask(__name__)
CORS(app, supports_credentials=True)

# 进行一系列后端限制
# 允许的文件扩展名
ALLOWED_EXTENSIONS = {'wav', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
# 保存WAV文件文件夹
UPLOAD_FOLDER = 'wav'
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# 允许上传文件的大小 定为5M
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

# CORS(app, supports_credentials=True)

# 检查后缀是否为允许的文件
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 随机生成文件名
def random_filename(filename):
    ext = os.path.splitext(filename)[-1]
    return uuid.uuid4().hex + ext

# 通过json传输数组数据
@app.route('/get_data')
def get_data():
    json_data = {
                "data1":[48, 57, 55, 80, 67, 67, 29, 19,20,15,5,11,3,100,190],
                "data2":[1, 57, 55, 300, 67, 67, 29, 19,20,15,5,11,3,10,190]
                }
    return json_data;


@app.route('/post_test', methods=['POST'])
def post_test():
    response_object = {'status': 'success'}
    app.logger.info("Received Post!")
    if request.method == 'POST':
        # app.logger.info("Received ",str(request))
        post_data = request.get_json()
        style_value = post_data['style_value'].get('_value')
        id_value = post_data['id_value'].get('_value')
        text = post_data['text'].get('_value')
        app.logger.info("Received post_data: style_value: {0}; id_value: {1}; text: {2}".format(style_value, id_value, text))
        # RESOURCES = []
        # RESOURCES.append({
        #     'sn': post_data.get('sn'),
        #     'teacher': post_data.get('teacher'),
        #     'learnt': post_data.get('learnt')
        # })
        # response_object['message'] = '资源添加成功！'
        # app.logger.info("Received ", RESOURCES)
        # print('receive name', name)
        return 'ok'
    else:
        return 'bad'
    return jsonify(response_object)
    pass

# 用于测试文件上传接口
@app.route('/post_upload', methods=['POST'])
def post_upload():
    response_object = {'status': 'success'}
    app.logger.info("Received Post Data Form!")
    if request.method == 'POST':
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            print(file.filename)
            filename = random_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(os.path.join(app.root_path, filepath))
            file_url = urljoin(request.host_url, filepath)
            print('url:',file_url)
        return 'ok'
    else:
        return 'bad'


# 后端ip
host_ip = "127.0.0.1"
# 端口号
host_port = 9090

if __name__ == '__main__':
    app.run(host = host_ip, port = host_port, debug='True')