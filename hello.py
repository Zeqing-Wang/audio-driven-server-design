# -*- coding:utf-8 -*-
from flask import Flask,request,jsonify
from flask_cors import *


app = Flask(__name__)
CORS(app, supports_credentials=True)
# CORS(app, supports_credentials=True)
# 通过json传输数组数据
@app.route('/get_data')
def get_data():
    json_data = {
                "data1":[48, 57, 55, 80, 67, 67, 29, 19,20,15,5,11,3,100,190],
                "data2":[1, 57, 55, 300, 67, 67, 29, 19,20,15,5,11,3,10,190]
                }
    return json_data;


@app.route('/post_test', methods=['POST', 'GET'])
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

# 后端ip
host_ip = "127.0.0.1"
# 端口号
host_port = 15004

if __name__ == '__main__':
    app.run(host = host_ip, port = host_port, debug='True')