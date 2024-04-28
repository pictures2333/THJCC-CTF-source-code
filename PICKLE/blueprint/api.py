from flask import Blueprint, redirect, request, send_file
from random import randint


api = Blueprint('api', __name__)

@api.route("/downloadExample")
def downloadHandler(): 
    if randint(1, 2) == 1: return send_file("example/adminExample.pickle", download_name="adminExample.pickle")
    else: return send_file("example/anotherExample.pickle", download_name="🦊.pickle")