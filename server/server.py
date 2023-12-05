from flask import Flask, request
from bson import json_util
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/data', methods=['POST', 'GET', 'PUT', 'DELETE']) #to get data of blogs
def blog_data():
    with MongoClient() as client:
        db = client['newblog']
        col = db.blogs
        col_list = list(col.find({},{'_id': False}))
        if request.method == 'GET':
            try:
                return col_list
            except:
                return "Did not get Database"
        elif request.method == 'POST':
            try:
                title = request.json["title"]
                id = len(col_list) + 1
                return str(col.insert_one({"title": title, "id": id}))
            except:
                return "Did not include data"
        elif request.method == 'PUT':
            try:
                id = request.json["id"]
                title = request.json["title"]
                return col.update({"id": id}, {"$set": {"title": title}})
            except:
                return "Did not update"
        elif request.method == 'DELETE':
            try:
                id = request.json["id"]
                
            except:
                pass
       
  

@app.route('/users') #to get data of users
def blog_users():
    with MongoClient() as client:
        db = client['newblog']
        col = db.blogs
        print(col.find())
        return list(col.find({}, {'firstName':1, '_id':0}))
    

if __name__ == '__main__':
    app.run(debug=True)
