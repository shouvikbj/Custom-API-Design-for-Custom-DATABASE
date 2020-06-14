from flask import Flask, request, jsonify
import db

app = Flask(__name__)

@app.route("/user", methods=["POST"])
def addData():
    name = request.json['name']
    age = request.json['age']
    image = request.json['image']
    result = db.enterData(name,age,image)
    if(result):
        user = {
            "name" : name,
            "age": age,
            "image": image
        }
    return jsonify(user)

@app.route("/user", methods=["GET"])
def getAllUsers():
    ret_users = []
    users = db.getData()
    for user in users:
        cur_user = {
            "id" : user[0],
            "name" : user[1],
            "age" : user[2],
            "image": user[3]
        }
        ret_users.append(cur_user)
    return jsonify(ret_users)

@app.route("/user/<id>", methods=["DELETE"])
def deleteUser(id):
    user = db.deleteData(id)
    if (len(user)):
        cur_user = {
            "id" : user[0][0],
            "name" : user[0][1],
            "age" : user[0][2],
            "image": user[0][3]
        }
        return jsonify(cur_user)
    else:
        cur_user = {
            "NO USER" : "no user found for deletion"
        }
        return jsonify(cur_user)

@app.route("/user/<id>", methods=["GET"])
def getOneUser(id):
    user = db.getOneData(id)
    if (len(user)):
        cur_user = {
            "id" : user[0][0],
            "name" : user[0][1],
            "age" : user[0][2],
            "image": user[0][3]
        }
        return jsonify(cur_user)
    else:
        cur_user = {
            "NO USER" : "no user found"
        }
        return jsonify(cur_user)





if __name__ == "__main__":
    app.run(debug=True)