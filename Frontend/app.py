from flask import Flask, render_template, request, jsonify, make_response, redirect, url_for, flash
import requests, json, os

app = Flask(__name__, static_url_path='')
app.secret_key = 'this is a secret key'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/allUsers", methods=["GET"])
def allUsers():
    try:
        response = requests.get("http://127.0.0.1:5000/user")
        data = response.json()
        # print(data)
        return render_template("view.html", users=data)
    except:
        return "<h1>Could not connect to Database Server.</h1>"

@app.route("/addUser", methods=["POST"])
def addUser():
    target = APP_ROOT+'/static/images'
    name = request.form.get("name")
    age = request.form.get("age")
    imagefile = request.files.get("img")
    image = ""
    if(imagefile):
        image = imagefile.filename
        destination = "/".join([target,image])
        imagefile.save(destination)
    else:
        image = 'img2.jpg'
    user = {
        "name" : name,
        "age" : age,
        "image": image
    }
    response = requests.post("http://127.0.0.1:5000/user", json=user)
    added_user = response.json()
    # print(added_user)
    msg = "User : \"" + added_user['name'] + "\" is ADDED successfully."
    flash(msg, "success")
    return redirect(url_for('index'))

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
    msg = "User : \"" + deleted_user['name'] + "\" is DELETED successfully."
    flash(msg, "success")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=5001)