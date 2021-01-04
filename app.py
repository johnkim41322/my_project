from flask import Flask, render_template, request, jsonify
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():  # 함수명 수정 - 이름만 보고 접속되는 페이지를 확인할 수 있게!
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def setStore():
    content = request.json
    print(content['stores'])
    db.stores.insert_many(content['stores'])
    return jsonify({'result': "success"})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)