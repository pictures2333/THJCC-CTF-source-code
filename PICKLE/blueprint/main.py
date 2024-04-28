from flask import Blueprint, redirect, request, render_template
import pickle, random

route = Blueprint('main', __name__)

def parse(file:str):
    with open(file, "rb") as f: item = pickle.load(f)
    return item.user, item.description

@route.route("/", methods = ['GET', "POST"])
def profile():
    if request.method == "GET": 
        u, d = parse("example/adminExample.pickle")
        return render_template("admin.html", user = u, des = d, fileHeader = "ExampleProfile")
    elif request.method == "POST":
        if 'file' in request.files:
            file = request.files['file']
            if file.filename == '': return "FAIL"
            else: 
                filename = f"uploads/{random.randint(1000000000, 9999999999)}.pickle"
                file.save(filename)
                with open(filename, "rb") as f: item = pickle.load(f)
                return render_template("admin.html", user = item.user, des = item.description, fileHeader = "Your Profile")
        else: return "FAIL"