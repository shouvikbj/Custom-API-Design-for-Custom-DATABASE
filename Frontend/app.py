from flask import Flask, render_template, request, jsonify, make_response, redirect
import requests, json

app = Flask(__name__, static_url_path='')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/allUsers", methods=["GET"])
def allUsers():
    try:
        response = requests.get("http://127.0.0.1:5000/user")
        data = response.json()
        # print(data)
        return jsonify(data)
    except:
        return "<h1>Could not connect to Database Server.</h1>"

@app.route("/addUser", methods=["POST"])
def addUser():
    name = request.form.get("name")
    age = request.form.get("age")
    user = {
        "name" : name,
        "age" : age
    }
    response = requests.post("http://127.0.0.1:5000/user", json=user)
    added_user = response.json()
    # print(added_user)
    return jsonify(added_user)

@app.route("/getUser", methods=["POST"])
def getUser():
    id = request.form.get('id')
    redirect_url = '/user/{}'.format(id)
    return redirect(redirect_url)

@app.route("/user/<id>")
def user(id):
    url = "http://127.0.0.1:5000/user/{}".format(id)
    response = requests.get(url)
    user = response.json()
    # print(user)
    return render_template("delete.html", user = user)

@app.route("/deleteUser/<id>", methods=["GET"])
def deleteUser(id):
    url = "http://127.0.0.1:5000/user/{}".format(id)
    response = requests.delete(url)
    deleted_user = response.json()
    # print(deleted_user)
    return jsonify(deleted_user)





if __name__ == "__main__":
    app.run(debug=True, port=5001)