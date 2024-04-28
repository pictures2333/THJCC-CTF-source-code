from flask import Flask, request, redirect, render_template
from auth import *

# Main
PORT = 10010

FLAG = "THJCC{exampleFlag}"

app = Flask(__name__)

# Routes
@app.route("/")
def index():
    cookie = request.cookies.get("role")
    if cookie is None: return guestGive()
    else:
        authCookie = auth(cookie)
        if authCookie is None: return guestGive()
        elif authCookie == "guest" or authCookie == "admin": return redirect("/flag")
        else: return guestGive()

@app.route("/flag", methods = ['GET', "POST"])
def profile():
    cookie = request.cookies.get("role")
    if cookie is None: return redirect("/")
    else:
        authCookie = auth(cookie)
        if authCookie is None: return redirect("/")
        elif authCookie == "guest": return render_template("main.html")
        elif authCookie == "admin": return FLAG + "<img src=\"https://media1.tenor.com/m/wm_jigc51u8AAAAC/fubuki-%E7%99%BD%E4%B8%8A%E3%83%95%E3%83%96%E3%82%AD.gif\" style=\"width: 100%;\" /><title>Flag</title>"
        else: return redirect("/")

if __name__ == "__main__": app.run("0.0.0.0", PORT, debug=False)