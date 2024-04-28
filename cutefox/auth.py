from flask import make_response, redirect
import base64, re, sqlite3, string

# Cookie & Auth
def auth(content):
    try:
        username, password = base64.b64decode(content.encode()).decode(encoding="utf8").split("@")
        # 去除所有空格
        username = "".join(username.split())
        password = "".join(password.split())

        # 過濾username中所有特殊字符
        mu = re.match(r'.*\W', username)
        if mu is None: 
            # 過濾password中所有英文字母跟等號
            cflag = False
            for w in password: 
                if (w in string.ascii_letters) or (w == "="): cflag = True
            if (cflag): return None
            else:
                conn = sqlite3.connect("user.db")
                rows = conn.execute(f"select * from user where (user='{username}') and (pass='{password}');")

                result = None
                for row in rows: result = tuple(row)
                conn.close()

                if result is None: return None
                else: return str(result[0])
        else: return None
    except: return None 
def guestGive():
    res = make_response(redirect("/"))
    res.set_cookie("role", base64.b64encode("guest@?*&-</;<$)~~/%.!}{/\){%~:<!)-#%](]$-%(}]]_&|.}_-;#`^<&%&]>`~*~(^>+,}/#*&&:&|#|&{]#/#%^.;%-^%}$])<[\:)~[>\~{#^[/?;`#`))}^]\*;_/,<".encode()).decode(encoding="utf8"))
    return res