from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from pymongo import MongoClient
import json
from bson import ObjectId

# connect to mongodb
client = MongoClient('mongodb://admin:adm00n@test-cluster-shard-00-00-zk4lm.mongodb.net:27017,test-cluster-shard-00-01-zk4lm.mongodb.net:27017,test-cluster-shard-00-02-zk4lm.mongodb.net:27017/test?ssl=true&replicaSet=test-cluster-shard-0&authSource=admin&retryWrites=true')

db = client['crud']
coll = db['item']

# provide context to flask
app = Flask(__name__)

# json encoder for objectId mongodb
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        else:
            pass
        return json.JSONEncoder.default(self, o)

@app.route('/', methods=['GET'])
def get_item():
    res = []
    for x in coll.find():
        res.append(x)
    
    #jsonify the encoded result
    return jsonify({'items': json.loads(JSONEncoder().encode(res))}), 200

@app.route('/name=<name>', methods=['GET'])
def get_item_by_name(name):
    res = []
    query = {'name' : name}
    for x in coll.find(query):
        res.append(x)
    return jsonify({'items': json.loads(JSONEncoder().encode(res))}), 200

@app.route('/', methods=['POST'])
def post_item():
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    parser.add_argument('age')
    parser.add_argument('detail')
    args = parser.parse_args()
    
    obj = {
        'name': args['name'],
        'age': args['age'],
        'detail': args['detail']
    }
    coll.insert_one(obj)
    return 'item posted successfully', 201

# run the backend
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
