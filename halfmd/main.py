from flask import Flask, render_template, redirect, abort, request, make_response, session
from flask_session import Session
import json, secrets

def auth(user:str):
    with open("user.json", "r", encoding = "utf8") as f: usr = json.load(f)
    if user in usr: return True
    else: return False

DOMAIN = "fake.scint.org"

FLAG = "THJCC{exampleFlag}"

# 公開檔案是這樣寫 #
# PASS = secrets.token_urlsafe(nbytes=64)
# HIDDEN = secrets.token_urlsafe(nbytes=64)
# END #

# 但題目檔案其實是這樣寫 #
with open("hidden", "r", encoding = "utf8") as f: hdta = json.load(f)
PASS = hdta['pass']
HIDDEN = hdta['hidden']
# END #

PORT = 10009

with open("hidden", "w", encoding = "utf8") as f: json.dump({
    "pass": PASS, "hidden": HIDDEN
}, f, ensure_ascii=False)

with open("user.json", "w", encoding = "utf8") as f: json.dump({
    f"admin@{DOMAIN}": {"mail": [{"user": "SYSTEM", "content":[ FLAG ]}]}, 
    f"guest@{DOMAIN}": {"mail": [{"user": "pour33142GX🌽", "content":[ "HalfMD 0.5 Demo", "# h1" , "## h2", "### h3", "**Format Example**" , "~~Format Example~~",
                                                               "``Format Example``", "*Format Example*", "==Format Example==",
                                                                "![Example Image](https://media1.tenor.com/m/2TeP31-goJcAAAAC/hamburger-dance.gif)",
                                                                 "[Example Link](https://youtube.com/@shirakamifubuki)" ]},
                                {
                                    "user":"pour33142GX🌽", "content":[f"Write a mail to the admin -> admin@{DOMAIN}", "And get the flag in the admin's mailbox."]
                                }]}
}, f, ensure_ascii=False)

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(nbytes=256)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_USE_SIGNER"] = True
Session(app)

@app.route("/")
def index(): 
    user = session.get("user")
    if auth(user): 
        with open("user.json", "r", encoding = "utf8") as f: usr = json.load(f)
        return render_template("index.html", username = user, mailList = usr[user]['mail'])
    else:
        session['user'] = f"guest@{DOMAIN}"
        return redirect("/")

@app.route("/sendmail", methods = ["POST"])
def sendmail():
    user = session.get("user")
    if auth(user): 
        to = request.form["to"]
        ctx = request.form["content"]

        if ("script" in ctx.lower()) or ("cookie" in ctx.lower()): return "ADMIN DOES NOT LIKE SCRIPT COOKIES"
        else:
            if auth(to): 
                with open("user.json", "r", encoding = "utf8") as f: usr = json.load(f)

                usr[to]['mail'].append({
                    "user": user, 
                    "content": ctx.split("\n")
                })
                with open("user.json", "w", encoding = "utf8") as f: json.dump(usr, f, ensure_ascii=False)

                return redirect("/")
            else: return "Wrong Address!"
    else: return "No Permission"

# 這是讓admin bot 接入的地方 #
@app.route(f"/{HIDDEN}", methods = ["GET"])
def admin():
    password = str(request.args.get("pass"))

    if (password == PASS):
        session['user'] = f"admin@{DOMAIN}"
        return redirect("/")
    else: return redirect("/")
# 寫得很爛很暴力 #

if __name__  == "__main__": app.run("0.0.0.0", PORT, debug = False)